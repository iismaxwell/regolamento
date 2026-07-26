#!/usr/bin/env python3
"""Genera assets/icone.html a partire dagli SVG in assets/icone/.

Le icone sono Phosphor Icons in stile duotone (licenza MIT, v. assets/icone/LICENSE)
e sostituiscono a pagina caricata le Bootstrap Icons che Quarto inserisce da sé.
Gli SVG di Phosphor hanno fill="currentColor" e il tratto secondario a opacità 0.2:
inseriti nel documento ereditano il colore del tema, chiaro o scuro che sia.

Uso:  python3 assets/genera-icone.py     (dalla radice del repo del regolamento)
Il file prodotto è versionato: rigenerarlo solo se si cambiano o aggiungono icone.
"""

import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parent
SVG_DIR = BASE / "icone"
USCITA = BASE / "icone.html"

# Classe Bootstrap Icons usata da Quarto -> nome dell'icona Phosphor
SOSTITUZIONI = {
    "bi-download": "download-simple",
    "bi-file-pdf": "file-pdf",
    "bi-file-word": "file-doc",
    "bi-clock-history": "clock-counter-clockwise",
    "bi-exclamation-triangle": "warning",
    "bi-layout-text-sidebar-reverse": "list-dashes",
    "bi-chevron-right": "caret-right",
    "bi-arrow-left-short": "arrow-left",
    "bi-arrow-right-short": "arrow-right",
}

# Icone usate dallo script ma non legate a una classe .bi: commutatore di tema,
# lente della ricerca (che l'autocomplete disegna per conto suo) e copia-link.
EXTRA = ["moon", "sun-dim", "magnifying-glass", "link-simple"]


def leggi(nome: str) -> str:
    svg = (SVG_DIR / f"{nome}.svg").read_text(encoding="utf-8").strip()
    svg = re.sub(r"\s+", " ", svg)
    # aria-hidden: l'icona è sempre accompagnata da un'etichetta testuale o da un
    # aria-label sull'elemento che la contiene.
    return svg.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)


def main() -> None:
    icone = {nome: leggi(nome) for nome in sorted(set(SOSTITUZIONI.values()) | set(EXTRA))}
    voci = ",\n    ".join(f'"{k}": {js_stringa(v)}' for k, v in icone.items())
    mappa = ",\n    ".join(f'"{k}": "{v}"' for k, v in SOSTITUZIONI.items())
    USCITA.write_text(MODELLO.format(icone=voci, mappa=mappa), encoding="utf-8")
    print(f"scritto {USCITA.relative_to(BASE.parent)} ({len(icone)} icone)")


def js_stringa(svg: str) -> str:
    return "'" + svg.replace("\\", "\\\\").replace("'", "\\'") + "'"


MODELLO = '''<script>
// GENERATO DA assets/genera-icone.py — non modificare a mano.
// Icone Phosphor duotone (MIT, v. assets/icone/LICENSE) al posto delle Bootstrap
// Icons che Quarto inserisce nella barra di navigazione, nell'indice e negli
// avvisi. La sostituzione avviene a pagina caricata: gli SVG ereditano il colore
// del testo, quindi seguono da soli il tema chiaro o scuro.
(function () {{
  var ICONE = {{
    {icone}
  }};

  var MAPPA = {{
    {mappa}
  }};

  // Esposta anche fuori: assets/copy-link.html la usa per il pulsante copia-link.
  window.iconaMaxwell = function (nome, classi) {{
    var span = document.createElement("span");
    span.className = "icona" + (classi ? " " + classi : "");
    span.innerHTML = ICONE[nome] || "";
    return span;
  }};

  function sostituisci(vecchio, nome) {{
    if (!ICONE[nome]) return;
    // Le classi di spaziatura di Bootstrap (pe-1, ms-2) vanno conservate.
    var tenute = Array.prototype.filter.call(vecchio.classList, function (c) {{
      return c !== "bi" && c.indexOf("bi-") !== 0;
    }});
    var nuovo = window.iconaMaxwell(nome, tenute.join(" "));
    ["role", "aria-label", "title"].forEach(function (attr) {{
      if (vecchio.hasAttribute(attr)) nuovo.setAttribute(attr, vecchio.getAttribute(attr));
    }});
    vecchio.replaceWith(nuovo);
  }}

  document.addEventListener("DOMContentLoaded", function () {{
    Object.keys(MAPPA).forEach(function (classe) {{
      document.querySelectorAll("i." + classe).forEach(function (i) {{
        sostituisci(i, MAPPA[classe]);
      }});
    }});

    // Commutatore chiaro/scuro: Quarto lascia un <i class="bi"> vuoto e ci
    // disegna sopra il glifo via CSS. Qui ci vanno due icone, luna e sole, e a
    // mostrarne una sola pensano le classi light-content/dark-content di Quarto:
    // in tema chiaro si vede la luna (che porta allo scuro) e viceversa.
    document.querySelectorAll(".quarto-color-scheme-toggle").forEach(function (toggle) {{
      var vuota = toggle.querySelector("i.bi");
      if (!vuota) return;
      var luna = window.iconaMaxwell("moon", "light-content");
      var sole = window.iconaMaxwell("sun-dim", "dark-content");
      vuota.replaceWith(luna, sole);
    }});

    // Lente della ricerca: la disegna la libreria di autocomplete, non Quarto.
    document.querySelectorAll("#quarto-search svg.aa-SubmitIcon").forEach(function (svg) {{
      var lente = window.iconaMaxwell("magnifying-glass", "aa-SubmitIcon");
      svg.replaceWith(lente);
    }});
  }});
}})();
</script>
'''


if __name__ == "__main__":
    main()

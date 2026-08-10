# Regolamento d'istituto — IIS J.C. Maxwell (Nichelino)

> **Stato: bozza in lavorazione — non è il regolamento vigente dell'Istituto.**
> Questo repository contiene una proposta di nuovo regolamento d'istituto,
> in corso di redazione. Diventerà «regolamento» solo con la delibera del
> Consiglio d'istituto, di cui il changelog darà conto.

## Cos'è

Il regolamento è mantenuto come documento **versionato e pubblico**: il testo
sorgente è in Markdown (Quarto), ogni modifica è tracciata, ogni versione ha un
numero `x.y.z` e una voce nel [changelog](CHANGELOG.md). Dal sorgente si
generano il sito web consultabile, il PDF e il DOCX.

## Struttura

- `index.qmd` — premessa
- `parti/` — il corpo del regolamento, una parte per file
- `allegati/` — patto di corresponsabilità, tabelle disciplinari, disciplina
  d'uso dell'IA, glossario
- `pagine/` — riferimenti normativi, dichiarazione di accessibilità,
  changelog renderizzato (incluso da `CHANGELOG.md`)
- `assets/` — tema del sito, logo, reference.docx
- `CHANGELOG.md` — storia delle versioni
- `STILE.md` — convenzioni di redazione e tipografia

## Versioni

- **MAJOR** — revisione organica dell'impianto (nuova delibera sull'intero testo)
- **MINOR** — modifica, aggiunta o abrogazione di articoli o allegati (delibera
  sulla modifica)
- **PATCH** — correzioni formali senza effetto normativo

## Come si genera

Con [Quarto](https://quarto.org) installato (richiede anche Typst, incluso
nella distribuzione Quarto):

```sh
quarto render                              # il sito in _book/
quarto render --profile stampa --no-clean  # vi aggiunge PDF e DOCX
quarto preview                             # anteprima locale del sito, con ricarica automatica
```

Le due corse vanno in quest'ordine: la prima ripulisce `_book/` e genera il
sito, la seconda vi affianca i due documenti (senza `--no-clean` cancellerebbe
il sito appena prodotto).

Sono corse distinte perché il documento scaricabile non contiene tutto il sito:
la **dichiarazione di accessibilità** e il **changelog** descrivono il sito, non
il regolamento, e restano fuori da PDF e DOCX. In un libro Quarto un capitolo non
si può escludere per formato, quindi i due profili di render — `sito`
(predefinito, `_quarto-sito.yml`) e `stampa` (`_quarto-stampa.yml`) — dichiarano
elenchi di allegati e formati diversi; `_quarto.yml` tiene ciò che hanno in comune.

Il sito (`_book/index.html` e seguenti) è pubblicato su GitHub Pages a ogni
push su `main` (`.github/workflows/publish.yml`). Quando si crea un tag
`v*`, lo stesso workflow allega PDF e DOCX come artefatti della release.

## Licenza

Proposta: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it)
— in attesa di conferma definitiva.

Materiali di terzi inclusi nel sito, con licenza propria:

- **Cormorant Garamond** e **Lora** (`assets/fonts/`): SIL Open Font License 1.1.
- **Phosphor Icons**, stile duotone (`assets/icone/`): licenza MIT, copia in
  `assets/icone/LICENSE`. Le icone incluse sono solo quelle usate dal sito; lo
  script `assets/genera-icone.py` rigenera `assets/icone.html` a partire da esse.

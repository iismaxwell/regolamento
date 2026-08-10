# Repo pubblico del regolamento — regole editoriali

Questo è il repo **pubblico** del regolamento d'istituto dell'IIS J.C. Maxwell.
La progettazione (wiki, piano, fonti, spec) vive nel repo privato che contiene
questa cartella: se la sessione è aperta qui e serve contesto di progetto,
chiedere a Marco di aprirla dalla radice del progetto.

## Regole dure

- **Niente materiale di progettazione qui dentro**: non citare, copiare o
  committare file di `../progettazione/` (è un repo privato; questo è pubblico).
- **Ogni modifica al testo normativo passa dal changelog**: nessun commit che
  cambia parti/allegati senza la voce corrispondente in `CHANGELOG.md` e il
  bump di versione coerente (semantica nel README § Versioni). Correzioni di
  refusi = PATCH, comunque a changelog.
- La versione compare in più punti da tenere allineati: l'intestazione più
  recente di `CHANGELOG.md` e, in `_quarto.yml`, il `subtitle` del libro, il
  badge in `book.navbar.right` e il testo in `book.page-footer.center`.
- **Due profili di render**, non uno: `quarto render` fa il sito,
  `quarto render --profile stampa --no-clean` vi aggiunge PDF e DOCX (in
  quest'ordine: la prima corsa ripulisce `_book/`). Il profilo `stampa` non ha
  la dichiarazione di accessibilità né il changelog, che descrivono il sito e
  non il regolamento; un nuovo capitolo va aggiunto a `_quarto.yml`, non ai
  profili, se deve stare in tutti i formati. V. README § Come si genera.
- Stile e tipografia: `STILE.md`, sempre.
- Riferimenti normativi: mai a memoria; se non è verificabile, marcare
  `<!-- TODO-VERIFICA -->` e segnalarlo.
- Il testo è una **proposta non vigente** finché il changelog non registra la
  delibera del Consiglio d'istituto: non rimuovere gli avvisi di stato da
  README e premessa prima di quel momento.
- Commit in italiano, imperativi e specifici (`f5: parte 06 disciplina`,
  `patch: refusi parte 04`).

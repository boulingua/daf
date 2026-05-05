# Rechtliches — Pflege- und Build-Hinweise

Dieses Repository veröffentlicht eine DSGVO-konforme Konfiguration:

- `impressum.qmd` — Anbieter nach § 5 DDG, § 18 Abs. 2 MStV
- `datenschutz.qmd` — Datenschutzerklärung mit allen Drittanbietern
  (Plausible self-hosted, VG Wort, GitHub Pages, Google Fonts)
- `haftungsausschluss.qmd` — Haftung Inhalte, Haftung Links,
  Urheberrecht

Im Header oben rechts erscheinen alle drei unter dem Eintrag
**Rechtliches**, im Footer als eigene Linkgruppe inkl. Kontakt.

## Plausible Analytics

Eingebunden über `_quarto.yml` → `format.html.include-in-header`.
Die Instanz ist selbst gehostet auf `analytics.hellebo.de`
(Server in Deutschland). Skript:

```html
<script defer data-domain="boulingua.github.io/daf"
  src="https://analytics.hellebo.de/js/script.file-downloads.outbound-links.js"></script>
```

## VG Wort Standard-Zählpixel

Die Pixel werden über den Pandoc-Lua-Filter
`_scripts/vgwort.lua` ausgegeben, sobald in der YAML-Frontmatter
einer Seite `vgwort_pixel: "<token>"` gesetzt ist.

### Workflow pro zählpflichtige Seite

1. **Token besorgen**: in [VG Wort T.O.M.](https://tom.vgwort.de/)
   neue Zählmarke ziehen. Eine Marke ist **single-use**:
   genau ein Werk, nicht wiederverwenden.
2. **Mindestlänge prüfen**: das Werk muss mindestens
   **1.500 Zeichen** Text (ohne Leerzeichen, ohne Code-Blöcke,
   ohne Bildunterschriften) umfassen, sonst nimmt VG Wort die
   Meldung im METIS-Standard-Verfahren nicht an.
3. **Frontmatter ergänzen**:
   ```yaml
   ---
   title: "Meine Einheit"
   vgwort_pixel: "vg08.met.vgwort.de/na/0123456789abcdef0123456789abcdef"
   ---
   ```
4. **Filter aktivieren** (einmalig pro Repo, in `_quarto.yml`):
   ```yaml
   filters:
     - _scripts/vgwort.lua
   ```
5. Das Pixel wird ausschließlich auf Seiten mit gesetztem Token
   gerendert. Übersichtsseiten, Listen, Impressum/Datenschutz/
   Haftungsausschluss bleiben pixelfrei.

### Was nicht zählpflichtig pixeln

- Startseiten, Listings, 404-Seiten,
- Übersichtsseiten ohne fortlaufenden Fließtext,
- die drei Rechtliches-Seiten,
- Werke unter 1.500 Zeichen.

## CI-Guard gegen unausgefüllte Platzhalter

`scripts/check-legal-placeholders.sh` scannt das gerenderte
Output-Verzeichnis (`docs/`) auf Platzhalter, die im Live-Betrieb
nichts verloren haben. Das Skript schlägt fehl, wenn es einen
Treffer findet. Lokal ausführbar:

```bash
bash scripts/check-legal-placeholders.sh
```

Geprüft wird auf:

- `{{CONTACT_EMAIL_HELLER}}`
- `{{CONTACT_EMAIL_LEBOULANGER}}`
- `{{SITE_DOMAIN}}`
- die Marker `TODO` / `FIXME` innerhalb von `legal/` bzw.
  `docs/legal/`.

Wenn dieses Repo eine GitHub-Actions-Pipeline besitzt, ist der
Aufruf nach dem Build einzuhängen.

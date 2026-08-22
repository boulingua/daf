# Fonts shipped by this repository

Seven self-hosted faces. All are Google Fonts cuts rather than
`kit/design/build_fonts.py` output, because this course uses the 300 and 500
weights of the body face, which are in no kit tier.

Self-hosting rather than linking `fonts.googleapis.com` is deliberate: a
webfont request from a learner's browser to a third party is a data transfer
the Datenschutzerklärung would have to declare, and many of these learners are
children.

These files are not covered by `kit/design/fonts/ATTRIBUTION.md`, which
documents the kit's own subsets. Gate A4 reads both.

| File | Family | Licence | Upstream |
|---|---|---|---|
| `source-sans-3-v19-latin_latin-ext-300.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-regular.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-500.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-600.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `source-sans-3-v19-latin_latin-ext-700.woff2` | Source Sans 3 | OFL 1.1 | <https://github.com/adobe-fonts/source-sans> |
| `jetbrains-mono-v24-latin_latin-ext-regular.woff2` | JetBrains Mono | OFL 1.1 | <https://github.com/JetBrains/JetBrainsMono> |
| `jetbrains-mono-v24-latin_latin-ext-500.woff2` | JetBrains Mono | OFL 1.1 | <https://github.com/JetBrains/JetBrainsMono> |

Licence texts: [`kit/design/fonts/LICENSES/`](https://github.com/boulingua/kit/tree/main/design/fonts/LICENSES).
Both families are the same OFL projects the kit documents; only the cut differs.

The `latin-ext` subset is required, not optional: German needs ä ö ü ß and the
course teaches names and loanwords well outside basic Latin.

---
title: "Materials Network — Layout-Vorschau"
description: "Statische HTML/CSS-Vorschau des Materials-Discovery-Layouts (Phase 5, Phase 2). Keine Interaktivität."
preview_only: true
---

> **Phase-2-Vorschau.** Diese Seite zeigt das geplante Layout der
> Materials-Discovery-Seite. Alle Daten sind hartkodiert, kein
> JavaScript läuft — bewertet wird nur Struktur, Abstände und Farben.
> Die Phase-3-Implementierung verbindet die Filter live mit dem
> Cytoscape-Graph und der Karten-Liste.

<section class="network-page" aria-label="Materials network preview">

  <div class="network-search">
    <span aria-hidden="true">⌕</span>
    <input type="search" placeholder="Titel, Stichwort, Modul…" disabled value="">
    <button type="button" disabled>Reset</button>
  </div>

  <aside class="network-rail" aria-label="Filter">

    <div class="facet-group">
      <h4>Typ</h4>
      <label class="facet-checkbox"><input type="checkbox" checked disabled><span class="glyph">●</span>Artikel <span class="count">60</span></label>
      <label class="facet-checkbox"><input type="checkbox" checked disabled><span class="glyph">■</span>Foliensatz <span class="count">60</span></label>
      <label class="facet-checkbox"><input type="checkbox" checked disabled><span class="glyph">◆</span>Arbeitsblatt <span class="count">60</span></label>
    </div>

    <div class="facet-group">
      <h4>Kurs</h4>
      <div class="facet-chips">
        <button class="facet-chip" aria-pressed="false" disabled>A1 <span class="count">12</span></button>
        <button class="facet-chip" aria-pressed="false" disabled>A2 <span class="count">12</span></button>
        <button class="facet-chip" aria-pressed="true" disabled>B1 <span class="count">12</span></button>
        <button class="facet-chip" aria-pressed="false" disabled>B2 <span class="count">12</span></button>
        <button class="facet-chip" aria-pressed="false" disabled>C1 <span class="count">12</span></button>
      </div>
    </div>

    <div class="facet-group">
      <h4>Topic</h4>
      <div class="facet-chips">
        <button class="facet-chip topic" data-topic="alltag" aria-pressed="false" disabled><span class="swatch"></span>Alltag <span class="count">17</span></button>
        <button class="facet-chip topic" data-topic="gesellschaft" aria-pressed="true" disabled><span class="swatch"></span>Gesellschaft <span class="count">11</span></button>
        <button class="facet-chip topic" data-topic="kultur" aria-pressed="false" disabled><span class="swatch"></span>Kultur <span class="count">10</span></button>
        <button class="facet-chip topic" data-topic="wissenschaft" aria-pressed="false" disabled><span class="swatch"></span>Wissenschaft <span class="count">8</span></button>
        <button class="facet-chip topic" data-topic="arbeit" aria-pressed="false" disabled><span class="swatch"></span>Arbeit <span class="count">7</span></button>
        <button class="facet-chip topic" data-topic="umwelt" aria-pressed="false" disabled><span class="swatch"></span>Umwelt <span class="count">5</span></button>
        <button class="facet-chip topic" data-topic="kommunikation" aria-pressed="false" disabled><span class="swatch"></span>Kommunikation <span class="count">5</span></button>
      </div>
    </div>

    <div class="facet-group">
      <h4>Tags</h4>
      <div class="facet-chips">
        <button class="facet-chip" disabled>modul-sprechen <span class="count">15</span></button>
        <button class="facet-chip" disabled>modul-lesen <span class="count">15</span></button>
        <button class="facet-chip" disabled>skill-schreiben <span class="count">26</span></button>
        <button class="facet-chip" disabled>skill-sprachmittlung <span class="count">3</span></button>
        <button class="facet-chip is-empty" disabled>skill-sprachreflexion <span class="count">0</span></button>
        <button class="facet-chip" disabled>+ 17 weitere</button>
      </div>
    </div>

    <div class="facet-group">
      <button class="facet-chip" disabled>Filter zurücksetzen</button>
    </div>

  </aside>

  <div class="network-graph" aria-label="Force-directed graph (mock)">
    <svg class="graph-mock-svg" viewBox="0 0 600 400" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Beispiel-Graph mit 12 Knoten">
      <!-- structural edges -->
      <g stroke="currentColor" stroke-opacity="0.3" stroke-width="1.5">
        <line x1="180" y1="120" x2="240" y2="160"></line>
        <line x1="180" y1="120" x2="200" y2="80"></line>
        <line x1="320" y1="200" x2="380" y2="180"></line>
        <line x1="320" y1="200" x2="360" y2="240"></line>
        <line x1="450" y1="120" x2="490" y2="160"></line>
        <line x1="450" y1="120" x2="430" y2="80"></line>
      </g>
      <!-- shared-tag edges -->
      <g stroke="#9B7EBD" stroke-opacity="0.35" stroke-width="1">
        <line x1="240" y1="160" x2="320" y2="200"></line>
        <line x1="240" y1="160" x2="380" y2="180"></line>
        <line x1="320" y1="200" x2="450" y2="120"></line>
        <line x1="180" y1="120" x2="450" y2="120"></line>
      </g>
      <g stroke="#7C9885" stroke-opacity="0.35" stroke-width="1">
        <line x1="120" y1="280" x2="240" y2="160"></line>
        <line x1="120" y1="280" x2="180" y2="320"></line>
      </g>
      <!-- nodes -->
      <g>
        <circle cx="240" cy="160" r="12" fill="#9B7EBD"></circle>
        <circle cx="320" cy="200" r="14" fill="#9B7EBD"></circle>
        <circle cx="450" cy="120" r="11" fill="#9B7EBD"></circle>
        <circle cx="120" cy="280" r="11" fill="#7C9885"></circle>

        <rect x="172" y="112" width="16" height="16" fill="#9B7EBD" fill-opacity="0.8"></rect>
        <rect x="370" y="170" width="16" height="16" fill="#9B7EBD" fill-opacity="0.8"></rect>
        <rect x="420" y="70" width="16" height="16" fill="#9B7EBD" fill-opacity="0.8"></rect>

        <g transform="translate(200,80)"><polygon points="0,-9 9,0 0,9 -9,0" fill="#7C9885" fill-opacity="0.8"></polygon></g>
        <g transform="translate(360,240)"><polygon points="0,-9 9,0 0,9 -9,0" fill="#9B7EBD" fill-opacity="0.8"></polygon></g>
        <g transform="translate(490,160)"><polygon points="0,-9 9,0 0,9 -9,0" fill="#9B7EBD" fill-opacity="0.8"></polygon></g>
        <g transform="translate(180,320)"><polygon points="0,-9 9,0 0,9 -9,0" fill="#7C9885" fill-opacity="0.8"></polygon></g>

        <!-- highlighted node (gold ring) -->
        <circle cx="320" cy="200" r="20" fill="none" stroke="#E8C547" stroke-width="2"></circle>
      </g>
    </svg>
    <div class="graph-legend">
      ● Artikel · ■ Foliensatz · ◆ Arbeitsblatt
    </div>
  </div>

  <div class="network-status">
    <span><strong>12</strong> Einträge sichtbar (von 180)</span>
    <span><a href="#">Filter zurücksetzen</a></span>
  </div>

  <div class="network-list" id="preview-list">
    <article class="network-card article" data-topic="gesellschaft">
      <span class="meta">Artikel · B1 · Gesellschaft</span>
      <h3 class="title"><a href="/kurs_b1/units/unit10_politik-und-teilhabe/">Politik und Teilhabe: Wahlen und Bürgerinitiativen</a></h3>
      <div class="tag-row">
        <span class="tag">level-b1</span>
        <span class="tag">modul-sprechen</span>
        <span class="tag">topic-gesellschaft</span>
      </div>
      <div class="type-row">
        <span class="glyph">● Artikel</span>
        <span class="glyph">■ Foliensatz</span>
        <span class="glyph">◆ Arbeitsblatt</span>
      </div>
    </article>

    <article class="network-card" data-topic="gesellschaft">
      <span class="meta">Foliensatz · B1</span>
      <h3 class="title">Politik und Teilhabe (Slides)</h3>
      <span class="placeholder-badge">Platzhalter</span>
      <div class="tag-row"><span class="tag">level-b1</span><span class="tag">topic-gesellschaft</span></div>
    </article>

    <article class="network-card" data-topic="gesellschaft">
      <span class="meta">Arbeitsblatt · B1</span>
      <h3 class="title">Politik und Teilhabe (PDF)</h3>
      <span class="placeholder-badge">Platzhalter</span>
      <div class="tag-row"><span class="tag">level-b1</span><span class="tag">topic-gesellschaft</span></div>
    </article>

    <article class="network-card article" data-topic="gesellschaft">
      <span class="meta">Artikel · B1 · Gesellschaft</span>
      <h3 class="title"><a href="/kurs_b1/units/unit08_stadt-und-land/">Stadt und Land</a></h3>
      <div class="tag-row">
        <span class="tag">level-b1</span>
        <span class="tag">modul-lesen</span>
        <span class="tag">topic-gesellschaft</span>
      </div>
      <div class="type-row">
        <span class="glyph">● Artikel</span>
        <span class="glyph">■ Foliensatz</span>
        <span class="glyph">◆ Arbeitsblatt</span>
      </div>
    </article>

    <article class="network-card article" data-topic="alltag">
      <span class="meta">Artikel · B1 · Alltag</span>
      <h3 class="title"><a href="/kurs_b1/units/unit01_neuanfang-in-basel/">Neuanfang in Basel — Arbeitsleben in zwei Ländern</a></h3>
      <div class="tag-row">
        <span class="tag">level-b1</span>
        <span class="tag">modul-sprechen</span>
        <span class="tag">topic-alltag</span>
      </div>
    </article>

    <article class="network-card" data-topic="alltag">
      <span class="meta">Foliensatz · B1</span>
      <h3 class="title">Neuanfang in Basel (Slides)</h3>
      <span class="placeholder-badge">Platzhalter</span>
    </article>

  </div>

</section>

## Was diese Vorschau zeigt

- **Layout-Raster** — vier Bereiche (Suche · Rail · Graph · Status · Liste) auf Desktop in einem CSS-Grid; auf Tablet stapelt der Rail über dem Graph; auf Mobile entfällt der Graph komplett (nur Filter + Liste).
- **Farb-Tokens** — sieben Topic-Farben aus `data/topics.yml` plus die Gold-Highlight-Farbe für Hover/Selection. Jede Karte trägt einen 4 px breiten linken Rand in der Topic-Farbe.
- **Knoten-Glyphen** — ● Artikel, ■ Foliensatz, ◆ Arbeitsblatt. Im Graph als SVG; in den Karten als Type-Zeile rechts oben.
- **Aktiv-Status** — der lila B1-Chip und der Gesellschaft-Chip sind in „aktiv" (Gold). Genauso werden Filter im Live-System aussehen.
- **Platzhalter-Badge** — dezenter Goldstreifen auf Karten für Materialien, deren Inhalt noch Platzhalter ist (alle 60 derzeit).

Phase 3 (nächste): echtes Cytoscape-Rendering aus `/network/graph.json`, gleicher Style, mit Theme-Wechsel via `MutationObserver` auf `data-theme`.

# GoreeCloud — Deep Cloud Wordmark Specification

## Status

I selected **Two Tone — Deep Cloud** as the GoreeCloud wordmark direction on August 19, 2026. I have now completed the corrected canonical-candidate production build for the wordmark and its principal lockups.

The already-approved GoreeCloud platform symbol remains **Unified Clean — Blue** in `official/goreecloud-logo.svg`. Wordmark production does not alter that symbol.

The current production package is a **canonical candidate** pending promotion of the generated outlined SVG outputs into `official/` and the corresponding final status update. This distinction prevents an editable or intermediate source from silently becoming the authoritative identity master.

## Selected visual hierarchy

The full-color wordmark uses two restrained text roles:

- `Goree` — dark neutral `#111827`;
- `Cloud` — GoreeCloud Deep Blue `#174EA6`.

The distinction is intentionally typographic and chromatic rather than illustrative. I do not insert a space, separator, icon, cloud pictogram, gradient, outline, glow, or other decorative element between `Goree` and `Cloud`.

## Production typography

The production build uses **DejaVu Sans Bold** as its open-source type foundation and converts the rendered lettering into SVG path geometry. Distributed canonical-candidate SVGs therefore do not require the typeface to be installed on the consuming system.

This resolves the principal reproducibility requirement: the appearance of the production artwork is determined by vector geometry rather than by browser, operating-system, or application font substitution.

The repository retains a deterministic build path so the relationship between the source typography and generated vector artwork remains maintainable and auditable.

## Corrected canonical-candidate build

The production build was corrected after validation identified cropping risk in the standalone wordmark and stacked arrangement. The corrected package rebuilds the relevant view boxes and positioning so the complete lettering remains inside the intended canvas.

The corrected package contains:

- primary Deep Cloud wordmark;
- primary horizontal symbol + wordmark lockup;
- primary stacked symbol + wordmark lockup;
- reversed wordmark;
- reversed horizontal lockup;
- reversed stacked lockup;
- monochrome wordmark;
- monochrome horizontal lockup;
- monochrome stacked lockup;
- PNG previews/derivatives corresponding to the vector candidates.

The corrected package supersedes the earlier preliminary production export where the standalone/stacked bounds were not yet fully validated.

## Horizontal lockup

The horizontal lockup is the preferred full identity where adequate width is available.

The approved symbol appears to the left of the wordmark. The wordmark is vertically aligned optically with the symbol rather than positioned solely by font metrics. The gap remains sufficient for the symbol and name to read as coordinated identity components rather than one fused drawing.

I do not place the wordmark inside the symbol or allow the text to overlap the symbol's clear area.

## Stacked lockup

The stacked lockup is intended for narrower or centered compositions. The approved symbol appears above the wordmark and remains visually dominant enough to preserve recognition.

The stacked arrangement changes only spacing and presentation scale. It does not change the symbol geometry or the `Goree` / `Cloud` hierarchy.

## Light presentation

On the approved light field or another validated light background:

- the platform symbol retains Primary Blue `#3B82F6` and Deep Blue `#174EA6`;
- `Goree` uses dark neutral `#111827`;
- `Cloud` uses Deep Blue `#174EA6`;
- the approved light field remains `#F7FAFF` where a field is included.

## Dark presentation

The canonical-candidate reversed presentation uses a dark field and high-contrast light/blue identity treatment. It exists for dark surfaces and accessibility/contrast needs; it does not replace the primary Deep Cloud presentation.

Dark/reversed treatment is a controlled derivative of the same identity geometry.

## Monochrome presentation

The canonical-candidate monochrome set renders the identity as a controlled single-color derivative for reproduction contexts where the full two-tone palette is unavailable.

Monochrome does not replace the normal Deep Cloud presentation where full color is supported.

## Deterministic build tooling

The repository includes a wordmark asset generator and pinned build requirements. The generator exists so official vector derivatives can be reproduced from a documented process instead of being manually redrawn.

Generated output must still be visually validated before promotion. Deterministic generation does not by itself constitute brand approval.

## Clear space

Lockups require clear space around the complete composition, not merely around the symbol. No text, border, icon, photograph edge, or interface ornament should visually crowd the identity.

The existing platform-symbol clear-space guidance remains the baseline. Final promoted lockups may add more specific measurable lockup guidance without reducing the symbol's protected space.

## Minimum size

The symbol-only identity remains preferred at sizes where the wordmark can no longer reproduce clearly. The generated lockups must be tested at intended production sizes before use in especially small UI contexts.

Favicons and very small launcher surfaces should normally use the approved symbol rather than the full wordmark lockup.

## Canonical promotion plan

The corrected production package establishes the vector artwork intended for the following official files:

- `official/goreecloud-wordmark.svg`;
- `official/goreecloud-lockup-horizontal.svg`;
- `official/goreecloud-lockup-stacked.svg`;
- corresponding reversed derivatives;
- corresponding monochrome derivatives.

The next identity action is to promote the generated outlined SVG outputs into those canonical repository paths and then update the brand status from **selected/canonical candidate** to **finalized production artwork**.

Until that promotion occurs, `official/goreecloud-logo.svg` remains the authoritative platform-symbol source and the corrected Deep Cloud package remains the validated production candidate for the wordmark system.

## Relationship to Glaze UI

Glaze UI may provide surrounding layout, surface, depth, animation, or interaction treatment. It must not distort, recolor arbitrarily, animate individual logo components independently, or apply decorative effects that change the canonical GoreeCloud identity.

## Governance

The Deep Cloud wordmark is a shared GoreeCloud identity asset. Individual applications or repositories must not recreate the text treatment independently.

Once the outlined lockups are promoted to `official/`, GoreeCloud surfaces should consume those approved shared assets or faithful generated raster derivatives from `GoreeCloud/goreecloud-branding-assets`.

Any future material change to the `Goree` / `Cloud` hierarchy, wordmark letterforms, approved colors, symbol relationship, or approved production geometry requires an explicit identity revision and corresponding documentation update.

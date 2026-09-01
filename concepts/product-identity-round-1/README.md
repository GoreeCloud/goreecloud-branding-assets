# Missing Product Identity Round 1

Status: **Approval candidates — not production artwork**

These four SVGs are first-round identity candidates for GoreeCloud products that currently lack canonical product artwork. They are intentionally stored under `concepts/` and MUST NOT be treated as approved assets, copied to production launchers, added to `catalog.json`, or represented as Stable visual conformance until the applicable visual acceptance and promotion work is complete.

Current production design baseline: **Glaze UI 2.1.0 Stable**. The geometry is intended to remain compatible with the Glaze UI 2.2 Candidate direction, but this concept round does not claim Glaze UI 2.2 Stable conformance.

## Shared construction

All four candidates follow the current GoreeCloud product-icon construction already used by canonical product artwork:

- 64 × 64 SVG artboard;
- 16-unit rounded application container;
- dominant single visual idea with secondary detail kept subordinate;
- white foreground geometry with approximately 3–3.5 unit primary strokes;
- bounded two-stop identity gradient;
- no text-dependent recognition;
- silhouette and internal geometry designed to remain distinguishable without color;
- temporary operational state is not encoded into the underlying product identity.

## GoreeCloud App Store

Candidate: `app-store.svg`

### Identity DNA

- **Core meaning:** authorized software/service catalog destination and acquisition surface.
- **Family relationship:** software discovery/distribution; related to Launcher and Search only at the ecosystem level, not through shared primary geometry.
- **Primary concept:** a contained catalog portal with three software/service entries and a downward acquisition path.
- **Silhouette / Identity Lock candidate:** one large rounded portal with a three-entry header and centered acquisition axis.
- **Negative space:** open central vertical path from catalog entries toward the receiving baseline.
- **Material personality:** clear, confident application destination rather than retail decoration.
- **Identity color family:** violet → blue.
- **Do not use:** shopping bag, Apple App Store-style tool/A construction, Google Play triangle, F-Droid robot, generic storefront awning, or a standalone four-tile launcher grid.
- **Semantic constraint:** the acquisition arrow expresses product purpose only; it does not assert that a package is authorized, verified, secure, installed, or successfully downloaded.

### Collision review

The three-entry portal is structurally different from GoreeCloud Launcher’s four equal independent tiles and from GoreeCloud Search’s magnifying-glass silhouette. The revised concept intentionally replaces the earlier physical-storefront direction because the product must read as software distribution before retail commerce.

## GoreeCloud File Manager

Candidate: `file-manager.svg`

### Identity DNA

- **Core meaning:** provider-spanning file browsing, organization, and control.
- **Family relationship:** system utility with cloud/data relationships; must remain distinct from GoreeCloud Drive.
- **Primary concept:** two file/provider panes connected by bidirectional management actions.
- **Silhouette / Identity Lock candidate:** paired tall rounded panes with a narrow directional bridge.
- **Negative space:** central corridor between provider panes.
- **Material personality:** precise, durable, operational.
- **Identity color family:** teal → indigo.
- **Do not use:** a generic folder as the primary symbol, GoreeCloud Drive’s folder silhouette, or cloud-only storage symbolism.
- **Semantic constraint:** bidirectional arrows communicate management/movement capability as an identity metaphor; they do not assert that a specific file operation, synchronization, backup, or transfer is currently available or successful.

### Collision review

The paired-pane silhouette remains distinct from GoreeCloud Drive’s single folder and from document/page identities even in grayscale.

## GoreeCloud Maps

Candidate: `maps.svg`

### Identity DNA

- **Core meaning:** map exploration, spatial context, route understanding, and navigation.
- **Family relationship:** spatial/navigation product; related to GoreeCloud Location without reusing Location’s positioning identity.
- **Primary concept:** a folded map carrying a route path.
- **Silhouette / Identity Lock candidate:** three-panel folded map with unequal outer edges.
- **Negative space:** alternating folds create the structural rhythm; route path crosses panels rather than terminating in a pin.
- **Material personality:** expressive but compact and legible.
- **Identity color family:** amber → rose.
- **Do not use:** location pin as the primary symbol, GoreeCloud Location’s teardrop silhouette, or a generic globe.
- **Semantic constraint:** warm identity colors are branding only and MUST NOT be reused as warning, danger, destructive, or error truth. Operational navigation or safety state must use Glaze UI semantic treatments separately.

### Collision review

The folded-map silhouette remains immediately different from GoreeCloud Location’s pin/ring geometry in grayscale and at compact sizes.

## GoreeCloud Index

Candidate: `index.svg`

### Identity DNA

- **Core meaning:** privacy-first structured indexing across authorized providers while preserving provenance and authority boundaries.
- **Family relationship:** intelligence/discovery infrastructure expressed as a launchable application; related to Search but not interchangeable with it.
- **Primary concept:** layered index records with structural tabs.
- **Silhouette / Identity Lock candidate:** three horizontally layered records with offset/tabbed right edges.
- **Negative space:** repeated horizontal channels distinguish indexed layers and provider structure.
- **Material personality:** structured, analytical, controlled.
- **Identity color family:** violet → indigo.
- **Do not use:** magnifying glass as the primary symbol, GoreeCloud Search’s search silhouette, Launcher grid, robot/brain/sparkle AI clichés, or a single document/page metaphor.
- **Semantic constraint:** layered records express organization/indexing only; they do not imply that a provider is authorized, available, complete, private, or successfully indexed without authoritative runtime evidence.

### Collision review

The stacked tabbed-record silhouette remains distinct from Search’s circular magnifier, Launcher’s four-tile matrix, and Documents’ single-page outline in grayscale.

## Preliminary optical and accessibility review

The candidates were rendered and reviewed at **16, 24, 32, 48, and 64 px**. The primary silhouettes remain identifiable at the smallest samples; fine secondary structure is expected to simplify optically if a micro variant becomes necessary. A grayscale pass confirms that the nearest-neighbor distinctions above do not depend on hue.

This is preliminary design evidence only. Promotion still requires the applicable human/evidence-backed acceptance for:

- ecosystem-wall comparison beyond the nearest neighbors documented here;
- light/dark and representative background presentation;
- color-vision and increased/high-contrast review;
- optical balance and safe-area review at supported platform sizes;
- adaptive/monochrome/platform derivative decisions;
- exact consumer-surface review in each application;
- final approval decision recorded before moving artwork into `products/` and pinning it in `catalog.json`.

## Promotion sequence

1. Review these candidates in the pull request and against the complete product ecosystem.
2. Refine any candidate that fails recognition, collision, accessibility, or semantic review.
3. Record the approval decision and final Identity DNA.
4. Promote the accepted SVG into `products/<id>/app-icon.svg`.
5. Fetch the resulting exact Git blob and add the product to `catalog.json`.
6. Add/update the product repository `BRANDING.md` and generate traceable platform derivatives.
7. Replace development placeholders on required product surfaces.
8. Update project specifications and canonical change logs with the accepted migration and evidence.

Related tracking: `GoreeCloud/goreecloud-branding-assets` issue #4.

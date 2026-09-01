# Missing Product Identity Round 1

Status: **Accepted source candidates — not yet canonical production artwork**

These four SVGs are the reviewed source candidates for GoreeCloud products that currently lack canonical product artwork. They are intentionally stored under `concepts/` until the canonical promotion sequence completes and MUST NOT be copied to production launchers, added to release surfaces as official artwork, or represented as Stable application conformance merely because the concept files exist.

Current production design baseline: **Glaze UI 2.1.0 Stable**. The geometry is intended to remain compatible with the Glaze UI 2.2 Candidate direction, but this work does not claim Glaze UI 2.2 Stable conformance.

`REVIEW-EVIDENCE.md` records the source-level ecosystem, small-size, grayscale, semantic, and graphical-contrast review that accepts the exact revised candidates for canonical promotion. Canonical promotion and consumer integration remain separate controlled steps.

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
- **Silhouette / Identity Lock:** one large rounded portal with a three-entry header and centered acquisition axis.
- **Negative space:** open central vertical path from catalog entries toward the receiving baseline.
- **Material personality:** clear, confident application destination rather than retail decoration.
- **Identity color family:** violet → blue.
- **Do not use:** shopping bag, Apple App Store-style tool/A construction, Google Play triangle, F-Droid robot, generic storefront awning, or a standalone four-tile launcher grid.
- **Semantic constraint:** the acquisition arrow expresses product purpose only; it does not assert that a package is authorized, verified, secure, installed, or successfully downloaded.

### Collision result

The three-entry portal is structurally different from GoreeCloud Launcher’s four equal independent tiles and from GoreeCloud Search’s magnifying-glass silhouette. The reviewed concept intentionally avoids the earlier physical-storefront direction because the product must read as software distribution before retail commerce.

## GoreeCloud File Manager

Candidate: `file-manager.svg`

### Identity DNA

- **Core meaning:** provider-spanning file browsing, organization, and control.
- **Family relationship:** system utility with cloud/data relationships; must remain distinct from GoreeCloud Drive.
- **Primary concept:** two file/provider panes connected by bidirectional management actions.
- **Silhouette / Identity Lock:** paired tall rounded panes with a narrow directional bridge.
- **Negative space:** central corridor between provider panes.
- **Material personality:** precise, durable, operational.
- **Identity color family:** teal → indigo.
- **Do not use:** a generic folder as the primary symbol, GoreeCloud Drive’s folder silhouette, or cloud-only storage symbolism.
- **Semantic constraint:** bidirectional arrows communicate management/movement capability as an identity metaphor; they do not assert that a specific file operation, synchronization, backup, or transfer is currently available or successful.

### Collision result

The paired-pane silhouette remains distinct from GoreeCloud Drive’s single folder, Documents’ page, Sync’s isolated opposing arrows, Manager’s horizontal rails, and Backup’s horizontally stacked storage records. The teal endpoint was darkened during accessibility review so white foreground geometry remains above the reviewed 3:1 stop-level contrast threshold.

## GoreeCloud Maps

Candidate: `maps.svg`

### Identity DNA

- **Core meaning:** map exploration, spatial context, route understanding, and navigation.
- **Family relationship:** spatial/navigation product; related to GoreeCloud Location without reusing Location’s positioning identity.
- **Primary concept:** a folded map carrying a route path.
- **Silhouette / Identity Lock:** three-panel folded map with unequal outer edges.
- **Negative space:** alternating folds create the structural rhythm; route path crosses panels rather than terminating in a pin.
- **Material personality:** expressive but compact and legible.
- **Identity color family:** amber → rose.
- **Do not use:** location pin as the primary symbol, GoreeCloud Location’s teardrop silhouette, or a generic globe.
- **Semantic constraint:** warm identity colors are branding only and MUST NOT be reused as warning, danger, destructive, or error truth. Operational navigation or safety state must use Glaze UI semantic treatments separately.

### Collision result

The folded-map silhouette remains immediately different from GoreeCloud Location’s pin/ring geometry in grayscale and at compact sizes. The warm gradient was darkened during accessibility review so the white route/fold geometry remains above the reviewed 3:1 stop-level contrast threshold.

## GoreeCloud Index

Candidate: `index.svg`

### Identity DNA

- **Core meaning:** privacy-first structured indexing across authorized providers while preserving provenance and authority boundaries.
- **Family relationship:** intelligence/discovery infrastructure expressed as a launchable application; related to Search but not interchangeable with it.
- **Primary concept:** layered index records with structural tabs.
- **Silhouette / Identity Lock:** three horizontally layered records with offset/tabbed right edges.
- **Negative space:** repeated horizontal channels distinguish indexed layers and provider structure.
- **Material personality:** structured, analytical, controlled.
- **Identity color family:** violet → indigo.
- **Do not use:** magnifying glass as the primary symbol, GoreeCloud Search’s search silhouette, Launcher grid, robot/brain/sparkle AI clichés, or a single document/page metaphor.
- **Semantic constraint:** layered records express organization/indexing only; they do not imply that a provider is authorized, available, complete, private, or successfully indexed without authoritative runtime evidence.

### Collision result

The stacked tabbed-record silhouette remains distinct from Search’s circular magnifier, Launcher’s four-tile matrix, Documents’ single-page outline, AI/Network node geometries, Manager’s slider rails, and Backup’s two-record/recovery composition.

## Review state

Completed source-level review includes:

- exact rendering at 16, 24, 32, 48, 64, and 128 px;
- grayscale recognition review;
- broader ecosystem-wall comparison beyond nearest neighbors;
- graphical foreground/background contrast correction and verification;
- semantic-state review confirming stable identity does not encode runtime truth;
- application-container/safe-area inspection;
- third-party/trademark collision review at the concept level.

`REVIEW-EVIDENCE.md` contains the exact findings and contrast values.

Remaining work is canonical promotion and consumer validation rather than concept discovery:

1. promote the accepted SVGs into `products/<id>/app-icon.svg`;
2. fetch the resulting exact Git blobs and add each product to `catalog.json`;
3. pass branding CI on the exact promotion head;
4. add/update each product repository `BRANDING.md` and generate traceable platform derivatives;
5. replace development placeholders on required product surfaces;
6. validate adaptive/monochrome/platform presentations and exact consumer contexts;
7. update project specifications and canonical change logs with the accepted migration and evidence;
8. keep application production/Stable acceptance separate from visual-identity acceptance.

Related tracking: `GoreeCloud/goreecloud-branding-assets` issue #4.

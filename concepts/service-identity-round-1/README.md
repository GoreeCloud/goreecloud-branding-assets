# Service Identity Round 1

Status: **Approval candidates — not production artwork**

This directory contains first-round service-identity candidates for two concrete visual-identity defects currently visible in the GoreeCloud App Store development service catalog:

- Identity Center currently reuses the full GoreeCloud Identity application icon.
- Mesh Center currently falls back to a generic cloud glyph.

The active Glaze UI Application and Service Icon Identity System requires service identities to derive from parent Identity DNA without copying the application icon directly. These candidates therefore explore a reduced service-class treatment rather than new unrelated product logos.

No file in this directory is canonical. The branding repository does not yet define an approved production `services/` namespace or machine-readable service registry. Issue #6 tracks that repository-system requirement. A candidate must not be copied into a consumer repository or represented as official until the service path/catalog model and visual acceptance gates are approved.

## Shared service-class direction

Both candidates use a **circular 48-unit identity field within the 64×64 artboard** rather than the full 64×64 rounded-square application container used by GoreeCloud product icons. This is a proposed service-class distinction for review, not an established production rule.

The direction intentionally provides:

- reduced visual complexity for dense service lists and administrative surfaces;
- clear separation from full launchable application identities;
- parent color/family inheritance without direct icon copying;
- stable identity geometry that does not encode running, healthy, trusted, connected, authorized, warning, failure, or other temporary state;
- compact-size readability with one dominant motif.

The circular field itself must be evaluated against the broader Glaze UI service construction system before any production convention is established.

## Identity Center

Candidate: `identity-center.svg`

Parent identity: `products/identity/app-icon.svg`

### Identity DNA derivation

- **Inherited DNA:** GoreeCloud Identity blue→violet relationship and a reduced human-identity fragment.
- **Service-specific concept:** identity subject plus a simple vertical control/relationship rail.
- **Primary silhouette:** circular service field rather than Identity's rounded-square application container.
- **Negative-space relationship:** open separation between the person fragment and the control rail.
- **Complexity reduction:** smaller head/shoulder fragment, no parent application's corner-arrow motif, no full application composition.
- **Semantic boundary:** control nodes are structural identity-management cues only. They do not mean authenticated, authorized, verified, trusted, active-session, protected, or compliant.

### Collision objective

A user should understand that Identity Center belongs to GoreeCloud Identity while still being able to distinguish the service from the launchable Identity application at a glance.

## Mesh Center

Candidate: `mesh-center.svg`

Parent identity: `systems/goreecloud-mesh/goreecloud-mesh-mark.svg`

### Identity DNA derivation

- **Inherited DNA:** Mesh cyan→blue→violet color relationship, crossing coordination routes, and endpoint nodes.
- **Service-specific concept:** a reduced two-route weave plus a central inspection/control ring.
- **Primary silhouette:** circular service field rather than the free-standing full Mesh system mark.
- **Complexity reduction:** removes the parent mark's vertical route rails and secondary inner paths; keeps only the essential distributed-route relationship.
- **Semantic boundary:** endpoint/routes/ring communicate Mesh administration and inspection only. They do not mean connected, synchronized, healthy, secure, reachable, authorized, or operational.

### Collision objective

Mesh Center should be visibly related to GoreeCloud Mesh while remaining simpler than the system-level mark and clearly different from a generic cloud/network-status glyph.

## Required review before promotion

- compare each candidate beside its parent identity and confirm related-but-not-identical recognition;
- compare against every current product/system identity and future service candidates for silhouette collision;
- review at representative dense-list sizes, including 16, 20, 24, 32, 48, and 64 px;
- review grayscale and applicable color-vision conditions so recognition does not depend on hue;
- review light, dark, increased-contrast, reduced-transparency/solid, and representative background contexts;
- validate that the proposed circular service-class field is compatible with Glaze UI rather than accidentally creating a new ungoverned icon class;
- define and validate the canonical service namespace/registry before production files are created;
- after approval, create exact canonical service assets, pin exact Git blobs, generate App Store Android derivatives, update service mappings, and remove the current full-app-icon/generic-glyph treatments.

Related tracking: issue #6.

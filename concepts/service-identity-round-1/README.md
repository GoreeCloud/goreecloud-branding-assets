# Service Identity Round 1

Status: **Accepted source candidates — not yet canonical production artwork**

This directory contains the first service-identity candidates for two concrete visual-identity defects visible in the GoreeCloud App Store development service catalog:

- Identity Center currently reuses the full GoreeCloud Identity application icon.
- Mesh Center currently falls back to a generic cloud glyph.

The active Glaze UI Application and Service Icon Identity System requires service identities to derive from parent Identity DNA without copying the application icon directly. These candidates therefore use reduced parent-derived service treatments rather than unrelated new product logos.

The canonical service namespace and machine-readable lifecycle model now exist at `services/` and `services/catalog.json`. Identity Center and Mesh Center are registered there as `artwork-pending`, so no file in this concept directory is canonical and neither service currently claims an approved production asset or Git blob.

`REVIEW-EVIDENCE.md` records the source-level visual, ecosystem, small-size, grayscale, parent-separation, semantic, and graphical-contrast review that accepts these exact revised candidates for canonical promotion. Consumer integration remains separate work.

## Shared service-class direction

Both candidates use a **circular 48-unit identity field within the 64×64 artboard** rather than the full 64×64 rounded-square application container used by GoreeCloud product icons.

The review accepted this treatment for Identity Center and Mesh Center because it provides:

- reduced visual complexity for dense service lists and administrative surfaces;
- immediate separation from full launchable application identities;
- parent color/family inheritance without direct icon copying;
- stable identity geometry that does not encode running, healthy, trusted, connected, authorized, warning, failure, or other temporary state;
- compact-size readability with one dominant motif.

This does not establish a requirement that every future GoreeCloud service use an identical circular field. Future service identities still require family and ecosystem collision review under the service identity standard.

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

### Collision result

The reviewed candidate remains recognizably related to GoreeCloud Identity while clearly distinguishable from the launchable Identity application at full and compact sizes.

## Mesh Center

Candidate: `mesh-center.svg`

Parent identity: `systems/goreecloud-mesh/goreecloud-mesh-mark.svg`

### Identity DNA derivation

- **Inherited DNA:** Mesh cyan→blue→violet relationship, crossing coordination routes, and endpoint nodes.
- **Service-specific concept:** a reduced two-route weave plus a central inspection/control ring.
- **Primary silhouette:** circular service field rather than the free-standing full Mesh system mark.
- **Complexity reduction:** removes the parent mark's vertical route rails and secondary inner paths; keeps only the essential distributed-route relationship.
- **Semantic boundary:** endpoint/routes/ring communicate Mesh administration and inspection only. They do not mean connected, synchronized, healthy, secure, reachable, authorized, or operational.

### Collision result

The reviewed candidate is visibly related to GoreeCloud Mesh while remaining simpler than the system-level mark and clearly different from the generic cloud/network-status fallback it will replace.

## Review state

Completed source-level review includes:

- exact parent comparison and related-but-not-identical recognition;
- broader product/system silhouette comparison;
- 16, 24, 32, 48, 64, and 128 px rendering review;
- grayscale recognition review;
- graphical foreground/background contrast correction and verification;
- stable-state semantic review;
- confirmation that the canonical service namespace/registry exists and keeps both records pending until promotion.

The remaining work is promotion and consumer validation rather than concept discovery:

1. create exact canonical service SVGs under `services/<service-id>/service-icon.svg`;
2. pin exact Git blobs and change the registry records to `approved`;
3. pass canonical branding and service-registry CI;
4. generate App Store Android derivatives;
5. replace the current full-app-icon/generic-glyph treatments;
6. validate the exact App Store Services surface and application package;
7. reconcile canonical project/change records.

Related tracking: issue #6.

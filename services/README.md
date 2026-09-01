# GoreeCloud Service Identities

This directory is the canonical identity namespace for GoreeCloud services and service-facing control surfaces.

Service identities are not independent mini-brands. Each service must declare an approved parent product or platform-system identity and derive a reduced, purpose-specific mark from that parent Identity DNA while remaining visually distinguishable from the full parent application/system artwork.

## Canonical path

Approved service artwork uses:

`services/<service-id>/service-icon.svg`

`services/catalog.json` is the authoritative machine-readable registry for this asset class.

A service directory or SVG must not be treated as official merely because it exists. Approval requires the service record to use `status: approved`, the exact canonical path above, and the exact Git blob of the accepted vector source.

## Lifecycle states

### `artwork-pending`

The service is known and governed, but no official service artwork has been approved. `canonical_asset` and `git_blob` must both remain `null`, and no canonical-looking `services/<service-id>/service-icon.svg` may exist.

Concepts may be developed under `concepts/`, but those files are review material only.

### `approved`

The service has passed the required visual, semantic, accessibility, optical-size, provenance, and ecosystem review gates. The registry must pin the exact approved SVG Git blob.

## Parent derivation

Every service record declares:

- `parent.class`: `product` or `system`;
- `parent.id`: the corresponding identity in the root branding catalog;
- one or more `consumer_surfaces` showing where the service identity is used.

The approved parent must already have canonical artwork. A service may inherit selected geometry, motif, color, material, or negative-space DNA, but it must not directly reuse the full parent icon path or bytes.

Examples of valid derivation include a reduced fragment of a product symbol, a simplified control-oriented composition, or a restrained subsystem motif. Merely copying the parent application icon and renaming it as a service is noncompliant.

## State separation

Operational state is not part of the stable identity. Connected, disconnected, healthy, degraded, synchronized, authorized, trusted, secure, protected, or similar runtime conditions must be communicated by separate Glaze UI state treatments and evidence-backed status semantics.

Displaying a service identity never establishes technical authority, authentication, authorization, privacy consent, security posture, continuity, health, connectivity, or release acceptance.

## Consumer derivatives

Consumer repositories may contain native/platform derivatives only when required for implementation. Those copies remain traceable derivatives of the approved canonical service source and must record the canonical path and exact Git blob in their branding contract.

The service registry is validated by `tools/validate_services.py` and is part of the branding CI gate.

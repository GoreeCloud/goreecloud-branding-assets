# GoreeCloud Branding Repository Migration

## Canonical repository

`GoreeCloud/goreecloud-branding-assets` is the canonical source for GoreeCloud logos, icons, artwork, wordmarks, product marks, platform-system identities, concepts, and approved production derivatives.

The former `GoreeCloud/goreecloud-logo` repository was fully migrated, retired, audited, and deleted on August 28, 2026.

## Completed consolidation

The GoreeCloud parent-platform identity and retained design history were migrated from `GoreeCloud/goreecloud-logo` into this repository. The approved platform vector remains at `official/goreecloud-logo.svg`.

The GoreeCloud Suite product icon set is centralized under `products/<product>/app-icon.svg`. Product repositories may retain synchronized local derivatives, but they are not branding authorities for assets represented here.

Approved platform-system artwork is centralized here:

- Privacy Shield: `systems/privacy-shield/privacy-shield-icon.svg`
- Wardveil Security: `systems/wardveil-security/wardveil-security-icon.svg`
- Everkeep: `systems/everkeep/everkeep.svg`
- Glaze UI: `systems/glaze-ui/glaze-ui-mark.svg`
- GoreeCloud Mesh: `systems/goreecloud-mesh/goreecloud-mesh-mark.svg` (Weave)

`catalog.json` is the machine-readable registry for the current platform, product, platform-system, and consumer branding authority.

## Consumer migration contract

Every GoreeCloud consumer must identify branding provenance from this repository. Local copies are permitted only as packaging, deployment, public-site generation, offline, performance, or platform-integration derivatives and must remain synchronized with an approved source path here.

For the GoreeCloud platform mark:

- repository: `GoreeCloud/goreecloud-branding-assets`
- canonical path: `official/goreecloud-logo.svg`
- migrated canonical commit: `9f434ac22fe2cf9121a4390df22ccb0ce1c648dc`
- reviewed Git blob: `082936062de7839148db89ea3ab4e86ff71341b0`

The GoreeCloud website platform-logo provenance records, public asset inventory, README, and stability baseline identify this repository as the branding authority. The public organization-profile repository vendors the approved platform logo for rendering while identifying this repository as the source of truth.

Privacy Shield, Wardveil Security, Everkeep, Glaze UI, and GoreeCloud Mesh consumer repositories identify repository-local artwork, where present, as synchronized derivatives of the unified system assets.

All 33 accessible Suite consumer repositories represented by the product catalog have a repository-local `BRANDING.md` contract pointing to their `products/<product>/app-icon.svg` authority here. GoreeCloud Vault artwork is centralized at `products/vault/app-icon.svg`; no accessible `GoreeCloud/goreecloud-vault` consumer repository exists in the connected GitHub scope.

## Final retirement audit

Before deletion, all 54 then-accessible GoreeCloud repositories, including the retired repository, were cloned and checked locally. The initial scan found only intentional migration/deprecation records, the local audit inventory, and four stale narrative references in the GoreeCloud website documentation.

The website references were corrected and pushed as commit `1c9bb74078d1e7b7deb9352150c704fd85c6d141`. A follow-up active-dependency scan across the remaining repositories returned zero references to `GoreeCloud/goreecloud-logo`, `github.com/GoreeCloud/goreecloud-logo`, or `raw.githubusercontent.com/GoreeCloud/goreecloud-logo` outside intentionally excluded migration-history material.

Immediately before deletion, the former repository was fetched with all branches/tags and preserved in a verified complete Git bundle. The retired repository `main`/`HEAD` was `1e4c1cc1bfaa0d1753fbe7563d78649e5c9e8d34`.

## Deletion completion

`GoreeCloud/goreecloud-logo` was deleted through an authorized GitHub CLI session with `delete_repo` scope on August 28, 2026. Post-deletion verification returned repository-not-found, and the connected GitHub repository inventory now contains 53 accessible GoreeCloud repositories.

The deletion gate is complete. No current or future GoreeCloud branding work may recreate the former repository as a competing branding authority. Historical references may remain only where they are explicitly documenting the completed migration or repository history.

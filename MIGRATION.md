# GoreeCloud Branding Repository Migration

## Canonical repository

`GoreeCloud/goreecloud-branding-assets` is the canonical source for GoreeCloud logos, icons, artwork, wordmarks, product marks, platform-system identities, concepts, and approved production derivatives.

The former `GoreeCloud/goreecloud-logo` repository is retired and must not receive new branding work.

## Completed consolidation

The GoreeCloud parent-platform identity and retained design history were migrated from `GoreeCloud/goreecloud-logo` into this repository. The approved platform vector remains at `official/goreecloud-logo.svg`.

The current GoreeCloud Suite product icon set is centralized under `products/<product>/app-icon.svg`. Product repositories may retain synchronized local derivatives, but they are no longer the branding authority for assets represented here.

The current approved platform-system artwork has also been centralized:

- Privacy Shield: `systems/privacy-shield/privacy-shield-icon.svg`
- Wardveil Security: `systems/wardveil-security/wardveil-security-icon.svg`
- Everkeep: `systems/everkeep/everkeep.svg`
- Glaze UI: `systems/glaze-ui/glaze-ui-mark.svg`
- GoreeCloud Mesh: no approved artwork yet; `systems/goreecloud-mesh/README.md` establishes the text-only pending state and future source-of-truth rule.

`catalog.json` is the machine-readable registry for the current platform, product, and platform-system branding authority.

## Consumer migration contract

Every GoreeCloud consumer must identify branding provenance from this repository. Local copies are permitted only as packaging, deployment, public-site generation, offline, performance, or platform-integration derivatives and must remain synchronized with an approved source path here.

For the GoreeCloud platform mark, use:

- repository: `GoreeCloud/goreecloud-branding-assets`
- canonical path: `official/goreecloud-logo.svg`
- migrated canonical commit: `9f434ac22fe2cf9121a4390df22ccb0ce1c648dc`
- reviewed Git blob: `082936062de7839148db89ea3ab4e86ff71341b0`

The GoreeCloud website platform-logo provenance records and public asset inventory have been migrated to this repository. The public organization-profile repository vendors the approved logo for rendering while identifying this repository as the branding authority. The website Suite portfolio likewise identifies centralized product artwork as its source authority.

Privacy Shield, Wardveil Security, Everkeep, and Glaze UI source repositories now identify their local approved artwork as synchronized derivatives of the unified system assets. GoreeCloud Mesh has a source-repository branding contract that keeps Mesh text-only until approved artwork is created here.

All 33 accessible Suite consumer repositories represented by the current product catalog have a repository-local `BRANDING.md` contract pointing to their `products/<product>/app-icon.svg` authority here. GoreeCloud Vault artwork is centralized at `products/vault/app-icon.svg`, but an accessible `GoreeCloud/goreecloud-vault` consumer repository is not present in the connected GitHub scope.

## Remaining retirement gate

Known active first-party branding provenance has been migrated from the former platform-logo repository. The remaining deletion gate is a definitive repository-wide residual-reference audit for `GoreeCloud/goreecloud-logo`.

GitHub code-search indexing is currently unavailable for the GoreeCloud repositories, so indexed organization-wide code search cannot yet prove that no residual reference remains. Until an authoritative full-repository scan is available, the retired repository should remain intact with its retirement notice rather than being destructively emptied.

## Deletion condition

Delete `GoreeCloud/goreecloud-logo` only after:

1. an authoritative repository-wide scan finds no active dependency on the retired repository;
2. the unified repository still contains the required canonical platform source and retained design history;
3. current public surfaces continue to render from synchronized local derivatives or another supported distribution path where the canonical repository is private; and
4. repository deletion is performed through an authorized GitHub control with deletion permission.

The connected GitHub action set available during this migration does not expose repository deletion, so deletion must be performed separately after the final audit gate is satisfied.

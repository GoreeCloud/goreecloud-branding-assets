# GoreeCloud Branding Repository Migration

## Canonical repository

`GoreeCloud/goreecloud-branding-assets` is the canonical source for GoreeCloud logos, icons, artwork, wordmarks, product marks, platform-system identities, and approved production derivatives.

The former `GoreeCloud/goreecloud-logo` repository is retired and must not receive new branding work.

## Consumer migration contract

Every GoreeCloud consumer must identify branding provenance from this repository. Product-local copies are permitted only as packaging, deployment, offline, or performance derivatives and must remain synchronized with an approved source path here.

For the GoreeCloud platform mark, use:

- repository: `GoreeCloud/goreecloud-branding-assets`
- canonical path: `official/goreecloud-logo.svg`
- migrated canonical commit: `9f434ac22fe2cf9121a4390df22ccb0ce1c648dc`
- reviewed Git blob: `082936062de7839148db89ea3ab4e86ff71341b0`

## Current retirement gates

The old repository must not be deleted until current consumers no longer depend on its repository URL. Known migration work includes the GoreeCloud website provenance records in `docs/visual-identity-sources.json` and `docs/public-asset-inventory.md`, which still record `GoreeCloud/goreecloud-logo` as the source authority for the platform mark.

The public organization-profile repository has already been migrated: it now vendors the approved logo for public rendering and records `GoreeCloud/goreecloud-branding-assets` as the canonical branding source.

GitHub code-search indexing is currently unavailable for the GoreeCloud repositories, so the final deletion gate also requires a complete reference audit once repository indexing is available or by another authoritative repository-wide scan.

## Deletion condition

Delete `GoreeCloud/goreecloud-logo` only after:

1. all known current consumer references have been migrated;
2. a repository-wide reference audit finds no active dependency on the retired repository;
3. the unified repository contains the required canonical source and retained design history;
4. current public surfaces continue to render from synchronized local derivatives or another supported distribution path where the canonical repository is private.

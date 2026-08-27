# GoreeCloud Branding Assets

Authoritative source-control repository for GoreeCloud branding assets, including logos, icons, artwork, wordmarks, platform marks, product marks, system identities, and approved production derivatives.

## Repository policy

- This repository is the canonical source for all current and future GoreeCloud branding assets.
- GoreeCloud applications, websites, documentation, repositories, and services must reference approved assets from this repository rather than creating independent copies as sources of truth.
- Existing product-local copies may be retained only when required for packaging, deployment, offline use, or performance; they must be generated or synchronized from an approved source here.
- New logos, icons, artwork, and branding-system assets belong here first.
- Experimental concepts must remain clearly separated from approved production assets.

## Current platform identity

**Official platform symbol:** Unified Clean — Blue  
**Canonical vector source:** `official/goreecloud-logo.svg`  
**Design language:** Glaze UI  
**Platform:** GoreeCloud

The canonical SVG is the source of truth for the GoreeCloud platform mark. Raster icons, favicons, launcher artwork, social avatars, and other production derivatives must be generated from approved vector sources rather than independently redrawn.

## Repository structure

- `official/` — approved GoreeCloud platform identity artwork and derivatives.
- `concepts/` — exploratory platform-identity artwork retained for design history; not approved for production use.
- `BRAND.md` — platform identity meaning, usage, geometry, color, and brand rules.
- `WORDMARK.md` — GoreeCloud wordmark specification and construction guidance.
- `PRODUCTION-ASSETS.md` — production export matrix and regeneration requirements.
- `tools/` — asset-generation and validation tooling.

As the unified library grows, product, system, campaign, and experience-specific assets should be organized into clearly named directories without creating separate branding repositories.

## Integration contract

Consumers should reference this repository as `GoreeCloud/goreecloud-branding-assets`. References to the retired `GoreeCloud/goreecloud-logo` repository are deprecated and must be migrated.

When an asset must be vendored into another repository, record its source path here and keep the vendored copy synchronized with the approved source.

## Governance

Approved production assets must be evidence-backed and must not imply capabilities that are not implemented. GoreeCloud platform-system identities such as Privacy Shield, Wardveil Security, Everkeep, Glaze UI, and GoreeCloud Mesh remain substantive system identities; their artwork belongs in this unified repository when created or revised.

See `BRAND.md`, `WORDMARK.md`, and `PRODUCTION-ASSETS.md` before integrating, modifying, or exporting the platform identity.

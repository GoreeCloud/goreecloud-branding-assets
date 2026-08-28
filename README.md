# GoreeCloud Branding Assets

Authoritative source-control repository for GoreeCloud branding assets, including logos, icons, artwork, wordmarks, platform marks, product marks, system identities, concepts, and approved production derivatives.

## Repository policy

- This repository is the canonical source for all current and future GoreeCloud branding assets.
- GoreeCloud applications, websites, documentation, repositories, and services must identify approved assets from this repository as their branding source of truth.
- Product- or system-local copies may exist only when required for packaging, deployment, public-site generation, offline use, performance, or platform integration; they are synchronized derivatives rather than independent authorities.
- New logos, icons, artwork, wordmarks, identity concepts, and branding-system assets belong here first.
- Experimental concepts must remain clearly separated from approved production assets.
- Branding never creates technical authority or evidence for privacy, security, continuity, design conformance, coordination, or application capability claims.

## Current platform identity

**Official platform symbol:** Unified Clean — Blue  
**Canonical vector source:** `official/goreecloud-logo.svg`  
**Design language:** Glaze UI  
**Platform:** GoreeCloud

The canonical SVG is the source of truth for the GoreeCloud platform mark. Raster icons, favicons, launcher artwork, social avatars, and other production derivatives must be generated from approved vector sources rather than independently redrawn.

## Repository structure

- `official/` — approved GoreeCloud parent-platform identity artwork and derivatives.
- `products/` — canonical GoreeCloud application and product identity artwork.
- `systems/` — canonical platform-system branding for Privacy Shield, Wardveil Security, Everkeep, Glaze UI, and GoreeCloud Mesh.
- `concepts/` — exploratory parent-platform identity artwork retained for design history; not approved for production use.
- `BRAND.md` — platform identity meaning, usage, geometry, color, and brand rules.
- `WORDMARK.md` — GoreeCloud wordmark specification and construction guidance.
- `PRODUCTION-ASSETS.md` — production export matrix and regeneration requirements.
- `MIGRATION.md` — repository-consolidation and retirement status.
- `tools/` — asset-generation and validation tooling.

Product, system, campaign, and experience-specific assets should be organized inside this repository rather than split into separate branding repositories.

## Platform-system identities

The following are substantive GoreeCloud platform systems, not decorative labels:

- **Privacy Shield → Privacy Center** — platform-wide privacy identity and privacy-control authority.
- **Wardveil Security → Security Center** — platform-wide security and protection identity.
- **Everkeep → Continuity Center** — resilience, backup/recovery, preservation, portability, succession, and digital-legacy identity.
- **Glaze UI → Design Center** — GoreeCloud visual, interaction, adaptation, and interface-design system.
- **GoreeCloud Mesh → Mesh Center** — application/service coordination and governance plane.

Approved system artwork is indexed in `systems/README.md`. GoreeCloud Mesh currently has no approved canonical artwork and must use text-only identity presentation until an approved source is created here.

## Integration contract

Consumers must reference this repository as `GoreeCloud/goreecloud-branding-assets` for branding provenance. References to the retired `GoreeCloud/goreecloud-logo` repository are deprecated and must not be introduced.

When an asset is vendored into another repository, its documentation or machine-readable identity contract should record the canonical path here. Vendored bytes must stay synchronized with the approved source.

## Governance

Approved production assets must be source-traceable and evidence-backed. Public artwork and language must not imply capabilities that are not implemented or accepted for the represented scope.

See `BRAND.md`, `WORDMARK.md`, `PRODUCTION-ASSETS.md`, `products/README.md`, and `systems/README.md` before integrating, modifying, or exporting GoreeCloud identity artwork.

# GoreeCloud Production Logo Assets

## Purpose

I use the approved **Unified Clean — Blue** artwork as the sole source for production GoreeCloud platform-logo derivatives. The canonical vector source remains `official/goreecloud-logo.svg`; raster and platform packages are generated artifacts rather than independent masters.

## Production export matrix

### General PNG

I maintain square PNG exports at 16, 32, 48, 64, 128, 256, 512, 1024, and 2048 pixels as needed for interfaces, documentation, integrations, and distribution.

### Web

I maintain favicon-compatible 16, 32, and 48 pixel artwork, plus 180, 192, and 512 pixel web/application icons. A multi-size `favicon.ico` may contain the 16, 32, and 48 pixel renderings.

### Social and repository identity

I use a 1024 × 1024 canonical raster rendering for GitHub and social-avatar source artwork. Individual platforms may downsample this source. I do not redesign the mark for a specific social network.

### Android

Launcher-source raster sizes are maintained for mdpi (48), hdpi (72), xhdpi (96), xxhdpi (144), and xxxhdpi (192). Application projects may derive adaptive-icon packaging from the approved mark, but may not alter the mark geometry.

### Apple platforms

I maintain source raster sizes including 120, 152, 167, 180, and 1024 pixels for appropriate application-icon workflows. Platform-specific packaging must follow current platform requirements while preserving the approved GoreeCloud artwork.

## Generation rule

All raster assets must be regenerated from the approved SVG when the canonical artwork changes. I do not manually edit exported PNG files and then treat those edits as official artwork.

## Validation

Before release, I visually inspect small exports to confirm that the central opening, outer boundary, and outward connection remain distinct. I also verify square dimensions, alpha/background expectations, file integrity, and that no export has been stretched or cropped.

## Repository policy

`GoreeCloud/goreecloud-branding-assets` is the authoritative Git home for approved branding vector sources and identity documentation. Binary production packages may be distributed as release artifacts or checked in where operationally useful, but they remain derivatives of canonical sources stored here.

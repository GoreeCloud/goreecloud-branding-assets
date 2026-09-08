# GoreeCloud Mobile Wallpaper System

Status: Design and implementation requirement
Target: GoreeCloud Android / GoreeCloud OS Mobile
Design system: Glaze UI

## Purpose

GoreeCloud devices must ship with an original GoreeCloud-themed wallpaper collection rather than relying on LineageOS-branded/default wallpaper artwork.

The wallpaper system must express GoreeCloud through material, depth, atmosphere, connected-system motifs, and restrained accent color. It must not be a generic stock-wallpaper collection and must not simply place a large GoreeCloud logo or wordmark over a gradient.

## Visual language

The wallpaper family follows Glaze UI principles:

- neutral glass is the primary material;
- color is a restrained accent rather than the entire surface;
- layered translucency, soft refraction, subtle depth, and controlled highlights are preferred;
- compositions must preserve strong icon and widget legibility;
- artwork must remain calm enough for prolonged daily use;
- light and dark families must feel related rather than like unrelated collections;
- no LineageOS branding, imagery, derivative artwork, or visual references may appear.

## Required first-party collection

1. **Living Glaze** — signature default. Layered translucent neutral glass with a restrained teal/cyan GoreeCloud light source and deep spatial falloff.
2. **Pearl** — bright frosted pearl and clear-neutral glass for light environments.
3. **Graphite** — smoke/graphite glass, subdued highlights, and restrained cool GoreeCloud accents.
4. **Mesh** — connected translucent nodes/paths representing GoreeCloud Mesh without literal network-diagram styling.
5. **Aurora** — atmospheric GoreeCloud light interacting with neutral glass layers.
6. **Depth** — dimensional glass planes and refraction emphasizing Glaze UI material hierarchy.
7. **Minimal Light** — low-detail light composition optimized for icon/widget readability.
8. **Minimal Dark** — low-detail dark composition optimized for OLED/low-light use and icon/widget readability.

## Device-safe composition

Master artwork must be produced at a resolution large enough for modern phone crops. Phone derivatives must preserve the central safe region when cropped for portrait displays such as the OnePlus Nord N200. Important visual structure must not depend on extreme left/right edges.

Do not bake UI text, status-bar graphics, clocks, navigation bars, or app icons into wallpaper artwork.

## Default assignments

- Default Home wallpaper: **Living Glaze**.
- Default Lock wallpaper: **Graphite** or a lock-specific Living Glaze derivative with reduced detail behind clock/notifications.

The final Android packaging layer may provide separate home/lock derivatives while retaining one common master-artwork family.

## Repository authority

`GoreeCloud/goreecloud-branding-assets` is the authoritative home for master wallpaper assets and approved derivatives. Android recovery packages and application repositories consume these assets; they do not become independent sources of truth.

## Android integration requirements

- Preserve the Android wallpaper framework and picker services.
- Replace LineageOS-branded/default content where technically safe rather than deleting core wallpaper services.
- Make GoreeCloud wallpapers available as first-party system wallpaper choices.
- Make the designated GoreeCloud defaults applicable during GoreeCloud OS provisioning or recovery-pack installation where Android permits it safely.
- Preserve the wallpaper payload across compatible OTA updates when shipped through the GoreeCloud recovery add-on.

## Acceptance

Artwork is not accepted merely because it renders. It must be reviewed on a physical Android device for icon readability, widget readability, status-bar contrast, crop behavior, light/dark behavior, and visual consistency with current Glaze UI.

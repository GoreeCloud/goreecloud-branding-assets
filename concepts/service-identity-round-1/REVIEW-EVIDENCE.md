# Service Identity Round 1 — Review Evidence

Status: **Source-level visual acceptance evidence for promotion review**

This record reviews the Identity Center and Mesh Center service candidates against their exact parent identities and the current GoreeCloud product ecosystem. It does not itself promote the SVGs into `services/` or change the canonical service registry from `artwork-pending` to `approved`.

## Review basis

The candidates were rendered from exact SVG source at 16, 24, 32, 48, 64, and 128 px. Color, grayscale, small-size recognition, parent relationship, silhouette separation, and stable-state semantics were inspected.

Parent comparison used:

- `products/identity/app-icon.svg` for Identity Center;
- `systems/goreecloud-mesh/goreecloud-mesh-mark.svg` for Mesh Center.

The broader collision pass also considered current product geometry including Launcher, Search, Drive, Documents, Location, Backup, Sync, Manager, Network, and AI.

## Service-class field

Both candidates use a circular 48-unit service field within the 64×64 artboard. The circle is accepted for these two service identities as a reduced service-class treatment because:

- it creates immediate separation from the rounded-square launchable application container;
- it remains a stable identity field rather than an operational-state badge;
- the parent-derived internal motif remains the primary recognition cue;
- it is legible in dense App Store service cards and compact list sizes;
- it does not copy the full parent application/system composition.

This acceptance applies to these service identities and does not require every future GoreeCloud service to use an identical circle. Future services still require family/ecosystem collision review under the service identity standard.

## Graphical contrast correction

The first candidates used bright blue/cyan endpoints where white foreground geometry fell below a 3:1 foreground/background contrast threshold. The source was corrected before this review:

- Identity Center start color: `#3B82F6` instead of `#60A5FA`.
- Mesh Center start color: `#0891B2` instead of `#22D3EE`.
- Mesh Center middle color: `#2563EB` instead of `#3B82F6`.
- Mesh Center end color: `#7C3AED` instead of `#8B5CF6`.

Final white-foreground contrast against service gradient stops is:

| Candidate | Gradient stop | White contrast |
| --- | --- | ---: |
| Identity Center | `#3B82F6` | 3.68:1 |
| Identity Center | `#7C3AED` | 5.70:1 |
| Mesh Center | `#0891B2` | 3.68:1 |
| Mesh Center | `#2563EB` | 5.17:1 |
| Mesh Center | `#7C3AED` | 5.70:1 |

Consumer-specific high-contrast/monochrome behavior remains a separate integration check.

## Identity Center — PASS for canonical promotion

The candidate clearly inherits GoreeCloud Identity through the blue→violet relationship and reduced person motif, but it no longer copies the application icon. The circular service field, smaller subject geometry, missing corner-arrow motif, and separate vertical control rail create a visibly different lock.

At compact sizes the person fragment remains dominant and the rail reads as a secondary management/control cue. Recognition remains possible in grayscale. The nodes do not imply authenticated, authorized, trusted, verified, or active state.

## Mesh Center — PASS for canonical promotion

The candidate inherits GoreeCloud Mesh through crossing coordination routes, endpoint nodes, and the cyan/blue/violet family. It removes the full system mark’s vertical rails and secondary internal route structure and adds a central inspection/control ring.

The result is visibly related to Mesh while substantially simpler than the system mark and distinct from the generic cloud placeholder currently used by App Store. At compact sizes the crossing-route lock remains recognizable. The route/node/ring composition does not encode connected, healthy, synchronized, secure, reachable, or authorized state.

## Acceptance conclusion

The exact revised service candidates pass this source-level visual review for **canonical promotion** under the service identity governance now established in `services/README.md` and `services/catalog.json`.

Promotion must still be executed through source control:

1. create `services/identity-center/service-icon.svg` and `services/mesh-center/service-icon.svg` from the accepted source;
2. pin the exact SVG Git blobs in `services/catalog.json` and move both records from `artwork-pending` to `approved`;
3. pass `tools/validate_catalog.py` and `tools/validate_services.py` on the exact promotion head;
4. generate traceable App Store Android derivatives;
5. replace Identity Center’s full application-icon reuse and Mesh Center’s generic cloud fallback;
6. add App Store fail-closed mapping validation;
7. review the exact App Store Services surface and package evidence;
8. reconcile App Store and applicable Identity/Mesh change records without implying runtime authority.

Related tracking: issue #6.

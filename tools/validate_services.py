#!/usr/bin/env python3
from __future__ import annotations

from hashlib import sha1
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SERVICE_CATALOG = ROOT / "services" / "catalog.json"
ROOT_CATALOG = ROOT / "catalog.json"
EXPECTED_REPOSITORY = "GoreeCloud/goreecloud-branding-assets"
EXPECTED_PATH_PATTERN = "services/<service-id>/service-icon.svg"
GIT_BLOB = re.compile(r"^[0-9a-f]{40}$")
VALID_PARENT_CLASSES = {"product", "system"}
VALID_STATUSES = {"artwork-pending", "approved"}


def fail(message: str) -> None:
    raise ValueError(message)


def git_blob_id(raw: bytes) -> str:
    return sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()


def require_pinned_file(relative: str, expected_blob: str, label: str) -> None:
    path = ROOT / relative
    if not path.is_file() or path.is_symlink():
        fail(f"{label} is not a regular canonical file: {relative}")
    if not GIT_BLOB.fullmatch(expected_blob):
        fail(f"{label} has invalid pinned Git blob: {expected_blob!r}")
    actual = git_blob_id(path.read_bytes())
    if actual != expected_blob:
        fail(
            f"{label} changed without registry approval: "
            f"{relative}; expected {expected_blob}, got {actual}"
        )


def load_json(path: Path, label: str) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{label} must contain a JSON object")
    return data


def parent_index(root_catalog: dict) -> dict[tuple[str, str], dict]:
    index: dict[tuple[str, str], dict] = {}
    for parent_class, collection in (
        ("product", root_catalog.get("products", [])),
        ("system", root_catalog.get("systems", [])),
    ):
        if not isinstance(collection, list):
            fail(f"root catalog {parent_class} collection must be a list")
        for item in collection:
            if not isinstance(item, dict):
                fail(f"root catalog {parent_class} record must be an object")
            item_id = item.get("id")
            if not isinstance(item_id, str) or not item_id:
                fail(f"root catalog {parent_class} record lacks an id")
            key = (parent_class, item_id)
            if key in index:
                fail(f"duplicate root catalog parent identity: {parent_class}:{item_id}")
            index[key] = item
    return index


def main() -> int:
    try:
        root_catalog = load_json(ROOT_CATALOG, "root branding catalog")
        service_catalog = load_json(SERVICE_CATALOG, "service identity catalog")

        if service_catalog.get("schema_version") != 1:
            fail("service catalog schema_version must be 1")
        if service_catalog.get("canonical_repository") != EXPECTED_REPOSITORY:
            fail("service catalog canonical_repository drifted")
        if service_catalog.get("asset_class") != "service":
            fail("service catalog asset_class must be 'service'")
        if service_catalog.get("canonical_path_pattern") != EXPECTED_PATH_PATTERN:
            fail("service catalog canonical_path_pattern drifted")

        policy = service_catalog.get("policy") or {}
        for key in (
            "parent_derived_identity_required",
            "direct_parent_icon_reuse_forbidden",
            "operational_state_must_remain_separate",
            "pending_services_must_not_claim_artwork",
            "consumer_copies_are_derivatives",
        ):
            if policy.get(key) is not True:
                fail(f"service catalog policy must keep {key}=true")
        if policy.get("branding_creates_technical_authority") is not False:
            fail("service branding must never create technical authority")

        parents = parent_index(root_catalog)
        service_ids: set[str] = set()
        approved_paths: set[str] = set()
        consumer_keys: set[tuple[str, str, str]] = set()

        services = service_catalog.get("services")
        if not isinstance(services, list) or not services:
            fail("service catalog must contain at least one service record")

        for service in services:
            if not isinstance(service, dict):
                fail("service records must be objects")

            service_id = service.get("id")
            if (
                not isinstance(service_id, str)
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", service_id)
                or service_id in service_ids
            ):
                fail(f"duplicate or invalid service id: {service_id!r}")
            service_ids.add(service_id)

            name = service.get("name")
            if not isinstance(name, str) or not name.strip():
                fail(f"service {service_id} lacks a name")

            parent = service.get("parent")
            if not isinstance(parent, dict):
                fail(f"service {service_id} lacks a parent identity")
            parent_class = parent.get("class")
            parent_id = parent.get("id")
            if parent_class not in VALID_PARENT_CLASSES:
                fail(f"service {service_id} has invalid parent class: {parent_class!r}")
            if not isinstance(parent_id, str) or not parent_id:
                fail(f"service {service_id} has invalid parent id")
            parent_record = parents.get((parent_class, parent_id))
            if parent_record is None:
                fail(
                    f"service {service_id} references unknown parent "
                    f"{parent_class}:{parent_id}"
                )

            parent_asset = parent_record.get("canonical_asset")
            parent_blob = parent_record.get("git_blob")
            if not isinstance(parent_asset, str) or not isinstance(parent_blob, str):
                fail(
                    f"service {service_id} parent {parent_class}:{parent_id} "
                    "does not have approved canonical artwork"
                )
            require_pinned_file(
                parent_asset,
                parent_blob,
                f"parent identity for service {service_id}",
            )

            status = service.get("status")
            if status not in VALID_STATUSES:
                fail(f"service {service_id} has unsupported status: {status!r}")

            expected_asset = f"services/{service_id}/service-icon.svg"
            asset = service.get("canonical_asset")
            blob = service.get("git_blob")

            if status == "artwork-pending":
                if asset is not None or blob is not None:
                    fail(
                        f"pending service {service_id} must not claim "
                        "canonical artwork or Git blob"
                    )
                if (ROOT / expected_asset).exists():
                    fail(
                        f"pending service {service_id} has a canonical-looking asset "
                        f"without approval: {expected_asset}"
                    )
            else:
                if asset != expected_asset:
                    fail(
                        f"approved service canonical path drift for {service_id}: "
                        f"expected {expected_asset!r}, got {asset!r}"
                    )
                if asset == parent_asset:
                    fail(f"service {service_id} directly reuses its parent asset path")
                if blob == parent_blob:
                    fail(f"service {service_id} directly reuses its parent asset blob")
                if asset in approved_paths:
                    fail(f"duplicate approved service canonical asset: {asset}")
                approved_paths.add(asset)
                require_pinned_file(asset, str(blob or ""), f"service {service_id}")

            surfaces = service.get("consumer_surfaces")
            if not isinstance(surfaces, list) or not surfaces:
                fail(f"service {service_id} must declare at least one consumer surface")
            for surface in surfaces:
                if not isinstance(surface, dict):
                    fail(f"service {service_id} consumer surface must be an object")
                repo = surface.get("repository")
                surface_name = surface.get("surface")
                item_id = surface.get("item_id")
                if not isinstance(repo, str) or not repo.startswith("GoreeCloud/"):
                    fail(f"service {service_id} has invalid consumer repository: {repo!r}")
                if not isinstance(surface_name, str) or not surface_name.strip():
                    fail(f"service {service_id} has invalid consumer surface")
                if not isinstance(item_id, str) or not item_id.strip():
                    fail(f"service {service_id} has invalid consumer item_id")
                key = (repo, surface_name, item_id)
                if key in consumer_keys:
                    fail(f"duplicate service consumer surface mapping: {key}")
                consumer_keys.add(key)

        discovered = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "services").glob("*/service-icon.svg")
            if path.is_file() and not path.is_symlink()
        }
        if discovered != approved_paths:
            extra = sorted(discovered - approved_paths)
            missing = sorted(approved_paths - discovered)
            fail(
                "service canonical asset registry drift: "
                f"unregistered={extra}, missing={missing}"
            )

    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Service identity validation failed: {exc}", file=sys.stderr)
        return 1

    approved_count = sum(
        1 for service in services if service.get("status") == "approved"
    )
    pending_count = len(services) - approved_count
    print(
        f"Service identity validation passed: {len(services)} services, "
        f"{approved_count} approved, {pending_count} artwork-pending; "
        "parent identities and consumer surfaces are valid."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

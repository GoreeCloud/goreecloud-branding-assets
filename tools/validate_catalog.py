#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
EXPECTED_REPOSITORY = "GoreeCloud/goreecloud-branding-assets"


def fail(message: str) -> None:
    raise ValueError(message)


def require_file(relative: str, label: str) -> None:
    path = ROOT / relative
    if not path.is_file() or path.is_symlink():
        fail(f"{label} is not a regular canonical file: {relative}")


def main() -> int:
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))

        if data.get("schema_version") != 1:
            fail("catalog schema_version must be 1")
        if data.get("canonical_repository") != EXPECTED_REPOSITORY:
            fail("catalog canonical_repository drifted")

        policy = data.get("policy") or {}
        for key in (
            "canonical_first",
            "consumer_copies_are_derivatives",
            "new_branding_must_originate_here",
        ):
            if policy.get(key) is not True:
                fail(f"catalog policy must keep {key}=true")
        if policy.get("branding_creates_technical_authority") is not False:
            fail("branding must never create technical authority")

        platform = data.get("platform") or {}
        if platform.get("status") != "approved":
            fail("platform branding status must remain approved")
        require_file(str(platform.get("canonical_asset", "")), "platform asset")

        system_ids: set[str] = set()
        system_paths: set[str] = set()
        for system in data.get("systems", []):
            system_id = system.get("id")
            if not system_id or system_id in system_ids:
                fail(f"duplicate or missing system id: {system_id!r}")
            system_ids.add(system_id)

            status = system.get("status")
            asset = system.get("canonical_asset")
            if status == "approved":
                if not asset:
                    fail(f"approved system lacks canonical asset: {system_id}")
                if asset in system_paths:
                    fail(f"duplicate system canonical asset: {asset}")
                system_paths.add(asset)
                require_file(asset, f"system {system_id}")
            elif status == "text-only-pending-approved-artwork":
                if asset is not None:
                    fail(f"pending text-only system must not claim artwork: {system_id}")
            else:
                fail(f"unsupported system branding status for {system_id}: {status!r}")

            repo = system.get("consumer_repository")
            if repo is not None and not str(repo).startswith("GoreeCloud/"):
                fail(f"invalid system consumer repository: {repo!r}")

        product_ids: set[str] = set()
        product_paths: set[str] = set()
        for product in data.get("products", []):
            product_id = product.get("id")
            if not product_id or product_id in product_ids:
                fail(f"duplicate or missing product id: {product_id!r}")
            product_ids.add(product_id)

            asset = product.get("canonical_asset")
            expected = f"products/{product_id}/app-icon.svg"
            if asset != expected:
                fail(f"product canonical path drift for {product_id}: expected {expected!r}, got {asset!r}")
            if asset in product_paths:
                fail(f"duplicate product canonical asset: {asset}")
            product_paths.add(asset)
            require_file(asset, f"product {product_id}")

            repo = product.get("consumer_repository")
            if repo is not None and not str(repo).startswith("GoreeCloud/"):
                fail(f"invalid product consumer repository: {repo!r}")

        if not product_ids:
            fail("catalog contains no product branding records")
        if not system_ids:
            fail("catalog contains no platform-system branding records")

    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Branding catalog validation failed: {exc}", file=sys.stderr)
        return 1

    print(
        f"Branding catalog validation passed: {len(product_ids)} products, "
        f"{len(system_ids)} platform systems, canonical platform artwork present."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

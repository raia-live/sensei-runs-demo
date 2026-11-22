from shipkit import sync


def test_manifest_matches_the_region_modules():
    out = sync.stale()
    assert not out, f"shipkit/manifest.json is out of date for: {', '.join(out)}. See CONTRIBUTING.md."

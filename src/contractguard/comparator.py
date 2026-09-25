def compare_contracts(old: dict, new: dict):
    changes = []

    old_paths = old.get("paths", {})
    new_paths = new.get("paths", {})

    # --------------------------------
    # Check removed endpoints / methods
    # --------------------------------

    for path, old_methods in old_paths.items():
        print("Path ",old_paths)
        # Entire endpoint was removed
        if path not in new_paths:
            changes.append({
                "type": "removed_endpoint",
                "path": path,
                "severity": "breaking",
            })

            continue

        # Check if individual HTTP methods were removed
        for method in old_methods:

            if method not in new_paths[path]:
                changes.append({
                    "type": "removed_endpoint",
                    "path": path,
                    "method": method.upper(),
                    "severity": "breaking",
                })

    # --------------------------------
    # Check added endpoints / methods
    # --------------------------------

    for path, new_methods in new_paths.items():

        # Entire endpoint was added
        if path not in old_paths:
            changes.append({
                "type": "added_endpoint",
                "path": path,
                "severity": "safe",
            })

            continue

        # Check if individual HTTP methods were added
        for method in new_methods:

            if method not in old_paths[path]:
                changes.append({
                    "type": "added_endpoint",
                    "path": path,
                    "method": method.upper(),
                    "severity": "safe",
                })

    return changes
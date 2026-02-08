
"""
Simulates a crisis response system for archive access.
Demonstrates safe file handling using the `with` statement
and robust exception handling for different failure scenarios.
"""


def access_files(filename: str) -> None:
    try:
        with open(filename, "r+") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            content = file.read()
            print(f"SUCCESS: Archive recovered- ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Unexpected system anomaly detected")


if __name__ == "__main__":
    """Run crisis response scenarios."""
    print("=== CYBER ARCHIVES- CRISIS RESPONSE SYSTEM ===")
    print()
    access_files('lost_archive.txt')
    print()
    access_files('classified_vault.txt')
    print()
    access_files('standard_archive.txt')
    print()
    print("All crisis scenarios handled successfully. Archives secure.")

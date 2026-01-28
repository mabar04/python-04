if __name__ == "__main__":
    try:
        if routine:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")

        # safe file access
        with open(filename, "r") as f:
            content = f.read()
            print(content)

        # success handling
        if routine:
            print("SUCCESS: Archive recovered - ``Knowledge preserved for humanity''")
            print("STATUS: Normal operations resumed")
        else:
            print("SUCCESS: Crisis archive recovered")
            print("STATUS: Crisis resolved, data preserved")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, diagnostics recommended")


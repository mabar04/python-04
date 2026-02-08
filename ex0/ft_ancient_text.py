"""
Reads the file ancient_fragment.txt and displays its content
as part of a simulated data recovery process.
Handles missing file errors gracefully.
"""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES- DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")

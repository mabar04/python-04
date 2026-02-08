"""
Demonstrates secure file handling using the `with` statement.
The program reads classified data and writes new security
information while ensuring the file is automatically closed.
"""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r+") as r:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(r.read())
            print("SECURE PRESERVATION:")
            r.write("\n[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion\n")
            print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Classified vault not found.")

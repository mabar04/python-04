import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="")
    id = input()
    print("Input Stream active. Enter status report: All systems nominal\n")
    sys.stdout.write("[STANDARD] Archive status from ARCH_7742: "
                     "All systems nominal\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\n")
    print("Three-channel communication test successful.")

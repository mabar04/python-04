# python-04

# Exercise 0

## Description
This program simulates a data recovery process from a storage vault.  
It reads the file `ancient_fragment.txt`, displays the recovered data, and confirms that the connection is properly closed.  
If the file does not exist, the program prints an error message.

## Answer to the Questions

### What happens to the storage system if connections aren’t properly closed?
If a file is not closed, system resources remain in use, files may stay locked, and the program or system can slow down or run into errors after too many open files.
### Why is the disconnect protocol critical?
Closing the file ensures all data is safely handled, frees system resources, and allows other programs to access the file correctly.

# Exercise 1

## Description
This program simulates creating a new archive entry in the Cyber Archives system.  
It creates a file named `new_discovery.txt`, writes three preservation entries into it, and confirms that the archive was successfully created and sealed.

## How the Program Works
1. Prints a system header.
2. Opens (or creates) `new_discovery.txt` in write mode.
3. Writes three archive entries to the file.
4. Displays the same entries in the terminal.
5. Closes the file to ensure data is saved properly.

## Answer to the Questions

### What’s the critical difference between extraction mode ('r') and preservation mode ('w')?
'r' (read mode) opens a file for reading only and does not modify its contents.
'w' (write mode) creates a new file or overwrites an existing one, replacing all previous data.

### Why is this distinction vital for archivists?
Because opening a file in write mode can permanently erase existing data. Archivists must be careful to avoid accidentally overwriting valuable or historical information.

# Exercise 2 – Stream Management

## Description
This program demonstrates how to use Python’s three standard data streams:
- `stdin` for receiving user input
- `stdout` for standard program output
- `stderr` for alert and diagnostic messages

The program collects an archivist ID and a status report, then routes
messages to the correct communication channels.

## Why separate streams?
The Archives maintain separate channels to ensure clarity and reliability.
Standard data and alerts serve different purposes and must not interfere
with each other.

## Questions & Answers

### Why do the Archives maintain separate channels for standard data and alerts?
Separate channels allow systems and operators to distinguish between normal
operation messages and critical alerts. This prevents important warnings
from being lost among regular output.

### What could happen if these streams were mixed?
If alerts were sent through the standard output channel, critical warnings
could be overlooked, delayed, or ignored, leading to system failures or
data loss.

# Exercise 3 – Vault Security

## Description
This program demonstrates secure file handling using Python’s
`with` statement (context manager).

The program:
- Opens a classified vault file
- Extracts stored data
- Archives new information
- Automatically seals the vault after operations

## Questions & Answers

### How does the with protocol prevent data corruption?
The `with` statement automatically closes the file after the block
finishes, even if an error occurs. This ensures that resources are
released properly and that partially written data does not corrupt
the file.

### What is the RAII principle and why is it crucial for vault security?
RAII (Resource Acquisition Is Initialization) means that resources
are acquired and released in a controlled way tied to object lifetime.
In file handling, this guarantees that files are closed properly,
preventing data loss, corruption, or resource leaks.

# Exercise 4 – Crisis Response

## Description
This program simulates a crisis response system for digital archives.

It:
- Attempts to access archive files
- Handles missing files
- Handles permission errors
- Handles unexpected system errors
- Uses the `with` statement to ensure files are safely closed

The program demonstrates how proper error handling prevents crashes
and maintains system stability.

---

## Questions & Answers

### What are the most dangerous threats to digital archives?

The most dangerous threats include:
- Missing or deleted files
- Permission and security errors
- Data corruption
- Unexpected system failures
- Improper file handling that leaves files open

These issues can lead to data loss or unstable systems if not handled correctly.

---

### How does proper crisis response prevent data loss and maintain system stability?

Proper crisis response:
- Detects errors using try/except blocks
- Prevents program crashes
- Ensures files are closed safely using the `with` statement
- Provides clear messages about what went wrong
- Allows the system to continue running even after failures

This keeps the archive system stable and protects stored data.

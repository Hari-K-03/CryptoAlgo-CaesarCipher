# Cryptography Concepts

## Encryption using August Cipher through a custom Hash Function

---

## Description

This project implements encryption of a message by implementing August Cipher and using custom Hash Functions.

A message is first filtered using a defined character set, hashed using a custom hash function, concatenated with the hash, and then encrypted using August cipher. The system also supports decryption and message integrity verification.

---

## Features

- Custom non-cryptographic hash function
- Message filtering using defined character set
- August Cipher
- Decryption support
- Message authentication
- Menu-driven interface

---

## How It Works

1. Input message is filtered to include only allowed characters
2. A hash value is generated for the filtered message
3. The hash is appended to the message
4. The combined string is encrypted using August cipher
5. During decryption, the message and hash are separated
6. The hash is recomputed and compared for authentication

---

## Character Set

"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,-\_@"

---

## How to Run

1. Clone the repository
2. Navigate to the project folder
3. Run the program using Python

---

## Menu Options

- Encrypt Message
- Decrypt Message
- Authenticate
- Exit

---

## Example

- Input Message: Hello
- Encrypted Output: Ifmmp491122361
- Decrypted Output: Hello380011250
- Authentication: Valid

---

## Custom Hash Function:

This project uses a custom non-cryptographic hash function inspired by the FNV (Fowler–Noll–Vo) hashing technique.

The hash is initialized with a constant value (2166136261). For each character in the input message, the following operations are performed:

- XOR the current hash value with the ASCII value of the character.
- Multiply the result by a large prime number (16777619).
- Apply a bitwise right shift and XOR operation for additional mixing.
- Take modulo (10^9 + 7) to keep the value within a fixed range.

This process ensures that small changes in the input message produce significantly different hash values.

Note: Produces integer hash values in the range 0 to 1,000,000,006

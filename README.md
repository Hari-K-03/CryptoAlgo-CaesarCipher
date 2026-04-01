# Cryptography Concepts

## Encryption using August Cipher through a custom Hash Function

---

## Description

This project implements encryption of a message by implementing August Cipher and using custom Hash Functions.

A message is first filtered using a defined character set, hashed using a custom hash function, concatenated with the hash, and then encrypted using August cipher. The system also supports decryption and message integrity verification.

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

### Output 1

- Input Message: Hi, hello and welcome
- Hash Value: 901571682
- Encrypted Output: Ij-.ifmmp.boe.xfmdpnf 12682793
- Decrypted Output: Hi, hello and welcome901571682
- Authentication: Authenticated.

### Output 2

- Input Message: My name is Hari
- Hash Value: 657981888
- Encrypted Output: Nz.obnf.jt.Ibsj768 92999
- Decrypted Output: My name is Hari657981888
- Authentication: Authenticated.

---

## Custom Hash Function

This project uses a custom non-cryptographic hash function inspired by the FNV (Fowler–Noll–Vo) hashing technique.

The hash is initialized with a constant value (2166136261). For each character in the input message, the following operations are performed:

- XOR the current hash value with the ASCII value of the character.
- Multiply the result by a large prime number (16777619).
- Apply a bitwise right shift and XOR operation for additional mixing.
- Take modulo (10^9 + 7) to keep the value within a fixed range.

This process ensures that small changes in the input message produce significantly different hash values.

Note: Produces integer hash values in the range 0 to 1,000,000,006

---

## August Cipher

The August Cipher is a substitution cipher where each character is shifted by exactly one position in the defined character set.

### Working Principle:

- Each character in the message is assigned an index based on its position in the character set.
- A fixed shift value (key=1) is used to transform the message.
- During encryption, each character is shifted forward by the key value, 1.
- During decryption, characters are shifted backward by the same key.

### Formula:

**Encryption:**
E(x) = (x + k) mod n

**Decryption:**
D(x) = (x - k) mod n

Where:

- x = index of the character
- k = shift key
- n = size of the character set

---

## WorkFlow of the Script

Message Input → Message Filtering → Hash Generation → Concatenate (Message+Hash) → Encryption → Decryption → Split (Message,Hash) → Recompute Hash → Compare Hashes → Authenticated/Not Authenticated

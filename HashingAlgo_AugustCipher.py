charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,-_@"
N=len(charset)
def hash_function(message):
    H = 2166136261
    
    for c in message:
        H ^= ord(c)
        H = (H * 16777619) ^ (H >> 13)
        H = H % (10**9 + 7)
    
    return H

def final_encryption(message):
    global n
    text=""
    #Remove characters not in charset
    for c in message:   
        if c in charset:
            text+=c
        else:
            n-=1                            #Length of msg reduces when ignoring characters not in charset
    hash_value = hash_function(text)
    combined = text + str(hash_value)
    encrypted_text=encrypt(combined)
    return encrypted_text

def encrypt(text):
    encrypted=""
    for c in text:
        new_index = (charset.index(c) + 1) % N
        encrypted += charset[new_index]
    return encrypted

def decrypt(text):
    decrypted = ""
    
    for c in text:
        new_index = (charset.index(c) - 1) % N
        decrypted += charset[new_index]
    
    return decrypted

while True:
    print("\n--- MENU ---")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Authenticate")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if (choice=="1"):
        msg=input("Enter message: ")
        n=len(msg)
        encrypted_msg=final_encryption(msg)
        print("Encrypted text: ", encrypted_msg)
    
    elif (choice=="2"):
        decryptedtext=decrypt(encrypted_msg)
        print(decryptedtext)
    
    elif (choice=="3"):
        decryptedmsg=decryptedtext[:n]
        decryptedhash=decryptedtext[n:]
        if (str(hash_function(decryptedmsg))==decryptedhash):
            print("Authenticated.")
        else:
            print("Not Authenticated.")
    elif (choice=="4"):
        print("Thank you.")
        break
    else:
        print("Invalid choice.")


    
    
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Choose an option (1 or 2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Exiting program.")
        return

    mode = "encrypt" if choice == "1" else "decrypt"
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

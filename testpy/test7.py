def atbash_cipher(message):
    shifri = {chr(i): chr(219 - i) for i in range(97, 123)}

    result = ''.join(shifri.get(char.lower(), char) for char in message)

    return result

message = input("Enter any word: ")

decoded = print(f"decoded - {atbash_cipher(message)}")
original = print(f"original - {message}")


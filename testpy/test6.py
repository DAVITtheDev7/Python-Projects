text = "please search facebook"
strings_to_remove = ["please", "search"]

for string in strings_to_remove:
    text = text.replace(string, "")

print(text)

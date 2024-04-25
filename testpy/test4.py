from googlesearch import search
import re


user_input = input("\nYou: ")

if "calculate" in user_input:
 
    replaces2 = {"please" : "", "calculate" : ""}

    result = re.sub("|".join(replaces2.keys()), lambda match: replaces2[match.string[match.start():match.end()]], user_input)

    final = eval(result)
    print(final)
    
else:
    print("Chatbot: What I should search?")



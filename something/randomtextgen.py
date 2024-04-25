import random
import string

hello_world = "zzzz"
generated_string = ""

while generated_string != hello_world:
    generated_string = ''.join(random.choices(string.ascii_lowercase, k=len(hello_world)))
    print(generated_string)

print("Generated string is equal to 'hello world':", generated_string)

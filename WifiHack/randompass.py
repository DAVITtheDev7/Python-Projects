import random

password = False

mywifi = "12345678"

while True:
    p_1 = str(random.randint(0,9))
    p_2 = str(random.randint(0,9))
    p_3 = str(random.randint(0,9))
    p_4 = str(random.randint(0,9))
    p_5 = str(random.randint(0,9))
    p_5 = str(random.randint(0,9))
    p_6 = str(random.randint(0,9))
    p_7 = str(random.randint(0,9))
    p_8 = str(random.randint(0,9))


    final_pass = p_1 + p_2 + p_3 + p_4 + p_5 + p_6 + p_7 + p_8

    print(final_pass)

    if final_pass == mywifi:
        break


print(f"\n Your password: {final_pass}")
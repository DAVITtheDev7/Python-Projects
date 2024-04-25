import json
import time
import random
import pyautogui

n = int(input("\nHow many words do you want? "))
print("\nYou have 3 seconds!\n")

count = 3
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

fname = open("words.json")
file = json.load(fname)

start = time.time()

score = 0
for i in range(n):
    word = random.choice(file)
    print("\n" + word)
    answer = input("")
    if answer == word:
        score += 1

end = time.time()

TotalTime = int(end - start)
percent = int((score/n)*100)


pyautogui.alert(title = 'Result', text = f"It took you {TotalTime} seconds\nYou have guessed {score} words. {percent}%." )


import math
import pyautogui


def twod_plane():
    x1 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "X")
    y1 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "Y")

    x2 = pyautogui.prompt(title = "Distance Calculator -- Second point", text = "X")
    y2 = pyautogui.prompt(title = "Distance Calculator -- Second point", text = "Y")

    try:
        result  = math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2 )
    except ValueError:
        pyautogui.alert(text = "Enter numbers only!")

    pyautogui.alert(text = f"\nDistance is {result} \n")

def threed_plane():
    x1 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "X")
    y1 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "Y")
    z1 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "Z")

    x2 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "X")
    y2 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "Y")
    z2 = pyautogui.prompt(title = "Distance Calculator -- First point", text = "Z")

    try:
        result  = float(math.sqrt((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2 + (float(z2) - float(z1))**2))
    except ValueError:
        pyautogui.alert(text = "Enter numbers only!")

    pyautogui.alert(text = f"\nDistance is {result} \n")

while True:
    plane = pyautogui.prompt(text = "\nWhich: 2D or 3D (or type 'exit' to exit)?")

    if plane == "2d" or plane == "2":
        twod_plane()
    elif plane == "3d" or plane == "3":
        threed_plane()
    elif plane == 'exit':
        break
    else:
        pyautogui.alert("\tTry Again!")
        continue
        

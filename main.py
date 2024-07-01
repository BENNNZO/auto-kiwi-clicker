import pyautogui, time, keyboard

PROFESSION_POS_1 = [3200, 1330]
PROFESSION_POS_2 = [1930, 1270]
PROFESSION_POS_3 = [3280, 110]

def goto_kiwi():
    kiwi_coords = pyautogui.locateCenterOnScreen('imgs/kiwi.png', confidence=0.5)
    pyautogui.moveTo(kiwi_coords)

def goto_target():
    print("hello world!")

def upgrade():
    keys = ["t", "4", "q", "4", "w", "4", "e", "4", "r", "4"]

    for key in keys:
        pyautogui.press(key)
        time.sleep(0.1)

def professions():
    for coords in [PROFESSION_POS_1, PROFESSION_POS_2, PROFESSION_POS_3]:
        pyautogui.leftClick(coords[0], coords[1])
        time.sleep(0.5)


def main():
    # print("Starting In 10 Seconds...")
    print("To exit the loop hold 'Z' until the loop is broken")
    time.sleep(3)

    while True:
        time.sleep(5)
        upgrade()

        if keyboard.is_pressed("z"):
            print("broke while loop now exiting")
            break

        print("loop!")

if __name__ == "__main__":
    # main()
    goto_kiwi()
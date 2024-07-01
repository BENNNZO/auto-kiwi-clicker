import pyautogui, time, keyboard

PROFESSION_POS_1 = [3200, 1330]
PROFESSION_POS_2 = [1930, 1270]
PROFESSION_POS_3 = [3280, 110]

def move_to(img_path: str, confidence: float, duration: float, click: bool):
    coords = pyautogui.locateCenterOnScreen(img_path, confidence=confidence if confidence else 0.7)
    pyautogui.moveTo(coords, duration=duration if duration else 0)
    if (click): pyautogui.leftClick(coords)

def goto_kiwi(): 
    move_to('imgs/kiwi.png', 0.7, 0.25, False)

def goto_target(): 
    move_to('imgs/target.png', 0.7, 0.25, False)

def buy_upgrades():
    keys = ["t", "4", "q", "4", "w", "4", "e", "4", "r", "4"]

    for key in keys:
        pyautogui.press(key)
        time.sleep(0.02)

def professions():
    for i in range(3):
        move_to(f'imgs/profession{i}.png', 0.7, 0.2, True)
        time.sleep(0.5)

def collect_orbs():
    for i in range(5):
        move_to('imgs/sekiwity.png', 0.7, 0.25, False)
        pyautogui.moveRel(1000, 0, 2)

def transend():
    pyautogui.press('g')
    time.sleep(0.1)
    pyautogui.press('g')


def main():
    time.sleep(3)

    while True:
        transend()
        time.sleep(2)

        goto_kiwi()
        time.sleep(2)
        buy_upgrades()

        professions()

        goto_target()

        for i in range(10):
            buy_upgrades()
        
        pyautogui.press('r')
        collect_orbs()

        if keyboard.is_pressed("z"):
            break

        print("loop!")

if __name__ == "__main__":
    main()
    # goto_kiwi()
    # professions()
    # collect_orbs()
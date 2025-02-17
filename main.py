import pyautogui, time, keyboard

def move_to(img_path: str, confidence: float, duration: float, click: bool):
    coords = pyautogui.locateCenterOnScreen(img_path, confidence=confidence if confidence else 0.7)
    pyautogui.moveTo(coords, duration=duration if duration else 0)
    if (click): pyautogui.leftClick(coords)

def goto_kiwi(): 
    move_to('imgs/kiwi.png', 0.7, 0.1, False)

def goto_target(): 
    move_to('imgs/target.png', 0.7, 0.1, False)

def buy_upgrades():
    keys = ["t", "4", "q", "4", "w", "4", "e", "4", "r", "4"]

    for key in keys:
        pyautogui.press(key)
        time.sleep(0.01)

def professions():
    for i in range(3):
        move_to(f'imgs/profession{i}.png', 0.7, 0.2, True)
        time.sleep(0.5)

def collect_orbs():
    move_to('imgs/sekiwity.png', 0.7, 0.25, False)
    pyautogui.moveRel(1250, 0, 2)

def transend():
    for i in range(2):
        pyautogui.press('g')


def main():
    time.sleep(3)
    while True:
        try:
            while True:
                transend()

                # time.sleep(1)
                # goto_kiwi()
                
                # time.sleep(5)
                # buy_upgrades()

                # professions()

                goto_target()

                for i in range(35):
                    buy_upgrades()
                
                pyautogui.press('r')
                for i in range(3):
                    collect_orbs()

                if keyboard.is_pressed("z"):
                    break
        except:
            print("ERROR: restarting loop")



if __name__ == "__main__":
    main()
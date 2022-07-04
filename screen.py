import keyboard
import pyautogui
from PIL import ImageGrab
from PIL import Image
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
from datetime import datetime
import os
import sys

class Screenshot:
    STOP_COMBINATION = "ctrl+shift+x"

    def Reformat_Image(self, ImageFilePath):
        print(ImageFilePath)
        image = Image.open(ImageFilePath, 'r')
        image_size = image.sizeё
        width_p = image_size[0]
        height_p = image_size[1]

        if(width_p != height_p):
            f = open("settings.txt", 'r')
            for i in range(4):
                w = int(f.readline())
            space = f.readline()    
            WA = int(f.readline())
            HA = int(f.readline())
            WO = int(f.readline())
            HO = int(f.readline())
            

            background = Image.new('RGBA', (width_p+WA, height_p + HA), (255, 255, 255, 255))
            offset = (WO, HO)
            newsize = (width_p - 110, height_p - 180)
            img = image.resize(newsize)
            
            background.paste(img, offset)
            background.save(ImageFilePath)

            #img.save(ImageFilePath)
            print("Image has been resized !")

        else:
            print("Image is already a square, it has not been resized !")

    def __init__(self, dir: str) -> None:
        self.path = os.path.join(os.getcwd(), dir)

    def run(self) -> None:
        self.__create_path_if_absent()
        keyboard.on_press(self.__keyboard_callback)
        keyboard.wait(self.STOP_COMBINATION)

    def __create_path_if_absent(self):
        if not os.path.exists(self.path):
            try:
                os.makedirs(self.path)
            except Exception as e:
                print(e)
                # Check https://github.com/boppreh/keyboard/issues/167
                os._exit(0)

    def __keyboard_callback(
            self, event: keyboard._keyboard_event.KeyboardEvent) -> None:
        if event.name == "`" or event.name == "ё" :
            print('Создание фотографии')
            self.__create_screenshot()

    def __create_screenshot(self) -> None:
        self.__create_path_if_absent()

        name = datetime.now().strftime("%d-%m-%Y_%H_%M_%S_%f")
        print('Имя:', name)
        print()
        f = open("settings.txt", 'r')
        X1 = int(f.readline())
        Y1 = int(f.readline())
        X2 = int(f.readline())
        Y2 = int(f.readline())
        f.close()
        pyautogui.screenshot(region=(X1,Y1, X2, Y2)).save(os.path.join(self.path, f"{name}.png"))
        path_img = str(os.path.join(self.path, f"{name}.png"))
        print(path_img)
        self.Reformat_Image(path_img)
        #img = Image.open(os.path.join(self.path, f"{name}.png"))
        #new_image = img.resize((1305 , 1695))
        #new_image.save(os.path.join(self.path, f"{name}.png"))

if __name__ == "__main__":
    dir = 'screens' if len(sys.argv) < 2 else sys.argv[1]
    screen = Screenshot(dir)
    screen.run()

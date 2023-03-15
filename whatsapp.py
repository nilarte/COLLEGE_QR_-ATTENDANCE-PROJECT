import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+917980136952",
            message=msg,
            tab_close=True
        )
        time.sleep(5)
        pyautogui.click()
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="Registered Sucessfully!")
    pywhatkit.sendwhats_image("+7980136952","C:\\Users\\AA\\Downloads\\rajju.jpg" )

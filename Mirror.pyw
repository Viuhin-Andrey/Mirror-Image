# Command to install dependencies:
# pip install opencv-python numpy keyboard mss pyautogui
import cv2
import numpy as np
import os
import keyboard
from mss import mss
import pyautogui
import ctypes

# Configuration Settings
SAVE_PATH = r"C:\Users\Andrew\Desktop\Screenshots"
os.makedirs(SAVE_PATH, exist_ok=True)

is_flipped = False
image_counter = 0
m_key_pressed = False
s_key_pressed = False

def show_confirmation_dialog():
    result = ctypes.windll.user32.MessageBoxW(
        0,
        f"Save screenshot to folder?\n{SAVE_PATH}",
        "Save Confirmation",
        0x00000001 | 0x00000040
    )
    return result == 1

def get_current_screen():
    x, y = pyautogui.position()
    with mss() as sct:
        for monitor in sct.monitors[1:]:
            if (monitor['left'] <= x < monitor['left'] + monitor['width'] and
                monitor['top'] <= y < monitor['top'] + monitor['height']):
                return monitor
        return sct.monitors[1]

def capture_screen():
    current_monitor = get_current_screen()
    if not current_monitor:
        return None

    with mss() as sct:
        screenshot = sct.grab({
            'left': current_monitor['left'],
            'top': current_monitor['top'],
            'width': current_monitor['width'],
            'height': current_monitor['height']
        })
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGRA2BGR)

def display_image(original_frame):
    global is_flipped, image_counter, m_key_pressed, s_key_pressed
    
    current_mon = get_current_screen()
    cv2.namedWindow("Screen Mirror", cv2.WINDOW_NORMAL)
    cv2.moveWindow("Screen Mirror", current_mon['left'], current_mon['top'])
    cv2.setWindowProperty("Screen Mirror", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    height, width = original_frame.shape[:2]
    text = "Press 'M' to mirror | Press 'S' to save | Press 'Esc' to exit"
    
    while True:
        display_frame = cv2.flip(original_frame, 1) if is_flipped else original_frame.copy()
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
        text_x = (width - text_size[0]) // 2
        text_y = height - 10
        
        overlay = display_frame.copy()
        cv2.putText(overlay, text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow("Screen Mirror", overlay)
        
        if keyboard.is_pressed('m') and not m_key_pressed:
            is_flipped = not is_flipped
            m_key_pressed = True
        elif not keyboard.is_pressed('m'):
            m_key_pressed = False
            
        if keyboard.is_pressed('s') and not s_key_pressed:
            if show_confirmation_dialog():
                filename = f"screenshot_{image_counter}_{'mirrored' if is_flipped else 'original'}.png"
                full_path = os.path.join(SAVE_PATH, filename)
                
                try:
                    cv2.imwrite(full_path, display_frame)
                    image_counter += 1
                except Exception as e:
                    ctypes.windll.user32.MessageBoxW(
                        0,
                        f"Save error: {str(e)}",
                        "Error",
                        0x00000010
                    )
            s_key_pressed = True
        elif not keyboard.is_pressed('s'):
            s_key_pressed = False
            
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            os._exit(0)

if __name__ == "__main__":
    while True:
        frame = capture_screen()
        if frame is not None:
            display_image(frame)

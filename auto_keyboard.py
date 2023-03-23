import time
import pyautogui
from datetime import datetime

def saver() :
    screenWidth, screenHeight = pyautogui.size() 
	#화면 전체 크기를 출력(화면 해상도) 
    print('{}, {}'.format(screenWidth, screenHeight)) 
    cnt = 0 

    while True :
        # t 라는 문자를 입력
        pyautogui.write('t', interval=0.25) 
        cnt += 1 
        print('{} 번째 동작중'.format(cnt)) 
        time.sleep(120) 
        print(datetime.now())

if __name__ =="__main__" : 
	saver()
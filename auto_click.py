import time
import pyautogui
import random
from datetime import datetime

def saver() :
    screenWidth, screenHeight = pyautogui.size() 
	#화면 전체 크기를 출력(화면 해상도) 
    print('{}, {}'.format(screenWidth, screenHeight)) 
    cnt = 0 

    while True : 
        #마우스 클릭 - 2번 클릭할건데 0.2초마다
        pyautogui.click(clicks=2, interval=0.2)
        cnt += 1 
        print('{} 번째 동작중'.format(cnt)) 
        time.sleep(120) 
        print(datetime.now())

if __name__ =="__main__" : 
	saver()
import keyboard
import time
import ctypes
import win32gui
import time
from PIL import ImageGrab

def backgronud(px):
    if(px[0] <= 0 and 25 <= px[1] and px[1] <= 31 and 35 <= px[2] and px[2] <= 42): #90 25 80 35 85
        return 1
    elif (px[0] > 100 or px[1] > 100 or px[2] > 100): 
        return 3
    else:
        return 2
noise = 22
lowSpeedReflectionTime = noise + 20
HighSpeedReflectionTime = noise + 35
aheadinit = noise + 60
ahead = aheadinit
# 46 and 13 are good with normal speed
# 66 and 27 are good with normal speed
centerx = 1919//2 + 1
centery = 1079//2 + 28
t = 0
direction = 0
prevDirection = 0
time.sleep(3)
while True :
    time.sleep(0.01)
    px = ImageGrab.grab().load()
    if ahead < aheadinit :
        ahead = ahead + 1
    #print(direction)
    if direction == 0: 
        top = px[centerx, centery - ahead]
        #print(top)
        if backgronud(top) != 1:
            j = 1
            while backgronud(px[centerx, centery - (ahead + j)]) != 3 and j < 20:
                j = j + 1
            if j == 20:
                continue
            i = 1
            while backgronud(px[centerx - i, centery - lowSpeedReflectionTime]) != 3 and i < 100:
                i = i + 1
            k = 1
            while backgronud(px[centerx + k, centery - lowSpeedReflectionTime]) != 3 and k < 100:
                k = k + 1            
            if i < aheadinit:
                if k < aheadinit:
                    keyboard.press_and_release("right")
                    keyboard.press_and_release("down")
                    prevDirection = 1
                    direction = 3
                else:
                    keyboard.press_and_release("right")
                    prevDirection = direction
                    direction = 1   
            else:
                if k < aheadinit or (k >= aheadinit and prevDirection == 2):
                    keyboard.press_and_release("left")
                    prevDirection = direction
                    direction = 2
                else:
                    keyboard.press_and_release("right")
                    prevDirection = direction
                    direction = 1
            ahead = HighSpeedReflectionTime
    elif direction == 1 :
        right = px[centerx + ahead, centery]
        #print(right)
        if backgronud(right) != 1:
            j = 1
            while backgronud(px[centerx + (ahead + j), centery]) != 3 and j < 20:
                j = j + 1
            if j == 20:
                continue
            i = 1
            while backgronud(px[centerx - lowSpeedReflectionTime, centery - i]) != 3 and i < 100:
                i = i + 1
            k = 1
            while backgronud(px[centerx - lowSpeedReflectionTime, centery + k]) != 3 and k < 100:
                k = k + 1            
            if i < aheadinit:
                if k < aheadinit:
                    keyboard.press_and_release("up")
                    keyboard.press_and_release("left")
                    prevDirection = 0
                    direction = 2
                else:
                    keyboard.press_and_release("down")
                    prevDirection = direction
                    direction = 3 
            else:
                if k < aheadinit or (k >= aheadinit and prevDirection == 0):
                    keyboard.press_and_release("up")
                    prevDirection = direction
                    direction = 0
                else:
                    keyboard.press_and_release("down")
                    prevDirection = direction
                    direction = 3
            ahead = HighSpeedReflectionTime
    elif direction == 2 :
        left = px[centerx - ahead, centery]
        #print(left)
        if backgronud(left) != 1:  
            j = 1
            while backgronud(px[centerx - (ahead + j), centery]) != 3 and j < 20:
                j = j + 1
            if j == 20:
                continue
            i = 1
            while backgronud(px[centerx - lowSpeedReflectionTime, centery - i]) != 3 and i < 100:
                i = i + 1
            k = 1
            while backgronud(px[centerx - lowSpeedReflectionTime, centery + k]) != 3 and k < 100:
                k = k + 1            
            if i < aheadinit:
                if k < aheadinit:
                    keyboard.press_and_release("up")
                    keyboard.press_and_release("right")
                    prevDirection = 0
                    direction = 1
                else:
                    keyboard.press_and_release("down")
                    prevDirection = direction
                    direction = 3
            else:
                if k < aheadinit or (k >= aheadinit and prevDirection == 0):
                    keyboard.press_and_release("up")
                    prevDirection = direction
                    direction = 0
                else:
                    keyboard.press_and_release("down")
                    prevDirection = direction
                    direction = 3
            ahead = HighSpeedReflectionTime
    elif direction == 3 :
        bot = px[centerx, centery + ahead]
        #print(bot)
        if backgronud(bot) != 1:
            j = 1
            while backgronud(px[centerx, centery + (ahead + j)]) != 3 and j < 20:
                j = j + 1
            if j == 20:
                continue
            i = 1
            while backgronud(px[centerx - i, centery + lowSpeedReflectionTime]) != 3 and i < 100:
                i = i + 1
            k = 1
            while backgronud(px[centerx + k, centery + lowSpeedReflectionTime]) != 3 and k < 100:
                k = k + 1            
            if i < aheadinit:
                if k < aheadinit:
                    keyboard.press_and_release("right")
                    keyboard.press_and_release("up")
                    prevDirection = 1
                    direction = 0
                else:
                    keyboard.press_and_release("right")
                    prevDirection = direction
                    direction = 1   
            else:
                if k < aheadinit or (k >= aheadinit and prevDirection == 2):
                    keyboard.press_and_release("left")
                    prevDirection = direction
                    direction = 2
                else:
                    keyboard.press_and_release("right")
                    prevDirection = direction
                    direction = 1
            ahead = HighSpeedReflectionTime

'''

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
while True :
    a = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1919//2,1079//2 + 24 - 20)
    print (a)
    #time.sleep(0.1)

time.sleep(4)
while True:
    px = ImageGrab.grab().load()
    j = 1
    while j < 50:
        j = (j+1)
        print(px[centerx, centery - 15 -j],j)
    time.sleep(0.01) #0.001 bel 10
    print("****")
'''

# the closer the value to zero the more probable it is a background
'''def backgronudScore(px):
    return 3 * px[0] + abs(29 - px[1]) + abs(40 - px[2]) 
def continueStraight(pxAhead, px1, px2):
    if backgronud(px1) == False and backgronud(px2) == False and (backgronudScore(pxAhead) < backgronudScore(px1) or backgronudScore(pxAhead) < backgronudScore(px2)):
        return True
    else:
        return False
'''
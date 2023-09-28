import os
import pyautogui as pag
import time
import pydirectinput as pdi

NPC_KEY = 'n'
left = 'left'
right = 'right'
up = 'up'
down = 'down'

def main():
    char_x = None
    candy_x = None
    while char_x is None:
        try:
            char_x, char_y,_,_ = pag.locateOnScreen('pics/charname.png',confidence=0.70)
        except:
            print("Couldn't detect character. Moving right a bit and trying again...")
            move('right',0.5)
    print(f'Character detected at: X: {str(char_x)}, Y: {str(char_y)}')
    
    while candy_x is None:
        try:
            candy_x, candy_y,_,_ = pag.locateOnScreen('pics/pinkstarcandy.png',confidence=0.80)
        except:
            print("Couldn't detect candy. Moving right a bit and trying again...")
            move('right',0.5)
    print(f'Candy detected at: X: {str(candy_x)}, Y: {str(candy_y)}. Moving there now...')
    
    if abs(char_y - candy_y) > 175:
        climb(char_x,char_y)
        char_x = None
        while char_x is None:
            try:
                char_x, char_y,_,_ = pag.locateOnScreen('pics/kshionname.png',confidence=0.65)
            except:
                move('right',0.5)
        
    if char_x > candy_x:
        move('left',(char_x-candy_x)/200)
    else:
        move('right',(candy_x-char_x)/200)

    pdi.press('n')
    time.sleep(0.1)
    


def climb(char_x,char_y):
    vines_x = None
    while vines_x is None:
        try:
            vines_x,vines_y,_,_ = pag.locateOnScreen('pics/vines.png',confidence=0.65)
        except:
            pass

    #set climb direction
    if char_y - vines_y > 200:
        climb_direction = up
    else:
        climb_direction = down

    CLIMB_TIME = 2
    
    if char_x > (vines_x+220):
        #go to right vine
        if char_x > vines_x+455:
            #1 second of walking - ~215 pixels
            #right vine - 455 pixels away from left vine
            move('left',(char_x-(vines_x+455))/215)
            move(climb_direction,CLIMB_TIME)
        else:
            move('right',((vines_x+455)-char_x)/215)
            move(climb_direction,CLIMB_TIME)
    else:
        #go to left vine
        if char_x > vines_x:
            move('left',(char_x-(vines_x))/215)
            move(climb_direction,CLIMB_TIME)
        else:
            move('right',((vines_x)-char_x)/215)
            move(climb_direction,CLIMB_TIME)

def move(direction,duration):
    pag.keyDown(direction)
    time.sleep(duration)
    pag.keyUp(direction)


candies = 0
while True:
    main()
    candies+=1
    print(f"Candies collected: {candies}")




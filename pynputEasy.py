from time import sleep
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as keyboardController
mouse = Controller()
keyboard = keyboardController()

def movePosition(x,y):
    mouse.position = (x, y)
    return True

def mClick(x=None,y=None):
    if None not in (x, y):
        movePosition(x,y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return True

def mRClick(x=None,y=None):
    if None not in (x, y):
        movePosition(x,y)
    mouse.press(Button.right)
    mouse.release(Button.right)
    return True    

def mDoubleClick(x=None,y=None):
    if None not in (x, y):
        movePosition(x,y)
    mouse.click(Button.left, 2)
    return True

def tabKey(times=1):
    for i in range(times):
        oneKey(Key.tab)
        sleep(0.1)
    return True    

def enterKey():
    oneKey(Key.enter)    
    return True

def spaceKey():
    oneKey(Key.space)
    return True

def deleteKey():
    oneKey(Key.delete)
    return True

def upKey():
    oneKey(Key.up)
    return True

def oneKey(key, release=None):
    #################################
    #                               #
    #   None    0       1           #
    #   ----    --      --          #
    #   Press   Press   -           #
    #   Release -       Release     #
    #                               #
    #################################
    if release != 1:
        keyboard.press(key)
        print("press " + str(key) )
    if release != 0:
        keyboard.release(key)
        print("release " + str(key) )

    return True

def keyEdit(key):
    if len(key) > 1:
        key = Key[key]    
    return key    

def typeWord(word):
    lenWord = len(word)
    for i in range(lenWord):
        oneKey(word[i])
        sleep(0.3)
    return True    

def keyCombine(kombin):
    kombin=kombin.lower()
    if "+" not in kombin:
        typeWord(kombin)
        return True

    kombinSplit = kombin.split("+")
    lenKombinSplit = len(kombinSplit)
    for i in range(lenKombinSplit):
        oneKey(keyEdit(kombinSplit[i]), 0)
        if i == lenKombinSplit-1:
            for j in range(lenKombinSplit):
                oneKey(keyEdit(kombinSplit[-j-1]), 1)
    return True                

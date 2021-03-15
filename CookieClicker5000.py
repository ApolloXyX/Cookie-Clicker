import pyautogui

x = 0
cookieLocation = pyautogui.locateOnScreen('Cookie.png')
grandmaLocation = pyautogui.locateOnScreen('Grandma.png')
curserLocation = pyautogui.locateOnScreen('Curser.png')
farmLocation = pyautogui.locateOnScreen('Farm.png')
mineLocation = pyautogui.locateOnScreen('mine.png')
factoryLocation = pyautogui.locateOnScreen('Factory.png')
bankLocation = pyautogui.locateOnScreen('Bank.png')
templeLocation = pyautogui.locateOnScreen('Temple.png')


while True:
    if templeLocation != None:
        pyautogui.click(templeLocation)
        pyautogui.click(cookieLocation)
        templeLocation = pyautogui.locateOnScreen('Temple.png')

    elif bankLocation != None:
        pyautogui.click(bankLocation)
        pyautogui.click(cookieLocation)
        bankLocation = pyautogui.locateOnScreen('Bank.png')

    elif factoryLocation != None:
        pyautogui.click(factoryLocation)
        pyautogui.click(cookieLocation)
        factoryLocation = pyautogui.locateOnScreen('Factory.png')

    elif mineLocation != None:
        pyautogui.click(mineLocation)
        pyautogui.click(cookieLocation)
        mineLocation = pyautogui.locateOnScreen('mine.png')

    elif farmLocation != None:
        pyautogui.click(farmLocation)
        pyautogui.click(cookieLocation)
        farmLocation = pyautogui.locateOnScreen('Farm.png')

    elif grandmaLocation != None:
        pyautogui.click(grandmaLocation)
        pyautogui.click(cookieLocation)
        grandmaLocation = pyautogui.locateOnScreen('Grandma.png')

    elif curserLocation != None:
        pyautogui.click(curserLocation)
        pyautogui.click(cookieLocation)
        curserLocation = pyautogui.locateOnScreen('Curser.png')

    else:
        pyautogui.click(cookieLocation)

    print(x)
    x += 1

    if x % 100 == 0:
        # cookieLocation = pyautogui.locateOnScreen('Cookie.png')
        bankLocation = pyautogui.locateOnScreen('Bank.png')
        grandmaLocation = pyautogui.locateOnScreen('Grandma.png')
        curserLocation = pyautogui.locateOnScreen('Curser.png')
        farmLocation = pyautogui.locateOnScreen('Farm.png')
        mineLocation = pyautogui.locateOnScreen('mine.png')
        factoryLocation = pyautogui.locateOnScreen('Factory.png')
        templeLocation = pyautogui.locateOnScreen('Temple.png')

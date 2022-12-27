from time import sleep 
import pyautogui as pg


def apply(phone): 
    sleep(2)
    # click easy apply button
    try:
        xy = pg.locateOnScreen('img\\easy_apply.png')
        pg.moveTo(xy)
        pg.click()
        sleep(2)
    except:
        print("cant locate easy apply button")
        sleep(2)

    # input phone number
    try:
        pg.press(['tab','tab','tab', 'tab'])
        sleep(2)
        pg.write(str(phone))
        sleep(2)
        pg.press(['tab','tab', 'enter'])
    
    except:
        print("cant locate phone input")

    for i in range(10):          
        # submit or continue
        try:
            submit = pg.locateOnScreen('img\\submit_application.png')
            if submit != None:
                pg.moveTo(submit)
                pg.click()
                print("submition successful")
                return 1
        except:
            try:
                next = pg.locateOnScreen('img\\next.png')
                if next != None:    
                    pg.moveTo(next)
                    pg.click()
            except: 
                print("submit or next button not found")
                sleep(10)

        # click upload resume
        try:
            inp = pg.locateOnScreen('img\\upload_resume.png')
            if inp != None:
                pg.moveTo(inp)
                pg.click()
                sleep(1)
                pg.write("C:\\Users\\Pr Marcos Nascimento\\Desktop\\CS Personal Projects\\Python projects\\JobAppAuto\\assets\\MattResume.pdf")
                pg.press('enter')
                pg.press(['tab','tab','tab', 'tab', 'tab', 'enter'])

                sleep(8)
        except:
            print("failed to submit resume")
            pass
        
    return 0

if __name__ == '__main__':
    print(apply(1234567890))
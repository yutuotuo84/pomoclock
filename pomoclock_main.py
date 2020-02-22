from tkinter.messagebox import askokcancel
from time import sleep
from winsound import Beep

while True:
    Beep(600, 1000)
    if askokcancel(title="休息时间结束！", message="开始一个新的番茄钟吗？"):
        sleep(25*60)
        Beep(600, 1000)
        if askokcancel(title="工作时间结束", message="开始休息吗？"):
            sleep(5*60)
        else:
            break
    else:
        break

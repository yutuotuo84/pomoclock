from tkinter.messagebox import askokcancel
from time import sleep
from winsound import Beep
from datetime import datetime 

pomo_count = 0 
start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    Beep(600, 1000)
    if askokcancel(title="休息时间结束！", message="开始一个新的番茄钟吗？"):
        sleep(25*60)
        pomo_count += 1
        Beep(600, 1000)
        if askokcancel(title="工作时间结束", message="开始休息吗？"):
            sleep(5*60)
        else:
            break
    else:
        break

end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# TODO: 记录下本次运行一共运行了几个番茄钟，并以“日期 开始时间-结束时间 N个番茄钟”的格式保存到records.txt文件
print("本次一共完成了%d个番茄钟" % pomo_count)
with open("records.txt", "a") as f:
    f.write("From "+start_time+" to "+end_time+": completed "+str(pomo_count)+" pomoclocks.\n")
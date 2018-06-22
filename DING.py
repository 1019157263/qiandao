import schedule
import time
import threading
import MIUI
def job():
    print("I'm working...%s")
    MIUI.qian()
    

#schedule.every(0.1).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("00:00").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

def xxx():
  while True:
      schedule.run_pending()
      time.sleep(0.1)

t =threading.Thread(target=xxx)
t.start()
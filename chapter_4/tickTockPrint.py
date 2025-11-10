import time

def tick_tock(seconds: int) -> None:
    flag = True
    for _ in range(seconds):
        if flag:
            print("Tick...")
            time.sleep(1)
            flag = False
        else:
            print("Tock...")
            time.sleep(1)
            flag = True
        

tick_tock(5)

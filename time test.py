import time
help1 = True
while help1 == True:
    now_time = time.asctime( time.localtime(time.time()))
    print(now_time)

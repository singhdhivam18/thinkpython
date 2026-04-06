import pickle
class time:
    hour=0.0
    min=0.0
    sec=0.0
Time=time()
Time.hour=8
Time.min=59
Time.sec=30
Time2=time()
Time2.hour=8
Time2.min=59
Time2.sec=30
start=time()
start.hour=9
start.min=45
start.sec=60
duration=time()
duration.hour=1
duration.min=35
duration.sec=60
def all_sum(t1,t2):
    sum=time()
    sum.hour=t1.hour+t2.hour
    sum.min=t1.min+t2.min
    sum.sec=t1.sec+t2.sec
    return sum
sumtime=all_sum(start,duration)
print("sumtime",sumtime.hour,sumtime.min,sumtime.sec)

def add_all(sumtime):
    while sumtime.sec>=60:
        sumtime.sec-=60
        sumtime.min+=1
    while sumtime.min>=60:
        sumtime.min-=60
        sumtime.hour+=1
    return sumtime
solution2=add_all(sumtime)
print("%.2f:%.2f:%2f" % (solution2.hour,solution2.min,solution2.sec))  
def IS_after(Time,Time2):
    boolvalue=Time is Time2
    return boolvalue
ans=IS_after(Time,Time2)
print(ans)
print("%.2f:%.2f:%2f" % (Time.hour,Time.min,Time.sec))
class Time:
    '''the time object are 
    hour
    mintue
    second'''
    def __init__(self,hour=0,mintue=0,second=0):

        self.hour=hour
        self.mintue=mintue
        self.second=second
    def __str__(self):
        print('%2d,%2d,%2d'%(self.hour,self.mintue,self.second))
time=Time(3,40,30)
time.hour=1
time.mintue=20
time.second=30
def time_to_int(time):
    mintues=time.hour*60+time.mintue
    second=mintues*60+time.second
    return second
timeint=time_to_int(time)
def int_to_time(seconds):
    mintue,time.second=divmod(seconds,60)
    time.hour,time.mintue=divmod(mintue,60)
    return time
inttime=int_to_time(timeint)
print(inttime.hour,inttime.mintue,inttime.second)
start=Time(10,20,30)



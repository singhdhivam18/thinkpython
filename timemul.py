class Time:
    """hour mintue second"""
    def __init__(self,hr=0,min=0,sec=0,num=0):
        self.hr=hr
        self.min=min
        self.sec=sec
        self.num=num
    def __mul__(self,other):
        newtime=Time(0,0,0)
        newtime.hr=self.hr*other.num
        newtime.min=self.min*other.num
        newtime.sec=self.sec*other.num
        return exact_time(newtime)


"""def time_mul(number,t1):
    t_ans=Time()
    t_ans.hr=number*t1.hr
    t_ans.min=number*t1.min
    t_ans.sec=number*t1.sec
    return t_ans"""
def exact_time(time):
    while time.sec>=60:
        time.sec-=60
        time.min+=1
    while time.min>=60:
        time.min-=60
        time.hr+=1
    print("%2d:%2d:%2d"%(time.hr,time.min,time.sec))

#t3=time_mul(3,time1)
#print(t3.hr,t3.min,t3.sec)
time1=Time(3,20,30)
other=Time(0,0,0,3)
obj3=time1*other
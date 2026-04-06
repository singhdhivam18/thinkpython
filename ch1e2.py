"""1. How many seconds are there in 42 minutes 42 seconds?
2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour"""
min=input("enter the minute?")
sec=int(input("enter the seconds?"))
sec_min=min*60
final=sec_min+sec
print("the ans",final)
kilo=int(input("enter the kilometers"))
#1mile=1.61km
res=kilo//1.61
print("the miles are",res)
hr=final/60
avg=res/hr
print(avg)
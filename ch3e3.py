def print_line(first,second):
    print(first,second*4,first,second*4,first)
def print_dash(first,second):
    for _ in range(0,4):
        print(first,second*4,first,second*4,first,second*4)

print_line('+','-')
print_dash("|"," ")
print_line("+","-")
print_dash("|"," ")
print_line("+","-")

__author__ = 'huke'

def get_sum(a,b):
    if(a > b):
        dd=list(range(b,a))
        return (sum(dd))
    elif (a < b):
        dd=list(range(a,b))
        return (sum(dd))
    else:
        return a

print(get_sum(0,6))
print(get_sum(10,6))


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    num=pow(sq,1/2)
    if(float(num).is_integer()):
        num+=1
        return int(pow(num,2))
    return -1
print(find_next_square(625))
print("this is class two")
my_ss=""

def string_cpy(dep,add):
    global my_ss
    if dep == 0:
        return
    my_ss += add
    string_cpy(dep-1,add)


dd=string_cpy(5,'a')
print(my_ss)
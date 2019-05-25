import datetime

stamp = datetime.datetime.now()

def time():
    time = str(stamp)
    print(time)


with open("R1_%s.txt" % time, 'w')as f:
    f.write('hello')


# works fine inside the VM throws an OS error in windows

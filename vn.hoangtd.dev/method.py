##https://www.tutorialspoint.com/python/tk_panedwindow.htm
def print_two(*args):
    arg1,arg2 = args
    print  "arg1: %r, arg2: %r" % (arg1,arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "Done..."

def sum(a,b):
    return a + b;

print "%d " % sum(10,20)
print_two("hoang", "ta duy")
print_two_again("Ta", "Duy Hoang")
print_one("Hoang")
print_none()
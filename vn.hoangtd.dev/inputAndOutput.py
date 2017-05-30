## dau cuoi cau de cho phep nhap cung 1 dong
def methodInput():
    print "How old are you?"
    age = raw_input()
    print "How tell are you?"
    height = raw_input()
    print "How much do you weigh?"
    weight = raw_input()
    print "Age: %r : Height: %r :Weight: %r" % (age, height, weight)

if __name__  == '__main__':
    methodInput()
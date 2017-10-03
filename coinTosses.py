import random

def cointoss():
    head = 0
    tail = 0
    print "Starting the program..."

    for i in range (1,5001):
        num = random.randint(0,1)
        if num == 1:
            head += 1
            print "Attemp #{}: Throwing a coin... It's a head! ... got {} head(s) so far and {} tail(s) so far".format(i,head,tail)
        else:
            tail += 1
            print "Attemp #{}: Throwing a coin... It's a tail! ... got {} head(s) so far and {} tail(s) so far".format(i,head,tail)
    print "Ending the program, thank you!"

cointoss()
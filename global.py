total = 0

def add(n):
    global total
    for i in xrange(n):
        total += (i+1)
    print total

add(100)
print
print total
print

total = 0
for i in xrange(10):
    total += i+1
print total
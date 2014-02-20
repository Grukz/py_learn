import datetime
import itertools

num = 9
num = 10

def my_inductive_permutations_generator(n):
    ans = [[0]]
    if n <= 1:
        yield ans[0]
    temp = []
    for i in xrange(1, n):
        for one in ans:
            for j in xrange(i,-1,-1):
                two = one[:]
                two.insert(j, i)
                if i == n-1:
                    yield two
                else:
                    temp.append(two)
        ans = temp 
        temp = []

def my_permutations_generator_faster(n):
    l = range(n)
    yield l
    if n<=1:
        return
    while 1:
        for i in xrange(n-1, 0, -1):
            l[i], l[i-1] = l[i-1], l[i]
            yield l
        index = 0 
        for i in xrange(1, n):
            if not index and l[i] != n-i-1:
                index = i
                continue
            if index and l[i] == n-index-1:
                l[i], l[i-1] = l[i-1], l[i]
                left = l[:index]
                left.reverse()
                l = l[index:] + left
                yield l
                break
        else:
            return

def python_permutations(n):
    indices = range(n)
    cycles = range(n, 0, -1)
    yield indices
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield indices
                break
        else:
            return

def permute_in_place(n):
    a = range(n)
    yield a
    if n <= 1:
        return
    while 1:
        i = n - 1
        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = n - 1
                while a[i] >= a[j]:
                    j = j - 1
                a[i], a[j] = a[j], a[i]
                r = a[i+1:n]
                r.reverse()
                a[i+1:n] = r
                yield a
                break
            if i == 0:
                return

def get_time_delta(f):
    now = datetime.datetime.now()
    for one in f:
        #print one
        pass
    delta = (datetime.datetime.now() - now)
    print delta

def main():
    get_time_delta(itertools.permutations(range(num)))
    get_time_delta(my_permutations_generator_faster(num))
    get_time_delta(my_inductive_permutations_generator(num))
    get_time_delta(permute_in_place(num))
    get_time_delta(python_permutations(num))

main()






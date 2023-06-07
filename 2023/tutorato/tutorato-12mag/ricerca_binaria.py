

start = 1
end = 100000

def f(x):
    if x < 500:
        return True
    else:
        return False
    
assert(f(start) == True)
assert(f(end) == False)


while end - start > 1:
    print(f"{start} != {end}")

    m = (start + end) // 2

    if f(m):
        start = m
    else:
        end = m

assert(f(start) == True)
assert(f(end) == False)
assert(end - start == 1)

print(f"{start} / {end}")
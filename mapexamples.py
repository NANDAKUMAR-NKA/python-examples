list1=[1,6,9,4]
def demo(a):
    return a**3
list(map(demo,list1))

#
tuple1=(1,6,9,4)
def demo(a):
    return a**3
tuple(map(demo,tuple1))

#
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = list(map(addition, numbers))
print(list(result))
result.append(10)
result
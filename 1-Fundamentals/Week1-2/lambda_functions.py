x=lambda a:a+10
print(x(5))

x=lambda a,b:a*b
print(x(5,6))

x=lambda a,b,c:a+b+c
print(x(5,6,7))

def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
print(mydoubler(11))

mytripler=myfunc(3)
print(mytripler(11))

print((lambda x:x+1)(2))

full_name=lambda first,last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido','van rossum'))

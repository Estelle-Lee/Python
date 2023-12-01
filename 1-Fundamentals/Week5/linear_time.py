import timeit

print(timeit.timeit("[x for x in range(1000000)]",number=1))
print(timeit.timeit("[x for x in range(100000000)]",number=1))
print(timeit.timeit("[x for x in range(10000000000)]",number=1))

'''
$ python linear_time.py
0.0551871
8.560304
Traceback (most recent call last):
  File "C:\Users\ESTELLE\Desktop\NucampFolder\Python\1-Fundamentals\Week5\linear_time.py", line 5, in <module>
    print(timeit.timeit("[x for x in range(10000000000)]",number=1))
  File "C:\Users\ESTELLE\AppData\Local\Programs\Python\Python39\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Users\ESTELLE\AppData\Local\Programs\Python\Python39\lib\timeit.py", line 177, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
  File "<timeit-src>", line 6, in <listcomp>
MemoryError
'''
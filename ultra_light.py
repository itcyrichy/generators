sequence_generator = [x*y for x,y in zip(range(10),range(1,11))]
print(sequence_generator)

ternar_sequence_generator = [x**2 if x%2==0 else x*(-1) for x in range(20)]
print(ternar_sequence_generator)
print('\n')

import time

def decorator1(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        print(f(*args,**kwargs))
        time_dur = time.time() - start
        print(time_dur)
    return wrapper

@decorator1
def f(a,b):
    return [(b)**2/(x+1) for x in range(a)]

f(1000,5000)


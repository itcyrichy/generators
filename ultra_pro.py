from memory_profiler import profile
import psutil
import os


def memo(f):
    def wrapper(*args,**kwargs):
        proc = psutil.Process(os.getpid())
        print(f'Исп. память до:{proc.memory_info().rss/1000000}')
        f()
        print(f'Исп. память после:{proc.memory_info().rss/1000000}')
    return wrapper

@memo
@profile(precision=3)
def create_gen():
    return (x+2 if x%2==0 else x for x in range(1000000))

print('\n')

@memo
@profile(precision=3)
def create_list():
    return [x+2 if x%2==0 else x for x in range(1000000)]

create_list()
create_gen()
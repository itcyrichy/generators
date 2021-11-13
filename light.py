import time

def decorator1(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        f(*args,**kwargs)
        time_dur = time.time() - start
        print(time_dur)
    return wrapper

@decorator1
def create_gen():
    return (x for x in range(1000000))

@decorator1
def create_list():
    return [x for x in range(1000000)]

create_gen()
create_list()
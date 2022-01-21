import threading
import time
import concurrent.futures

'''start = time.perf_counter()

def do_something():
    print('do_something')
    print('sleeping in 3 second')
    time.sleep(3)
    print('Done Sleeping')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start ,2)} seconds(s)')'''

'''start1 = time.perf_counter()
def do_something_with_thread():
    #print('do_something_with_thread')
    print('sleeping in 1 second')
    time.sleep(1)
    print('Done Sleeping')

t1 = threading.Thread(target=do_something_with_thread)
t2 = threading.Thread(target=do_something_with_thread)

t1.start()
t2.start()

finish1 = time.perf_counter()
print(f'Finished in {round(finish1 - start1 , 2)} seconds(s)')'''

'''start2 = time.perf_counter()


def do_something_with_thread1():
    # print('do_something_with_thread1')
    print('sleeping in 3 second')
    time.sleep(1)
    print('Done Sleeping')


t1 = threading.Thread(target=do_something_with_thread1)
t2 = threading.Thread(target=do_something_with_thread1)


t1.start()
t2.start()
t1.join()
t2.join()
finish2 = time.perf_counter()

print(f'Finished in {round(finish2 - start2, 2)} seconds(s)')'''

'''start3 = time.perf_counter()
def thread_with_for():
    print('sleeping in 1 second')
    time.sleep(10)
    print('Done Sleeping')


threads = []
for _ in range(10):
    t = threading.Thread(target=thread_with_for)
     t.start()
    threads.append(t)
   


for thread in threads:
    thread.join()

finish3 = time.perf_counter()
print(f'Finished in {round(finish3 - start3, 2)} seconds(s)') '''

# with function argument

'''start = time.perf_counter()

def thread_with_func_arg(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping')

threads =[]
for _ in range(10):
    t = threading.Thread(target=thread_with_func_arg , args= [1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

# with threadpool executor
''''start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping')

with concurrent.futures.ThreadPoolExecutor() as executor :
    f1 = executor.submit(thread_with_func_threadpool ,1)

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

# now with return value
'''start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor :
    f1 = executor.submit(thread_with_func_threadpool ,1)
    print(f1.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

# 2 threads
'''start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor :
    f1 = executor.submit(thread_with_func_threadpool ,1)
    f2 = executor.submit(thread_with_func_threadpool ,1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

# with list comprehension
'''start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return 'Done Sleeping'

with concurrent.futures.ThreadPoolExecutor() as executor :
    results = [executor.submit(thread_with_func_threadpool,1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

'''start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor :
    secs =[5,4,3,2,1]
    results = [executor.submit(thread_with_func_threadpool,sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')'''

# with map method

start = time.perf_counter()

def thread_with_func_threadpool(seconds):
    print(f'sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor :
    secs =[5,4,3,2,1]
    results = executor.map(thread_with_func_threadpool,secs)
        #[executor.submit(thread_with_func_threadpool,sec) for sec in secs]

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish - start)} second(s)')



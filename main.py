import threading

def count_down(n):
    while n > 0:
        n -= 1

n = 10000000
thread1 = threading.Thread(target=count_down, args=(n,))
thread2 = threading.Thread(target=count_down, args=(n,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

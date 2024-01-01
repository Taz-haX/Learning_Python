import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate boi")
def drink_coffee():
    time.sleep(4)
    print("Ye addict tsk")
def study():
    time.sleep(5)
    print("ouff geni-ass")

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


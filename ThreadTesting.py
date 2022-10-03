from threading import Thread
from time import sleep

def thread_function(x):
    return f'Hello {x}'

class CustomThread(Thread):
    # constructor
    def __init__(self):
        # execute the base constructor
        Thread.__init__(self)
        # set a default value
        self.value = None
 
    # function executed in a new thread
    def run(self):
        # set the return value to be the result of the function
        self.value = self.function(*self.args)

thread = CustomThread()
thread.function = thread_function
thread.args = ('world',)

# start the thread
thread.start()

# wait for the thread to finish
thread.join()

# get the value returned from the thread
data = thread.value
print(data)
import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except :
   print("Error: unable to start thread")

#
time.sleep(5)
# time.sleep(20)



'''
Thread Module
threading.activeCount(): Returns the number of thread objects that are active.

threading.currentThread(): Returns the number of thread objects in the caller's thread control.

threading.enumerate(): Returns a list of all thread objects that are currently active.

Thread Class

run(): The run() method is the entry point for a thread.

start(): The start() method starts a thread by calling the run method.

join([time]): The join() waits for threads to terminate.

isAlive(): The isAlive() method checks whether a thread is still executing.

getName(): The getName() method returns the name of a thread.

setName(): The setName() method sets the name of a thread.
'''
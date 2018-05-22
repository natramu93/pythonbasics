import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name)
      process_data(self.name, self.q)
      print ("Exiting " + self.name)

def process_data(threadName, q):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = q.get()
         queueLock.release()
         print ("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
         time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")



# import threading
# import time
#
# class myThread (threading.Thread):
#    def __init__(self, threadID, name, list):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.list = list
#    def run(self):
#       print ("Starting " + self.name)
#       # Get lock to synchronize threads
#       #threadLock.acquire()
#       print_time(self.name, 2, self.list)
#       # Free lock to release next thread
#       #threadLock.release()
#
# def print_time(threadName, delay, counter):
#    for a in counter:
#       time.sleep(delay)
#       print ("%s: %s %s" % (threadName, time.ctime(time.time()),a))
#       pass
#
#
# threadLock = threading.Lock()
# threads = []
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", ["test1.txt","test2.txt","test3.txt"])
# thread2 = myThread(1, "Thread-2", ["test4.txt","test5.txt","test6.txt"])
#
# threads.append(thread1)
# threads.append(thread2)
#
# for t in threads:
#    t.start()
#
# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")

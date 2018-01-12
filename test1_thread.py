import threading
import time

exitFlag =0

class myThread (threading.Thread):
	def __init__(self, threadid, name, counter):
		threading.Thread.__init__(self)
		self.threadid = threadid
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting ",self.name
		print_time(self.name,5,self.counter)
		print "Exiting",self.name

def print_time(threadname, counter, delay):
	while counter:
		if(exitFlag):
			threadname.exit()
		time.sleep(delay)
		print "%s: %s" % (threadname, time.ctime(time.time()))
		counter -= 1

thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 10)

thread1.start()
thread2.start()

print("Exiting main thread")

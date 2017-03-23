#this is a result

#1st using cookbook code from Python Parallel Programming cookbook ch2
#2d using the recipe to run actual code 

import threading
import time

def function(i):
	print('function called by thread %i\n' %i)
	return

# threads = []
# for i in range(5):
# 	t = threading.Thread(target = function, args = (i,))
# 	threads.append(t)
# 	t.start()
# 	#book says that calling join will cause the master prog to wait untill the current thread finishes
# 	t.join()


def first_function():
	print(threading.currentThread().getName()+str(' is Starting \n'))

	# time.sleep(2)
	# print('Now reading the values from the proximity sensor \n')
	f = open('proxfile.txt', 'r+')
	print("Here is data from the prox sensor: ")
	print(f.read())
	print(threading.currentThread().getName()+ str(' is Exiting \n'))
	return

if __name__ == "__main__":
	t1= threading.Thread(name ='first_prox', target = first_function)
	t2= threading.Thread(name ='second_prox', target = first_function)
	t3= threading.Thread(name ='third_prox', target = first_function)
	t1.start()
	t2.start()
	t3.start()

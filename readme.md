# 多任务

- 并发

  在一段时间内交替去执行多个任务，适用于单核处理器

- 并行

  在一段时间内真正同时一起执行多个任务

# 进程

想要实现多任务可以使用多进程来完成

## 概念

进程(Process)是资源分配的最小单位，是操作系统进行资源分配和调度运行的基本单位，通俗理解：一个正在运行的程序就是一个进程，比如正在运行的qq或者微信

## 多进程

程序运行会默认创建一个进程，这个进程称之为主进程，想要使用多进程，会再创建一个子进程

## 多进程完成多任务

### 进程的创建步骤

1. 导入进程包

```python
import multiprocessing
```

2. 通过进程类创建进程对象

```python
进程对象 = multiprocessing.Process(target, name, group)
```

target：执行的目标函数名

name：进程名，一般不用设置

group：进程组，目前只能使用None

3. 启动进程执行任务

```python
进程对象.start()
```

multiprocess.py

```python
import time
import multiprocessing

def sing():
	for i in range(3):
		print('sing...')
		time.sleep(0.5)

def dance():
	for i in range(3):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	#使用进程类创建进程对象
	sing_process = multiprocessing.Process(target = sing)
	dance_process = multiprocessing.Process(target = dance)

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()

```

```python
sing...
dance...
sing...
dance...
sing...
dance...
```

### 进程执行带有参数的任务

####args参数的使用

```python
multiprocessing.Process(target = sing, args = ((3, ))
```

args：表示以元组的方式给函数传参

#### kwargs参数的使用

```python
multiprocessing.Process(target = sing, kwargs = {'num':3}
```

kwargs：以字典的方式给函数传参

multiprocess_with_para.py

```python
import time
import multiprocessing

def sing(num):
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	#使用进程类创建子进程对象
	sing_process = multiprocessing.Process(target = sing, args = (3, ))
	dance_process = multiprocessing.Process(target = dance, kwargs = {'num': 3})

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()
```

**注意**：这相当于是一个主进程创建了两个子进程

### 获取进程编号

当程序中进程的数量越来越多时，如果没有办法区分主进程和子进程还有不同的子进程，那么就无法进行有效的进程管理，为了方便管理，实际上每个进程都是有自己的编号

#### 获取进程编号的两种方式

1. 获取当前进程编号

```
os.getpid()
```

2. 获取当前父进程编号

```python
def work():
  	#获取当前进程的编号
    print('work进程编号:', os.getpid())
    #获取父进程的编号
    print('work父进程的编号:', os.getppid())
```

get_pid.py

```python
import os
import time
import multiprocessing

def sing(num):
	print('sing pid: ', os.getpid())
	print('sing ppid: ', os.getppid())
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	print('dance pid: ', os.getpid())
	print('dance ppid: ', os.getppid())
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	print('pid: ', os.getpid())
	#使用进程类创建进程对象
	sing_process = multiprocessing.Process(target = sing, args = (3, ))
	dance_process = multiprocessing.Process(target = dance, kwargs = {'num': 3})

	#使用进程对象启动任务
	sing_process.start()
	dance_process.start()
```

### 进程注意点

#### 主进程会等待所有的子进程执行结束再结束

#### 设置守护主进程

主进程结束所有的子进程都结束

guard_main_process.py

```python
import time
import multiprocessing

def work():
	for i in range(10):
		print('工作中...')
		time.sleep(0.2)

if __name__ == '__main__':
	work_process =multiprocessing.Process(target = work)

	#设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
	work_process.daemon = True
	work_process.start()

	time.sleep(1)
	print('主程序执行完成了啦')
```

### Example：传智教学视频文件夹高并发copy器

```python
import os
import shutil
import multiprocessing

def copy_file(source_data, file, target_data):
	print(os.getpid())
	shutil.copy(os.path.join(source_data, file), target_data)

if __name__ == '__main__':
	source_data = '../dai20200511_images_finished'
	target_data = '../copy_test'

	if not os.path.exists(target_data):
		os.mkdir(target_data)

	for file in os.listdir(source_data):
		copy_process = multiprocessing.Process(target = copy_file, args = (source_data, file, target_data))
		copy_process.start()
```

# 线程

## 多线程

进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源，就像跟两个人聊QQ就需要打开两个QQ软件一样是很浪费资源的

**线程**是程序执行的最小单位，实际上进程只负责分配资源，而利用这些资源执行程序的是线程，也就是说进程是线程的容器，**一个进程中最少有一个线程**来负责执行程序。线程自己不拥有系统资源，只需要一点在运行中必不可少的资源，但它**可与同属一个进程的其他线程共享进程所拥有的全部资源**

在进程中程序默认有一个线程来执行程序，被称为**主线程**，创建新的线程被称为子线程

## 使用多线程执行多任务

### 线程的创建步骤

1. 导入线程模块

```python
import threading
```

2. 通过线程类创建线程对象

```python
线程对象 = threading.Thread(target = 任务名)
```

3. 启动线程执行任务

```python
线程对象.start()
```

multithreading.py

```python
import time
import threading

def sing(num):
	for i in range(num):
		print('sing...')
		time.sleep(0.5)

def dance(num):
	for i in range(num):
		print('dance...')
		time.sleep(0.5)

if __name__ == '__main__':
	sing_thread = threading.Thread(target = sing, args = (3, ))
	dance_thread = threading.Thread(target = dance, kwargs = {'num': 2})

	sing_thread.start()
	dance_thread.start()
```

## 主线程会等待所有的子进程执行结束后主线程再结束

### 设置守护主线程

可以让主线程不等待子线程执行完成就可以结束主线程

```python
sing_thread = threading.Thread(target = sing, args = (3, ), daemon = True)
```

或者

```python
sing_thread.setDaemon(True)
```

### 线程间的执行顺序

线程之间执行是无序的

### 获取当前的线程信息

```python
current_thread = threading.current_thread()

print(current_thread)
```

unsorted.py

```python
import time
import threading

def task():
	time.sleep(0.5)
	current_thread = threading.current_thread()
	print(current_thread)

if __name__ == '__main__':
	for i in range(5):
		sub_thread = threading.Thread(target = task)
		sub_thread.start()
```

```python
<Thread(Thread-1, started 123145337344000)>
<Thread(Thread-5, started 123145358364672)>
<Thread(Thread-3, started 123145347854336)>
<Thread(Thread-2, started 123145342599168)>
<Thread(Thread-4, started 123145353109504)>
```

# 进程和线程对比

## 关系对比

1. 线程是依附在进程里面的，没有进程就没有线程
2. 一个进程默认提供一条线程，进程可以创建多个线程

## 区别对比

1. 创建进程的资源开销要比创建线程的开销要大
2. 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位

3. 线程不能独立执行，必须依存在进程中

## 优缺点对比

1. 进程优缺点

   优点：可以用多核

   缺点：开销大

2. 线程优缺点

   优点：资源开销小

   缺点：不能使用多核
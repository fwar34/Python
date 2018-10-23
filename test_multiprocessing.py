from multiprocessing import Process
import os

def proc(name):
    print("Running child process %s (%s)" % (name, os.getpid()))

if __name__ == '__main__':
    print("Parent process(%s)" % os.getpid())
    p = Process(target = proc, args = ('test',))
    print("Child process will start")
    p.start()
    p.join()
    print("Child process end")
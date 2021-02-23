"""
Computer Systems Architecture - Lab 3
"""
from threading import current_thread, enumerate, Condition, Event, Thread


class Master(Thread):
    def __init__(self, max_work, cond):
        Thread.__init__(self, name="Master")
        self.max_work = max_work
        self.cond = cond
        self.first_work = False

    def set_worker(self, worker):
        self.worker = worker

    def run(self):
        for i in range(self.max_work):
            with self.cond:
                # generate work
                self.work = i
                # notify worker
                self.first_work = True
                self.cond.notify()
                # get result
                self.cond.wait()
                if self.get_work() + 1 != self.worker.get_result():
                    print("oops")
                print("%d -> %d" % (self.work, self.worker.get_result()))

    def get_work(self):
        print("get work with self " + str(self) + " from thread " + str(current_thread()) + "\n")
        return self.work


class Worker(Thread):
    def __init__(self, terminate, cond):
        Thread.__init__(self, name="Worker")
        self.terminate = terminate
        self.cond = cond

    def set_master(self, master):
        self.master = master

    def run(self):
        while True:
            with self.cond:
                # wait work
                if not self.master.first_work:
                    self.cond.wait()
                    self.master.first_work = False  # must reset this after first use
                if terminate.is_set(): break
                # generate result
                self.result = self.master.get_work() + 1
                # notify master
                self.result_available = True
                self.cond.notify()

    def get_result(self):
        print("get result with self " + str(self) + " from thread " + str(current_thread()) + "\n")
        return self.result


if __name__ == "__main__":
    # create shared objects
    terminate = Event()
    cond = Condition()

    # start worker and master
    worker = Worker(terminate, cond)
    master = Master(10, cond)
    worker.set_master(master)
    master.set_worker(worker)
    worker.start()
    master.start()

    # wait for master
    master.join()

    # wait for worker
    with cond:
        terminate.set()
        cond.notifyAll()
    worker.join()

    # print running threads for verification
    print(enumerate())

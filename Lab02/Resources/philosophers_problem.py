from threading import Thread, Lock
import time
import argparse

class Philosopher(Thread):
    """Implements a philosopher"""
    """ The philosophers are threads"""
    def __init__(self, id, left_fork, right_fork):
        Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork

    """ The forks are locks """
    def run(self):
        while True:
            """ While holding left fork (lock) """
            self.left_fork.acquire()
            time.sleep(0.1)
            """ Take the right fork (lock) """
            result = self.right_fork.acquire(False)
            
            if result == True:
                break

            self.left_fork.release()
            """ Swap Forks """ 
            self.left_fork, self.right_fork = self.right_fork, self.left_fork

        print("Philosopher %d is eating" % self.id)
        """ Eliberam furculitele """
        self.left_fork.release()
        self.right_fork.release()

def main():
    parser = argparse.ArgumentParser(description="Showcases the philosophers' "
                                     + "problem using locks.")
    parser.add_argument("-p", type=int, required=True, dest="NUM_PHILOSOPHERS",
                        help="the number of philosophers")
    args = parser.parse_args()

    forks = []
    philosophers = [None] * args.NUM_PHILOSOPHERS

    """ A philosopher wants to eat.
        Eat is a task that required both forks (locks).
        Eat could simply mean displaying a message """

    for i in range(args.NUM_PHILOSOPHERS):
        forks.append(Lock())

    """ While holding right fork (lock)
        Take the left fork (lock) """

    for i in range(args.NUM_PHILOSOPHERS):
        philosophers[i] = Philosopher(i, forks[i - 1], forks[i])
        """ Now he can eat. Then he will let go of the forks """
        philosophers[i].start()

    for i in range(args.NUM_PHILOSOPHERS):
        """ asteaptam terminarea threadului """
        philosophers[i].join()

if __name__ == "__main__":
    main()
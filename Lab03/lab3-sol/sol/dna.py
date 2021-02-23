"""
Computer Systems Architecture - Lab 3

Threadpool assignment:
    Use a pool of threads to search for a DNA sequence in a list of DNA samples
"""
import random
from concurrent.futures import ThreadPoolExecutor as ThreadPool

random.seed(0)

# generate many DNA samples, need to be large, otherwise there's no point of parallelization
dna_samples = [[random.choice('ATGC') for _ in range(1, 10000)] for _ in range(50)]

SEARCH_SEQUENCE = ['C', 'G', 'C', 'G', 'G', 'C', 'G', 'T', 'T', 'G', 'A',
                   'C', 'A', 'T', 'T', 'A', 'T', 'G', 'T', 'G']


def search_dna_sequence(sequence, sample):
    """
    Search a DNA sample in a DNA sequence
    :return: True if the sequence was found, False otherwise
    """
    count = 0
    for seq in sample:
        if seq == sequence[count]:
            count += 1
            if count == len(sequence):
                return True
        else:
            count = 0
    return False


def thread_job(sample_index):
    """
    Each thread searches the sequence in a given sample
    """
    if search_dna_sequence(SEARCH_SEQUENCE, dna_samples[sample_index]):
        return "DNA sequence found in sample {}".format(sample_index)
    return "DNA sequence not found in sample {}".format(sample_index)


if __name__ == "__main__":

    thread_pool = ThreadPool(max_workers=10)

    futures = []

    with thread_pool:
        for index in range(len(dna_samples)):
            futures.append(thread_pool.submit(thread_job, index))

        for future in futures:
            print(future.result())

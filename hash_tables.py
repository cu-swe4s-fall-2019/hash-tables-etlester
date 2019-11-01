import random
import numpy
import hash_functions
import time
import matplotlib.pyplot as plt

class LinearProbe:
    def __init__(self, N, HF):
        self.hash_function = HF
        self.N = N
        self.T = [ None for i in range(N) ]
        self.hash_plotM = [ None for i in range(N) ]
        self.hash_plot = [ None for i in range(N) ]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.hash_plot[self.M] = test_slot
                self.hash_plotM[self.M] = self.M
                self.M += 1
                return True
        return False

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            # print(self.T[hash_slot][0])
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                print(self.T[test_slot][1])
                return self.T[test_slot][1]
        return None

class ChainedHash:
    def __init__(self, N, HF):
        self.hash_function = HF
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        return True

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None



def main():
    #load data
    keys = []
    for l in open('rand_words.txt'):
        keys.append(str(l.rstrip().split('/n')))
    values = []
    for l in open('rand_word_values.txt'):
        values.append(str(l.rstrip().split('/n')))
        N_values = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    #run experiments with different N values
    LP_h_ascii_run_times = []
    LP_h_rolling_run_times = []
    for i in range(len(N_values)):
        N = N_values[i]
        run_name = 'LP_h_ascii'
        LP = LinearProbe(N, hash_functions.h_ascii)
        t0 = time.time()
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            LP.add(key,value)
        t1 = time.time()
        x = LP.hash_plotM
        y = LP.hash_plot
        plt.scatter(x, y)
        plt.savefig(run_name + '_' + str(N) + '.png', bbox_inches='tight')
        plt.close()
        LP_h_ascii_run_times.append(t1 - t0)


        run_name = 'LP_h_rolling'
        LP = LinearProbe(N, hash_functions.h_rolling)
        t0 = time.time()
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            LP.add(key,value)
        t1 = time.time()
        x = LP.hash_plotM
        y = LP.hash_plot
        plt.scatter(x, y)
        plt.savefig(run_name + '_' + str(N) + '.png', bbox_inches='tight')
        plt.close()
        LP_h_rolling_run_times.append(t1 - t0)

    print('LP_h_ascii_run_times: ' + str(LP_h_ascii_run_times))
    print('LP_h_rolling_run_times: ' + str(LP_h_rolling_run_times))

    #plot run time vs Hash table size for LP_h_ascii
    x = N_values
    y = LP_h_ascii_run_times
    plt.scatter(x, y)
    plt.savefig('LP_h_ascii_run_times_vs_hashtable_size.png', bbox_inches='tight')
    plt.close()

    x = N_values
    y = LP_h_rolling_run_times
    plt.scatter(x, y)
    plt.savefig('LP_h_rolling_run_times_vs_hashtable_size.png', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    main()

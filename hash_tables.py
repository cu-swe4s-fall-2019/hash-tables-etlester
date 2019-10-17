import hash_functions

class LinearProbe:
    def __init__(self, N, HF):
        self.hash_function = HF
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                print(self.T)
                return True
        return False

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                print(self.T)
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
        print(self.T)
        self.M += 1
        return True

    def search(self, key):
        hash_slot = self.hash_function(key, self.N)
        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None



def main():
    key = 'cat'
    value = 9
    key2 = 'cat'
    value2 = 7
    size = 1000

    LP = LinearProbe(1000, hash_functions.h_rolling)
    LP.add(key, value)
    LP.add(key2, value2)
    print("Break")
    CH = ChainedHash(1000, hash_functions.h_rolling)
    CH.add(key, value)
    CH.add(key2, value2)
    CH.search(key2)

if __name__ == '__main__':
    main()

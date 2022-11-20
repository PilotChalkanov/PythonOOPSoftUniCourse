class dictionary_iter:
    def __init__(self,dictionary = {}):
        self.dictionary = dictionary
        self.ind = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.ind == len(self.dictionary):
            raise StopIteration
        k = list(self.dictionary.items())[self.ind]
        self.ind += 1
        return k


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
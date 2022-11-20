class sequence_repeat:
    def __init__(self,text:str, count:int):
        self.text = text
        self.count = count
        self.stopper = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        new_idx = self.idx % len(self.text)
        ch = self.text[new_idx]
        self.idx +=1
        self.count -=1
        return ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
class take_skip:

    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.value = 0
    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        result = self.value
        if self.count == -1:
            raise StopIteration
        self.value += self.step
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if len(self.data) < self.capacity:
           self.data.append(item)
        else:
           self.data.pop(self.index)
           self.data.insert(self.index, item)
           if self.index < self.capacity - 1:
               self.index += 1
           else:
               self.index = 0       

    def get(self):
        return self.data
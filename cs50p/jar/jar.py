class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or isinstance(capacity, float):
            raise ValueError('Invalid Capacity')
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if (self.size + n) > 12:
            raise ValueError('Too many cookies')
        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError('Not enough cookies')
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)
    print(jar.capacity)




if __name__ == '__main__':
    main()

class IterableWithGenerator:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for item in self.iterable:
            yield item


my_list = [1, 2, 3, 4, 5]
my_iterable = IterableWithGenerator(my_list)

for item in my_iterable:
    print(item)

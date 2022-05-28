# class MinStack:
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.ds = [None]
#
#     def push(self, val: int) -> None:
#         self.ds.append(val)
#
#     def pop(self) -> None:
#         self.ds.pop()
#
#     def top(self) -> int:
#         return self.ds[-1]
#
#     def get_min(self) -> int:
#         return min(self.ds)


class MinStack:
    def __init__(self):
        self.ds = []
        self.min = []

    def push(self, val: int) -> None:
        self.ds.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            if val <= self.min[-1]:
                self.min.append(val)

    def pop(self) -> None:
        if len(self.ds) != 0:
            e = self.ds.pop()
            if e == self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        if len(self.ds) != 0:
            return self.ds[-1]

    def get_min(self) -> int:
        if len(self.ds) != 0:
            return self.min[-1]


if __name__ == '__main__':
    my_stack = MinStack()
    print(my_stack.top(), end=', ')
    print(my_stack.get_min(), end=', ')
    my_stack.pop()
    my_stack.push(-1)
    my_stack.push(3)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top(), end=', ')
    my_stack.pop()
    my_stack.push(-2)
    print(my_stack.get_min(), end=', ')
    print(my_stack.top())

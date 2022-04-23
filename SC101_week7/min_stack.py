class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass


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

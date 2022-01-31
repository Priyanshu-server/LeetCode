class MyQueue:

    def __init__(self):
        self.inn = []
        self.out = []

    def push(self, x: int) -> None:
        self.inn.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if not self.out:
            if len(self.inn) == 1:
                return self.inn.pop()
            self._load_out()
        return self.out.pop()

    def _load_out(self):
        if self.out:
            raise Exception("_load_out called when out stack had values in it")
        while self.inn:
            self.out.append(self.inn.pop())

    def peek(self) -> int:
        if not self.out:
            if len(self.inn) == 1:
                return self.inn[0]
            self._load_out()
        return self.out[-1]

    def empty(self) -> bool:
        return len(self.inn) == 0 and len(self.out) == 0



obj  = MyQueue()
obj.push(12)
param_2 = obj.pop()
obj.push(13)
param_3 = obj.peek()
# param_4 = obj.empty()

print(param_2,param_3,sep = "\n")
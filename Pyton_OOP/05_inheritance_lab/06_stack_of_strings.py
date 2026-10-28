class Stack:

    def __init__(self):
        self.data: list[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str | None:
        if self.data:
            return self.data.pop()

    def top(self) -> str | None:
        if self.data:
            return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return f"[{', '.join(reversed(self.data))}]"


test_data = Stack()

test_data.push("a")
test_data.push("b")
test_data.push("c")
test_data.push("d")

print(test_data)

test_data.push("z")
print(test_data)

removed = test_data.pop()
print(removed)

print(test_data.top())
print(test_data.is_empty())
print(test_data)
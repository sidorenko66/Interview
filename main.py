class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return not bool(self.data)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)


def is_balanced(text):

    for element in text:
        if element in '([{':
            stack.push(element)
        elif stack.isEmpty():
            return "Несбалансированно"
        elif element == ')':
            if stack.peek() == '(':
                stack.pop()
            else:
                return "Несбалансированно"
        elif element == ']':
            if stack.peek() == '[':
                stack.pop()
            else:
                return "Несбалансированно"
        elif element == '}':
            if stack.peek() == '{':
                stack.pop()
            else:
                return "Несбалансированно"
    return "Сбалансированно"


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push('1 elenent')
    print(stack.peek())
    print(stack.size())
    print(stack.isEmpty())
    stack.pop()
    print(stack.isEmpty())
    print(stack.size())

    print('START 2 TASK')

    print(is_balanced('(((([{}]))))'))
    print(is_balanced('[([])((([[[]]])))]{()}'))
    print(is_balanced('{{[()]}}'))
    print(is_balanced('}{}'))
    print(is_balanced('{{[(])]}}'))
    print(is_balanced('[[{())}]'))

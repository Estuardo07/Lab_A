class Simbolo:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class Concat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a}.{self.b})'


class Or():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'({self.a}|{self.b})'


class Kleene():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}*'


class Plus():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}+'


class SignoInt():
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return f'{self.a}?'


class Expresion():
    def __init__(self, a, b=None):
        self.a = a
        self.b = b

    def __repr__(self):
        if self.b != None:
            return f'{self.a}{self.b}'
        return f'{self.a}'

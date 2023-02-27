from tokens import Token, TipoDeToken

SIMBOLOS = 'abcdefghijklmnopqrstuvwxyz0123456789.,:;"-/'


class Lector:
    def __init__(self, string: str):
        self.string = iter(string.replace(' ', ''))
        self.input = set()
        self.Next()

    def Next(self):
        try:
            self.curr_char = next(self.string)
        except StopIteration:
            self.curr_char = None

    def CrearTokens(self):
        while self.curr_char != None:

            if self.curr_char in SIMBOLOS:
                self.input.add(self.curr_char)
                yield Token(TipoDeToken.PARENT_IZQ, '(')
                yield Token(TipoDeToken.SIMBOLO, self.curr_char)

                self.Next()
                agregarParentesis = False

                while self.curr_char != None and \
                        (self.curr_char in SIMBOLOS or self.curr_char in '*+?'):

                    if self.curr_char == '*':
                        yield Token(TipoDeToken.KLEENE, '*')
                        yield Token(TipoDeToken.PARENT_DER, ')')
                        agregarParentesis = True

                    elif self.curr_char == '+':
                        yield Token(TipoDeToken.PLUS, '+')
                        yield Token(TipoDeToken.PARENT_DER, ')')
                        agregarParentesis = True

                    elif self.curr_char == '?':
                        yield Token(TipoDeToken.SIGNO_INT, '?')
                        yield Token(TipoDeToken.PARENT_DER, ')')
                        agregarParentesis = True

                    elif self.curr_char in SIMBOLOS:
                        self.input.add(self.curr_char)
                        yield Token(TipoDeToken.CONCAT)
                        yield Token(TipoDeToken.SIMBOLO, self.curr_char)

                    self.Next()

                    if self.curr_char != None and self.curr_char == '(' and agregarParentesis:
                        yield Token(TipoDeToken.CONCAT)

                if self.curr_char != None and self.curr_char == '(' and not agregarParentesis:
                    yield Token(TipoDeToken.PARENT_DER, ')')
                    yield Token(TipoDeToken.CONCAT)

                elif not agregarParentesis:
                    yield Token(TipoDeToken.PARENT_DER, ')')

            elif self.curr_char == '|':
                self.Next()
                yield Token(TipoDeToken.OR, '|')

            elif self.curr_char == '(':
                self.Next()
                yield Token(TipoDeToken.PARENT_IZQ)

            elif self.curr_char in (')*+?'):

                if self.curr_char == ')':
                    self.Next()
                    yield Token(TipoDeToken.PARENT_DER)

                elif self.curr_char == '*':
                    self.Next()
                    yield Token(TipoDeToken.KLEENE)

                elif self.curr_char == '+':
                    self.Next()
                    yield Token(TipoDeToken.PLUS)

                elif self.curr_char == '?':
                    self.Next()
                    yield Token(TipoDeToken.SIGNO_INT)

                # Finally, check if we need to add an CONCAT token
                if self.curr_char != None and \
                        (self.curr_char in SIMBOLOS or self.curr_char == '('):
                    yield Token(TipoDeToken.CONCAT, '.')

            else:
                raise Exception(f'Entrada Invalida: {self.curr_char}')

    def get_simbolos(self):
        return self.input

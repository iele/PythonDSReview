class Stack(object):
    @staticmethod
    def expr(l):
        try:
            s = []
            for i in l:
                if i not in ['+', '-', '*', '/']:
                    s.append(i)
                else:
                    a = s.pop()
                    b = s.pop()
                    if i == '+':
                        a = str(int(b)+int(a))
                    if i == '-':
                        a = str(int(b)-int(a))
                    if i == '*':
                        a = str(int(b)*int(a))
                    if i == '/':
                        a = str(int(b)/int(a))
                    s.append(a)
            return s[0]
        except Exception:
            return None

    @staticmethod
    def expr_convert(l):
        s = []
        e = []
        for i in l:
            if i in ['+', '-', '*', '/']:
                s.append(i)
            else:
                e.append(i)
        s.reverse()
        return e + s

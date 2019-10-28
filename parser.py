from exp import Val, Add, Sub, Mul, Div

'''
def parse(s: str):
    num = int(s)
    return Val(num)

e = parse("123")
print(e)

s = "123+456"
pos = s.find('+')
print('pos',pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s, s1, s2)


def parse(s: str):
    pos = s.find('+')
    if pos == -1:
        num = int(s)
        return Val(num)
    else:
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(Val(int(s1)), Val(int(s2)))
'''

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Add(parse(s1),parse(s2))

    if s.find('*') > 0:
        pos = s.find('*')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Mul(parse(s1),parse(s2))
    
    if s.find('-') > 0:
        pos = s.find('-')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Sub(parse(s1),parse(s2))

    if s.find('/') > 0:
        pos = s.find('/')
        s1 = s[0:pos]
        s2 = s[pos+1:]
        return Div(parse(s1),parse(s2))

    return Val(int(s))

e = parse("1*2+3")
print(e, e.eval())

e = parse("1+2*3")
print(e, e.eval())
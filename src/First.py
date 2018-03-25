records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
# Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)
print("........................")
def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m



print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, 10, clip=0))
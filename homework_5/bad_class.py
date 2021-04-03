class BadClass:

    def __init__(self, val=0):
        self.val = val

    # def __hash__(self):
    #     return hash(self.val)
    #
    # def __eq__(self, other):
    #     return self.val == other.val


bad = BadClass()

even_worse = {bad}

assert (bad in even_worse)

bad.val += 1

assert (bad in even_worse)

print('yeah, we good!')

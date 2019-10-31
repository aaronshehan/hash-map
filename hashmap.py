# emulation of dynamic hash maps - similar to dict in Python
import time


class hashmap():
    def __init__(self):
        self.H = [[]] * 4
        self.ctr = 0

    def add(self, k, v):
        h = hash(k) % len(self.H)
        vs = self.H[h]

        if not vs:  # self.H[h] is empty
            vs = [(k, v)]       # array of tuples
        else:       # self.H[h] not empty
            found = False
            for i in range(len(vs)):  # checking chain for key
                if vs[i][0] == k:   # key found in chain
                    found = True
                    vs[i][1] = v    # update value
                    break
            if not found:
                vs.append((k, v))   # add new tuple to chain
        self.ctr += 1
        self.H[h] = vs
        self.resize()

    def get(self, k):
        h = hash(k) % len(self.H)
        vs = self.H[h]
        for i in range(len(vs)):
            if vs[i][0] == k:
                return vs[i][1]
        return None

    def resize(self):
        if self.ctr / len(self.H) >= .75:
            self.ctr = 0
            temp = self.H
            self.H = [[]] * len(temp) * 2

            for i in range(len(temp)):
                vs = temp[i]
                if not vs:
                    continue
                else:
                    for j in range(len(vs)):
                        self.add(vs[j][0], vs[j][1])
        elif self.ctr / len(self.H) <= .1:
            self.ctr = 0
            temp = self.H
            self.H = [[]] * (len(temp) // 2)

            for i in range(len(temp)):
                vs = temp[i]
                if not vs:
                    continue
                else:
                    for j in range(len(vs)):
                        self.add(vs[j][0], vs[j][1])
            return
        else:
            return

    def remove(self, k):
        h = hash(k) % len(self.H)
        vs = self.H[h]
        if not vs:
            return
        where = -1
        for i in range(len(vs)):
            if vs[i][0] == k:
                where = i
                break
        if where >= 0:
            vs.pop(where)
        self.ctr -= 1
        self.resize()

    def __str__(self):
        # return str(self.H)
        buf = ['[\n']
        i = 0
        for kvs in self.H:
            if kvs:
                buf.append(str(i) + ":")
                for kv in kvs:
                    buf.append(str(kv))
                buf.append("\n")
            i += 1
        buf.append(']')
        return "".join(buf)

    def __getitem__(self, k):
        return self.get(k)

    def __setitem__(self, k, v):
        self.add(k, v)


def t1():
    d = hashmap()
    d.add('hello', 'Joe')
    d.add("bye", 'Bill')
    d.add("howdy", 'Mary')
    d.add("cheers", 'Mike')
    d.add("so long", 'Jill')
    print(d.ctr)
    print(len(d.H))
    d.remove('hello')
    d.remove('howdy')
    d.remove('bye')
    d.remove('cheers')
    d.remove('so long')
    print(d.ctr)
    print(len(d.H))
    print(d)



t1()


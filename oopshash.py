class _Core:
    def __init__(self, bit_map, state):
        self.bit_map = bit_map
        self.state = state

    def run(self, bit_in):
        self.state ^= bit_in
        self.state ^= (self.state >> 2) + 3
        self.state ^= self.state << 1 & 0xffffffffffffffff
        i = (self.state & 63)
        return (self.bit_map & 1 << i) >> i


class _BaseHash:
    def __init__(self, data=()):
        self.prev_out_bit = 0
        self.update(data)

    def run(self, bit_in):
        b = bit_in ^ self.prev_out_bit
        for core in self.cores:
            b = core.run(b)
        self.prev_out_bit = b
        return b

    def update(self, data):
        for b in data:
            self.run(b & 128)
            self.run(b & 64)
            self.run(b & 32)
            self.run(b & 16)
            self.run(b & 8)
            self.run(b & 4)
            self.run(b & 2)
            self.run(b & 1)

    def digest(self, size):
        d = []
        for _ in range(size):
            d.append(self.run(0) << 7 |
                     self.run(0) << 6 |
                     self.run(0) << 5 |
                     self.run(0) << 4 |
                     self.run(0) << 3 |
                     self.run(0) << 2 |
                     self.run(0) << 1 |
                     self.run(0))
        return bytes(d)

    def hexdigest(self, size):
        return self.digest(size).hex()


class OopsHash64(_BaseHash):
    def __init__(self, data=()):
        self.cores = [_Core(6537119906076492964, 4321492311467204856)]
        super().__init__(data)


class OopsHash128(_BaseHash):
    def __init__(self, data=()):
        self.cores = [_Core(17217151553996878104, 4958870265254886210),
                      _Core(11992618003714672525, 13484184169495611559)]
        super().__init__(data)


class OopsHash256(_BaseHash):
    def __init__(self, data=()):
        self.cores = [_Core(2438260962070730005, 7002575353325696708),
                      _Core(9279639784425646158, 2955146194857127575),
                      _Core(15353015120846490598, 1608773053241766879),
                      _Core(5139394705560508351, 8586000595181437306)]
        super().__init__(data)


class OopsHash512(_BaseHash):
    def __init__(self, data=()):
        self.cores = [_Core(15453634848838471120, 15235314905778949920),
                      _Core(15470291087738198158, 8594022745868063392),
                      _Core(11182472847644109763, 5367483418940019477),
                      _Core(15921683076584721056, 403620351650362107),
                      _Core(10720959227532343208, 5145870254053317264),
                      _Core(12463544872386195014, 11091957590084272415),
                      _Core(6596814176719301780, 17310142033595355372),
                      _Core(14211382655899701370, 18051728685003822369)]
        super().__init__(data)

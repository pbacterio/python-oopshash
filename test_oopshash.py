import unittest

from oopshash import *


class TestOopsHash(unittest.TestCase):

    def test_right_bitshift(self):
        self.assertEqual(0xffffffffffffffff >> 4, 0xfffffffffffffff)

    def test_left_bitshift(self):
        self.assertEqual(0xffffffffffffffff << 4 & 0xffffffffffffffff, 0xfffffffffffffff0)

    def test_hash64(self):
        self.assertEqual(OopsHash64().hexdigest(10), '62541a026c35c741a832')
        self.assertEqual(OopsHash64(b'\x00\x00\x00').hexdigest(10), '026c35c741a832ad6a42')
        self.assertEqual(OopsHash64(b'\x00\x08\x00').hexdigest(10), 'a07a8b290ab545d5f4eb')
        self.assertEqual(OopsHash64(b'\xff\xff\xff').hexdigest(10), '7c7645a0a28d199d3fea')

    def test_hash128(self):
        self.assertEqual(OopsHash128().hexdigest(10), 'b00a9f1042c89ac40996')
        self.assertEqual(OopsHash128(b'\x00\x00\x00').hexdigest(10), '1042c89ac409969c06c1')
        self.assertEqual(OopsHash128(b'\x00\x08\x00').hexdigest(10), '9984938a311ced838e86')
        self.assertEqual(OopsHash128(b'\xff\xff\xff').hexdigest(10), '583750834683f97f0595')

    def test_hash256(self):
        self.assertEqual(OopsHash256().hexdigest(10), 'abd9e8823a31877b913b')
        self.assertEqual(OopsHash256(b'\x00\x00\x00').hexdigest(10), '823a31877b913b09b0c7')
        self.assertEqual(OopsHash256(b'\x00\x08\x00').hexdigest(10), 'bafc4479dedd419e33e3')
        self.assertEqual(OopsHash256(b'\xff\xff\xff').hexdigest(10), '7882153db623279ee69e')

    def test_hash512(self):
        self.assertEqual(OopsHash512().hexdigest(10), '935f0d3d0e21ef9079ce')
        self.assertEqual(OopsHash512(b'\x00\x00\x00').hexdigest(10), '3d0e21ef9079ce5fec9a')
        self.assertEqual(OopsHash512(b'\x00\x08\x00').hexdigest(10), 'f4cdfd936fb60bc1443f')
        self.assertEqual(OopsHash512(b'\xff\xff\xff').hexdigest(10), '1973d51be8eae1e1b308')


if __name__ == '__main__':
    unittest.main()

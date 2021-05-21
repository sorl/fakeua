import unittest
import uas


class UasTest(unittest.TestCase):
    def test_chrome(self):
        self.assertIsInstance(uas.chrome(), str)

    def test_firefox(self):
        self.assertIsInstance(uas.firefox(), str)

    def test_bot(self):
        self.assertIsInstance(uas.bot(), str)

    def test_os(self):
        self.assertIsInstance(uas._os(), str)

    def test_BOTS(self):
        self.assertIsInstance(uas.BOTS, tuple)
        [self.assertIsInstance(bot, str) for bot in uas.BOTS]

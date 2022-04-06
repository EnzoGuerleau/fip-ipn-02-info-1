from argparse import ArgumentTypeError
import unittest
import chat

def ReturnOne():

    return 1

class TesterMonChat(unittest.TestCase):
    def test_constructor(self):
        monchat = chat.Chat("toto",18)
        self.assertEqual(monchat._nom, "toto")
        self.assertEqual(monchat.classification, chat.Classification.MAMIFERE)
        self.assertIsInstance(monchat.classification, chat.Classification)
        self.assertEqual(monchat._isCute, True)
        self.assertEqual(monchat._age, 18)
    
    def test_constructor_argumenttypeerror_name(self):
        self.assertRaises(ArgumentTypeError, chat.Chat, 2)
        self.assertRaises(ArgumentTypeError, chat.Chat, [1,"2",3,4])
        self.assertRaises(ArgumentTypeError, chat.Chat, {"1":1})
        self.assertRaises(ArgumentTypeError, chat.Chat, (1,2,3))
    
    def test_constructor_argumenttypeerror_age(self):
        self.assertRaises(ArgumentTypeError, chat.Chat, "toto", "")
        self.assertRaises(ArgumentTypeError, chat.Chat, "toto", [])
        self.assertRaises(ArgumentTypeError, chat.Chat, "toto", {})
        self.assertRaises(ArgumentTypeError, chat.Chat, "toto", ())


if __name__ == '__main__':
    unittest.main()

import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_push(self):
        stack = Stack(5)
        stack.push(11)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 11)
        stack.push(12)
        self.assertEqual(stack.size(), 2)
        stack.push(13)
        self.assertEqual(stack.size(), 3)
        stack.push(14)
        self.assertEqual(stack.size(), 4)
        stack.push(15)
        self.assertEqual(stack.size(), 5)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.peek(),15)
        self.assertRaises(IndexError, stack.push, 16)
        self.assertEqual(stack.size(), 5) # Make sure trying to push on full stack didn't have an effect
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.peek(), 15)

    def test_simple(self):
        stack = Stack(5)
        stack.push(0)       #[0,none.none,none.none]
        self.assertEqual(stack.peek(),0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    #Additional testcases for Array/List

    def test_if_empty(self):
        s1 = Stack(3)  #[none,none,none]
        self.assertTrue(s1.is_empty())  # Should be True

    def test_if_not_empty(self):
        s1 = Stack(4)  #[none,none,none,none]
        s1.push(2)     #[2,none,none,none]
        s1.push(3)      #[2,3,none,none]
        s1.push(4)      #[2,3,4,none]
        self.assertFalse(s1.is_empty())  # this is saying that the statement that the string is empty is false

    def test_if_full(self):
        s1 = Stack(3)      #[none,none,none]
        s1.push(5)  #[5,none,none]
        s1.push(4)  #[5,4,none]
        s1.push(3)  #[5,4,3]
        self.assertTrue(s1.is_full()) #this is checking to see if its true that the stack is full

    def test_if_not_full(self):
        s1 = Stack(2)  # [none,none]
        s1.push(2)          # [2,none]
        self.assertFalse(s1.is_full())  # it is false that the stack is full

    def test_IfWeCanPush(self):
        s1 = Stack(3)  #[none,none,none]
        s1.push(2)  #[2,none]
        s1.push(3)  #[2,3]
        self.assertFalse(s1.is_full())  # it is false that the stack is full

    def test_IfWeCantPush(self):
        s1 = Stack(3)  #[none,none,none]
        s1.push(2)      #[2,none,none]
        s1.push(3)      #[2,3,none]
        s1.push(3)      #[2,3,3]
        with self.assertRaises(IndexError):
            s1.push(4)

    def test_ifWeCanPop(self):
        s1 = Stack(3)  #[none,none,none]
        s1.push(3)  #[3,none,none]
        s1.push(3)  #[3,3,none]
        s1.push(5)  #[3,3,5]
        # This gives us an array [3,3,5]
        s1.pop()    # now we have [3,3]
        s1.pop()    # now we have [3]
        self.assertFalse(s1.is_empty())
        self.assertEqual(s1.pop(),3)

    def test_ifWeCantPop(self):
        s1 = Stack(2)  # this gives us [none,none]
        with self.assertRaises(IndexError):
            s1.pop()

    def test_ifWeCanPeek(self):
        s1 = Stack(4)
        s1.push(4)
        s1.push(3)
        s1.push(5)
        s1.push(54)
        self.assertEqual(s1.peek(),54) #this statement says that if we peek at the top of the stack it should be 54

    def test_ifWeCantPeek(self):
        s1 = Stack(4)
        with self.assertRaises(IndexError):
            s1.peek()

    def test_ifWeCanSeeTheSize(self):
        s1 = Stack(5)
        s1.push(3)
        self.assertEqual(s1.size(),1)  # this statement checks that the size or number of items in the
        # stack is 1 ... [ 3,none,none,none,none] only has one item which is 3

if __name__ == '__main__':
    unittest.main()


# Bracket Validator
# Just a bracket validator, this is the link https://www.interviewcake.com/question/python3/bracket-validator

import unittest


def is_valid(code):
    # Determine if the input code is valid
    
    # We'll use a list as a stack, it's the simpler way
    stack = []
    
    # Here we have our openers and their pair
    openers = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    for c in code:
        if c in openers:
            # In case the char we are evaluating is opening a pair, we add it to stack
            stack.append(c)
        elif len(stack) > 0 and c == openers[stack[-1]]:
            # if the current character is closing the opener in the stack we just remove that
            # opener from stack
            stack.pop()
        else:
            # This is the case we find a char that is not closing anything
            # It makes no sense to keep iterating
            return False
    # And last, in case there are still brackets without closing, we return False
    return len(stack) == 0


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)

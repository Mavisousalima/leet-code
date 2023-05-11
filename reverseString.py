"""
s[::-1] creates a reversed copy of the input list s. The [::-1] slice syntax with no start or stop indices means to 
include all elements of s in reverse order.
s[:] = ... assigns the reversed copy of s back to the original list s. The [:] slice syntax means to assign to 
all elements of s, effectively replacing it with the reversed copy.
"""

from typing import List

s = ['h', 'e', 'l', 'l', 'o']


def reverseString(s: List[str]) -> None:
    # s[:] = s[::-1]
    s.reverse()

# s.reverse()


reverseString(['h', 'e', 'l', 'l', 'o'])

print(s)

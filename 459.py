"""
459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""

def solve(s):
    i = 1
    while i < len(s):
        if s[i] == s[0]:
            if len(s) % (i) == 0:
                if s[:i] * (len(s)//i) == s:
                    return True
        i += 1
    return False
print(solve("abcabcabcabc"))
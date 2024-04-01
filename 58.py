#58 Length of Last Word

def lengthOfLastWord(s):
        words = s.strip().split(" ")
        return len(words[-1])

print(lengthOfLastWord("luffy is still joyboy"))
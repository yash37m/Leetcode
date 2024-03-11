# 791. Custom Sort String

from collections import Counter
def customSortString( order: str, s: str) :
    if len(order) > 1 and len(s) > 1:
        counted = Counter(s)
        x = ""
        for i in order:
                if i in counted:
                    x += i * counted.pop(i)

        for i in counted:
                x += i * counted[i]

        return x   
    else:
          return s  
        
print(customSortString("bcafg","abcd"))
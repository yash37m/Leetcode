# Maximize Happiness of Selected Children

def maximumHappinessSum(happiness, k):
    happiness.sort()
    sum = 0
    for i in range(k):
        print(happiness,i)
        x = happiness.pop() - i
        if x > 0:
            sum += x
    return sum

print(maximumHappinessSum([1,1,1,1],2))

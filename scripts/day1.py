import re

puzzle = open('../assets/day1puzzle.txt')
lines = puzzle.readlines()
result = []


# reverses all strings passed into it
def reverse(text):
    return text[::-1]


# for each line search for a digit then reverse and search again
for line in lines:
    x = re.search("[0-9]", line).group()
    y = re.search("[0-9]", reverse(line)).group()
    # appends result list by combining numbers as string then casting to int
    result.append(int(str(x) + str(y)))

# sums the result list
print(sum(result))

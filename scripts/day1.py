import re

puzzle = open('../assets/day1puzzle.txt')
lines = puzzle.readlines()
result_1 = []
result_2 = []


# reverses all strings passed into it
def reverse(text):
    return text[::-1]


def text2int(text):
    match text:
        case 'one':
            text = 1
        case 'two':
            text = 2
        case 'three':
            text = 3
        case 'four':
            text = 4
        case 'five':
            text = 5
        case 'six':
            text = 6
        case 'seven':
            text = 7
        case 'eight':
            text = 8
        case 'nine':
            text = 9
    return text


# for each line search for a digit then reverse and search again
for line in lines:
    x = re.search("[0-9]", line).group()
    y = re.search("[0-9]", reverse(line)).group()
    # appends result list by combining numbers as string then casting to int
    result_1.append(int(str(x) + str(y)))

# sums the result list
print(sum(result_1))

# part 2
for line in lines:
    # checks for plain text in a similar fashion  to part 1
    x = re.search("[0-9]|one|two|three|four|five|six|seven|eight|nine", line).group()
    y = reverse(re.search("[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin", reverse(line)).group())
    # checks if x or y are strings and if so sends them off to be converted
    if isinstance(x, str):
        x = text2int(x)
    if isinstance(y, str):
        y = text2int(y)
    # appends result list by combining numbers as string then casting to int
    result_2.append(int(str(x) + str(y)))

print(sum(result_2))

import re
inputLines = []
with open("input.txt") as fp:
    for line in fp:
        splitRow = list(map(int, re.split("\s+", line.strip())))
        minVal = int(min(splitRow))
        maxVal = int(max(splitRow))
        diff = maxVal - minVal
        inputLines.append(diff)

print(inputLines)
print("sum: ", sum(inputLines))

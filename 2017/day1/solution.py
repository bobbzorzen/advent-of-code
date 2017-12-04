inputData = ""
with open("input.txt") as fp:
    inputData = fp.read().strip()

def solve(testdata):
    stringSum = int(testdata[0]) if testdata[0] == testdata[-1] else 0
    for i in range(1, len(testdata)):
        if testdata[i-1] == testdata[i]:
            stringSum += int(testdata[i])
    return stringSum

print(solve(inputData))

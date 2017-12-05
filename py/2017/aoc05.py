f = open("input05.txt")
s = ""
content = f.read()
arr = map(lambda x: int(x), filter(lambda x : len(x) > 0, content.split('\n')))

numSteps = 0
currentIndex = 0

while currentIndex >= 0 and currentIndex < len(arr):
    numSteps += 1
    jump = arr[currentIndex]
    arr[currentIndex] = jump - 1 if jump >= 3 else jump + 1
    currentIndex += jump

print(numSteps)
string = input()
array = list(string)
if string.find("f") == -1:
    print(-2)
    exit

count = 0
index = 0
for item in array:
    if item == "f":
        count = count + 1
        if count == 2:
            print(index)
    index += 1

if count == 1:
    print(-1)
    exit

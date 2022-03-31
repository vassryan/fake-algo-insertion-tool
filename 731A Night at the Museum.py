stringinput = list("a" + input())

array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n = len(stringinput) 
outputsum = 0
for i in range(1,n):
    character1 = stringinput[i-1]
    character2 = stringinput[i]
    array_diff = int(array.index(character2)) - int(array.index(character1))
    if abs(array_diff) > 13:
        outputsum = outputsum + abs((26 - abs(array_diff)))
    else:
        outputsum = outputsum + abs(array_diff)
print(outputsum)



x = "outside function - global"

def func():
    x = "inside function - local"
    print(x)
    for i in range(2):
        x = "inside for loop - local"
        print (x, " iteration : ", i)

print(x)
func()
print(x)

x = "global"

def modify_global():
    global x
    print("Before modification: ", x)
    x = "modified global"
    print("After modification: ", x)

print(x)
modify_global()
print(x)

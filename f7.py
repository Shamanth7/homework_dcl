a=100 # goble variablelpl
def display():
    global a #use the global key word
    a=a+22 #we are modifing the goble variable inside the functon
    print(" display function body")
    print("inside the function",a)
display()
a=a+23
print("ouside the function",a)
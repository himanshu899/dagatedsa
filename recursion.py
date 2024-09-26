# Need to find relationship between input and the time
# The running time of a program is not the correct measure of complexity as it can vary from machine to machine. Machine with greater ram, processor can run the same piece of code faster
# And with increase in the input we can't exactly get how much time growth is there because of varying system specifications
def rec():
    a = [1,2,3,4,5]
    print(id(a[4]) - id(a[0]))
    print("HELLO")

rec()

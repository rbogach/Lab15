var = int(input("Enter a number greater than 0: "))


def checkvalueNow(valuetocheck):
    assert (type(valuetocheck) is int), "You must enter a number"
    assert (valuetocheck > 0), "Value entered must be greater than 0"
    if valuetocheck > 4:
        print("Value is greater than 4")


    checkvalueNow(var)

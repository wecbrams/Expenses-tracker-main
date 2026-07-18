for x in range(10):
    if x%20==0: # 0123456789
        print("twist")
    elif x%15==0:
        pass
    elif x%5==0:
        print("fizz")
    elif x%3==0:
        print("buzz")
    else:
        print(x)
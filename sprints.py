def MyFunc(*li):
    sumEven = 0
    numEvenInt = 0
    maxFloat = -10e9
    count = len(li)
    for i in li:
        if type(i) == int:
            count -= 1
            if i % 2 == 0:
                sumEven+=i
                numEvenInt+=1

        elif type(i) == float:
            count -= 1
            if i > maxFloat:
                maxFloat = i

    if count == len(li):
        return 0

    if numEvenInt == 0:
        if maxFloat == -10e9:
            return str("There was no even integers in the list"),str("There was no decimals in the list")
        return str("There was no even integers in the list"), maxFloat

    if maxFloat == -10e9:
        return sumEven/numEvenInt, str("There was no decimals in the list")

    return sumEven/numEvenInt, maxFloat

a,b=MyFunc("ksls",9,7,8,12,20,7.7,64,88,9.4,84,10.55)
print(a)
print(b)




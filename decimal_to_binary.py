
def toBinary(decimalNumber :int):
    timesPowerOfNumber = []
    binaryNumber=[]
    divide = True
    powerLevel=0

    while (divide):
        if (2 ** powerLevel ) < decimalNumber :
            timesPowerOfNumber.append(2 ** powerLevel)
            powerLevel+=1
        else:
            divide = False
    remainder = decimalNumber
    

    for i in range(len(timesPowerOfNumber),0,-1):
        binaryNumber.append(remainder // timesPowerOfNumber[i-1] )
        remainder = remainder % timesPowerOfNumber[i-1]
        
    return binaryNumber

output = toBinary(325)
print(output)
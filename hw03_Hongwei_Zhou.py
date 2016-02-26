import binascii

def convertToBinary(n):
    n = '{0:08b}'.format(int(n))
    print(n)

def convertACII(aList):
    for i in range(0,len(aList)):
        aList[i] = binascii.unhexlify((hex(aList[i]))[2:])
        aList[i] = aList[i].decode("utf-8")
    aList = ''.join(aList)
    print(aList)

def convertBtoH(n):
    output = hex(int(n,2))
    print(output)
        
def convertOtoD(n):
    n = int(n)
    output = 0
    count = 0
    while(n != 0):
        output += (n%10)*(8**count)
        n = int(n/10)
        count+=1
    print(output)

convertToBinary(input("Enter an integer to convert to binary:"))
convertACII([0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x57])
convertBtoH(input("Enter Binary to convert to Hexdecimal:"))
convertOtoD(input("Enter Octal to convert to decimal: "))

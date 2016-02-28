
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

def disassemble(operation_code):
    for content in operation_code:
        if int(content) == 000:
            print("HLT")
        elif int(content) == 901:
            print("INP")
        elif int(content) == 902:
            print("OUT")
        else:
            print(INS_REF[int(int(content)/100)]+" "+str(int(content)%100).zfill(2))
    pass

def main():
    inputLines = []
    ifDone = 0
    while ifDone == 0:
        line = input("Please Enter Code Line By Line, Enter 000 To Finish:\n")
        if line == "000":
            inputLines.append(line)
            ifDone = 1
        else:
            inputLines.append(line)
    disassemble(inputLines)
    pass

if __name__ == "__main__":
    main()

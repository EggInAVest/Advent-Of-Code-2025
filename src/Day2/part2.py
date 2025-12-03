
def main():
    with open("input.txt", "r") as file1:
        content = file1.read()
        res = 0

        """Splitting the inputs into pairs into a list"""
        for pair in content.split(","):
            first_str, last_str = pair.split("-")
            first = int(first_str)
            last = int(last_str)
            for ID in range(first, last+1):
                stringID = str(ID)
                if invalidID(stringID):
                    res += int(stringID)
    print(res)

def invalidID(stringID):
        stringLen = len(stringID)
        for patternSize in range(1, stringLen // 2 + 1):
             if stringLen % patternSize != 0:
                  continue
             block = stringID[:patternSize]
             res = block
             number = stringLen // patternSize
             for i in range(1, number):
                  res += block
             if res == stringID:
                  return True
        return False



if __name__=="__main__":
    main()


def main():
    with open("input.txt", "r") as file1:
        
        result = 0
        content = file1.readlines()
        for line in content:
            largestFirst = 0
            largestBoth = 0
            for i, curr in enumerate(line):
                if curr.isdigit():
                    currNum = int(curr)
                    if currNum > largestFirst:
                        largestFirst = currNum
                        for j, next in enumerate(line[i+1:], start=i+1):
                            fullNumStr = curr + next
                            if int(fullNumStr) > largestBoth:
                                largestBoth = int(fullNumStr)

            result += largestBoth
        print(result)
                    
                
if __name__=="__main__":
    main()
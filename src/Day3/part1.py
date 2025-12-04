
def main():
    with open("test.txt", "r") as file1:
        
        result = 0
        content = file1.readlines()
        for line in content:
            largestFirst = 0
            largestBoth = 0
            for curr, next in zip(line, line[1:]):
                if curr.isdigit() and next.isdigit():
                    currNum = int(curr)
                    nextNum = int(next)
                    fullNumStr = curr + next
                    if currNum > largestFirst:
                        largestFirst = currNum
                        if int(fullNumStr) > largestBoth:
                            largestBoth = int(fullNumStr)
                            print(largestBoth)
            result += largestBoth
        print(result)
                    
                
if __name__=="__main__":
    main()
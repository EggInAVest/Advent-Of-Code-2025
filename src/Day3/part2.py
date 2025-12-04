
def main():
    with open("input.txt", "r") as file1:
        
        result = 0
        content = file1.readlines()
        for line in content:
            line = line.strip()
            freeSlots = 12
            finalStr = ""
            lineLen = len(line)
            searchArea = line
            while freeSlots > 0:
                num = max(searchArea[:len(searchArea) - freeSlots + 1])
                searchArea = searchArea[searchArea.index(num) + 1:]
                finalStr += num
                freeSlots -= 1
            result += int(finalStr)
        print(result)
                    
                
if __name__=="__main__":
    main()
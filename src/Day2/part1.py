

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
                if (len(stringID) % 2 != 0):
                    continue
                firstpart, secondpart = stringID[:len(stringID)//2], stringID[len(stringID)//2:]
                if (firstpart == secondpart):
                    res = res + int(stringID)
    print(res)
                    
                
                
            
            
                
            
            

if __name__=="__main__":
    main()
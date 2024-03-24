arr2 = ["trances", "nectar"]
def letter_check(arr): 
    xxx = "".join(set(sorted(str.lower(arr[0]))))
    yyy = "".join(set(sorted(str.lower(arr[1]))))
    gg = 0
    while len(yyy) > gg:
       if yyy[gg] in xxx:
          gg+=1
       else:
            return False
    return True
        
    
print(letter_check(arr2))

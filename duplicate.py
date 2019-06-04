def remove_duplicates(value):
   
    result=[]
    seen=set()
    for char in value:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)   

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))

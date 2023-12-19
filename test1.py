def repeatedString(s, n):
    # Repeat the string s to have a total length of n
    L = list(s)
    L1=L*n
    count = 0
    for i in range(n):
        if L1[i]  == 'a':
            count += 1
    return count
res=repeatedString("a",1000000)
print(res)    

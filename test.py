def solution(s):
    def delete_same(s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return s[:i] + s[i+2:] if i != len(s)-1 else s[:i]
        
        return s
    
    while s != '':
        if delete_same(s) == s:
            break
        
        s = delete_same(s)

    return int(len(s) == 0)


print(solution('baabaa'))
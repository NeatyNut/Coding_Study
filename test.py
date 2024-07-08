def solution(n):
    str_n = str(n)
    new_number = 0


    for idx, i in enumerate(str_n):
        else_list = sorted(list(str_n[idx+1:]))
        if int("".join(else_list[::-1])) == int(str_n[idx+1:]):
            print(idx)
            for idx2, j in enumerate(else_list):
                if j > i:
                    break

    
            new_number = else_list[idx2]
            else_list[idx2] = i
            break

    return str_n[:idx] + new_number + "".join(else_list)

print(solution(364))
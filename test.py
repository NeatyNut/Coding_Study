zip_number = input()
zip_number_list = list(zip_number)
zip_number_list.reverse()
answer_numbers = ""
ex_numbers = ""

situation = False # False 시 붙이기
# situation = True # True 시 ex_numbers 여러번 붙이기

for i in zip_number_list:
    if i == ")":
        continue

    if i == "(":
        ex_numbers = answer_numbers
        situation = True
    else:
        if situation:
            answer_numbers = ex_numbers * int(i)
            situation = False
        else :
            answer_numbers = i + answer_numbers


print(len(answer_numbers))
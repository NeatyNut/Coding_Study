def solution(begin, target, words):
    if not target in words:
        return 0

    # 비교하기
    def compare(word, part_target):
        # 동일할 시 0 리턴
        if word == part_target:
            return 0
        
        # 다를 시
        ch_number = 0

        for idx in range(len(part_target)):
            if word[idx] != part_target[idx]:
                ch_number += 1
        return ch_number

    # 방법 찾기    
    def find_way(begin:str, target:str, words:list, result:int):
        needs = compare(begin, target)

        for word in words:
            if compare(begin, word) == 1 and compare(word, target) < needs:
                result += 1
                break
        
        part_begin = word
        part_words = [w for w in words if w != part_begin]

        if part_begin != target:
            return find_way(part_begin, target, part_words, result)
        else :
            return result
    
    return find_way(begin, target, words, 0)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
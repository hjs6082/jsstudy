import re

p = re.compile("ca.e") 
#or (^de) 일경우 ^는 문자열의 시작을 의미
# $ (de$) $는 문자열의 끝을 의미


#m = p.match("case")
#print(m.group())
# 매치되지 않으면 에러 발생
def print_match(m):
    if m:
     print(m.group()) # 일치하는 문자열 반환
     print(m.string) # 입력받은 문자열 반환
     print(m.start()) # 일치하는 문자열의 시작 index
     print(m.end()) # 일치하는 문자열의 끝 index
     print(m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("care")
# print_match(m)

# m = p.search("cafebene") # 주어진 문자열에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good cafebene cave") # 일치하는 모든것들을 리스트로 반환
print(lst)
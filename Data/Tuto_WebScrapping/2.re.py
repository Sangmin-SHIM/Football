import re

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X) ...
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X) ...
# $ (se$) : 문자열의 끝 > case, base (O) | face (X) ...

#########
# Match #
#########
# Definition : 주어진 문자열의 처음부터 일치하는지 확인 - (ex) "good case" (X) | "careless" (O)
# Match되지 않으면 에러 발생
def print_match(m):

    if m:
        print("m.group() : ",m.group(), ", mathched") # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ",m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ",m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ",m.span()) # 일치하는 문자열의 시작 / 끝 index
        print("--------------------")
        
    else:
        print("No match")
        print("--------------------")


m1= p.match("good case")
print_match(m1)

m2= p.match("careless")
print_match(m2)

##########
# Search #
##########
# Definition : 주어진 문자열 중에 일치하는게 있는지 확인 - (ex) "good case" (O) | "careless" (O)
m3= p.search("good case")
print_match(m3)

m4= p.search("careless")
print_match(m4)

###########
# findall #
###########
# Definition : 일치하는 모든 것을 리스트 형태로 반환
list = p.findall("careless cafe case calesesese")
print(list)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. list = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X) ...
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X) ...
# $ (se$) : 문자열의 끝 > case, base (O) | face (X) ...

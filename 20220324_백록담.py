letters = 'python'
print(letters[0])
print(letters[2])

string = "PYTHON"
print(string[::-1])

url = "http://sharebook.kr"
name = input("특정 문자열을 입력하시오: ")
num1 =url.rfind(name)
num2 = len(name)
print(num1)
result = url[num1:num1+num2]
print(result)

file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

file_name_second = "2020_보고서.xlsx"
print(file_name_second.startswith('2020'))

score = int(input("학점을 입력하시오: "))
if 80<score<=100 :
    print("학점: A")
elif 60<score<=80 :
    print("학점: B")
elif 40<score<=60 :
    print("학점: C")
elif 20<score<=40 :
    print("학점: D")
elif 0<score<=20 :
    print("학점: E")

cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
print(len(cook))

warn_investment_list = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
list_warn = input("투자 경고 종목을 입력하시오: ")
if warn_investment_list.count(list_warn) > 0 :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다")

list_for = [100,200,300]
for i in range(3):
    print(list_for[i]+10)

list_list = ["SK하이닉스","삼성전자","LG전자"]
for i in range(3):
    print(len(list_list[i]))


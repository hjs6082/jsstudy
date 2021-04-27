import requests
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()
# print("응답코드 : ", res.status_code) # 200이여야 정상 못가져올시 403

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제 발생 [에러코드", res.status_code, "]")

# res.raise_for_status()
# print("스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("google.html", "w", encoding="utf8") as f:
    f.write(res.text)
import re
import requests
from bs4 import BeautifulSoup
import time

url = "http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=1000"

resp = requests.get(url)
resp.encoding = 'utf8'
html = resp.text
html = re.sub(r'\s{1,2}[0-9a-f]{3,4}\s{1,2}', '', html)

soup = BeautifulSoup(html, "lxml")

# f = open(str(time.time())+".txt", 'wt', encoding='utf-8')
f = open(str(time.time())+".txt", 'wb').write(resp.content)

for member_tag in soup.select('.memberna_list dl dt a'):
    name = member_tag.text
    link = member_tag['href']

    matched = re.search(r'\d+', link)
    if matched:
        member_id = matched.group(0)
    else:
        member_id = None

    print(name.encode('cp949', 'ignore').decode('cp949'), member_id) 
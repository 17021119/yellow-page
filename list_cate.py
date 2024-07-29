import requests
from bs4 import BeautifulSoup

import file_utils

url = 'https://www.yellowpages.vn/cate.asp?page='
cate_list = []


def get_cate_page(page):
    x = requests.get(url + str(page))
    soup = BeautifulSoup(x.content, 'html.parser')

    elements = soup.find_all(class_='text-capitalize')
    cates = ''
    for ele in elements:
        cate = str(ele.get_text().split("(")[0]).strip()
        # cate = str(ele.get_text()).strip()
        # change & to %26
        cate = cate.replace("&", "%26")
        cate = cate.replace("(", "%28")
        cate = cate.replace(",", "%2C")
        cate = cate.replace(")", "%29")
        cates += cate + "\n"
    file_utils.write_file(cates, 'cate')


def get_cate_list():
    for i in range(1, 28):
        get_cate_page(i)

# get_cate_list()

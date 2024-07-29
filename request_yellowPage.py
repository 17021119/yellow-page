import time

import requests
from bs4 import BeautifulSoup

from datetime import datetime

import file_utils

# url = 'https://www.yellowpages.vn/search.asp?keyword=Vật Liệu Xây Dựng&where=Thái Nguyên'

url = 'https://www.yellowpages.vn/search.asp?keyword=Bàn Ghế Gỗ&where=Thái Nguyên'
phone_set = set()


def request_to_link(url):
    try:
        x = requests.get(url)
        soup = BeautifulSoup(x.content, 'html.parser')

        elements = soup.find_all(class_='yp_noidunglistings')
        all_data = ''
        if len(elements) > 0:
            for ele in elements:
                try:
                    tels = ele.find_all('a', href=True)
                    tel = get_phone(tels)
                    if tel == '':
                        continue
                    else:
                        if tel in phone_set:
                            continue
                        else:
                            phone_set.add(tel)
                            file_utils.write_file(tel + "\n", "phone_unique_hn")
                except Exception as e:
                    tel = ''

                try:
                    name = get_content(ele, 'fs-5 pb-0 text-capitalize')
                except Exception as e:
                    name = ''

                try:
                    links = ele.find_all('a', href=True)
                    for l in links:
                        if 'www.yellowpages.vn/lgs' in l['href']:
                            link = l['href']
                            break
                    request_detail = requests.get(link)
                    soup_detail = BeautifulSoup(request_detail.content, 'html.parser')

                    elements_details = soup_detail.find_all(class_='mt-3 h-auto clearfix')
                    year = get_year(elements_details)
                    mst = get_MST(elements_details)
                    # get year

                except Exception as e:
                    link = ''

                try:
                    nganh = get_content(ele, 'yp_nganh_text')
                except Exception as e:
                    nganh = ''

                try:
                    province = (ele.find_all_next(class_='m-0')[0].find_all_next(
                        class_='fw-semibold border-bottom border-warning')[0].getText())

                except Exception as e:
                    try:
                        province = ele.find_all_next(class_='fw-semibold')[0].getText()
                    except Exception as r:
                        province = ele.find_all_next(class_='fw-semibold')[0].getText()

                try:
                    location = (ele.find_all_next('small')[0].getText())
                    index = 0
                    isUpdate = 'Thông tin đã lâu chưa cập nhật' in location or 'Ngày cập nhật gần nhất' in location or 'Thông tin này có thể không còn chính xác' in location
                    while (isUpdate):
                        index += 1
                        location = (ele.find_all_next('small')[index].getText())
                        isUpdate = 'Thông tin đã lâu chưa cập nhật' in location or 'Ngày cập nhật gần nhất' in location or 'Thông tin này có thể không còn chính xác' in location

                except Exception as e:
                    location = ''

                all_data += concat_content(province, year, nganh, name, tel, mst, location, link, url) + "\n"
            if ("<div" in all_data):
                file_utils.write_file("error: " + url, "error")
            else:
                if all_data != '':
                    file_utils.write_file(all_data, "data_hn")

        print("done: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), " ", url)
    except Exception as e:
        file_utils.write_file(url + "\n", "error")
        print("====ERROR[" + url + "]", e)


def concat_content(*args):
    result = ''
    for arg in args:
        result += str(arg).replace(',', '-').strip() + ","
    return result


def get_phone(tels):
    try:
        for x in tels:
            text = str(x.getText().replace("(", "").replace(")", "").replace(".", " ").strip())
            if text.startswith("09") or text.startswith("03") or text.startswith("01"):
                return "'" + text
    except Exception as e:
        return ""
    return ""


def get_content(ele, class_name):
    return ele.find_next(class_=class_name).getText()


def get_MST(elements):
    for ele in elements:
        if 'Mã số thuế' in ele.getText():
            return str(ele.getText()).replace("\n", "").replace("Mã số thuế:", "").strip()


def get_year(elements):
    for ele in elements:
        if 'Năm thành lập' in ele.getText():
            return str(ele.getText()).replace("\n", "").replace("Năm thành lập:", "").strip()


def read_phone_set():
    try:
        phone_list = file_utils.read_phone_set()
        if len(phone_list) > 0:
            for x in phone_list:
                if x != '':
                    phone_set.add(x)
        print("phone set:", len(phone_set))
    except Exception as e:
        print("read_phone_set not exitst")


if __name__ == '__main__':
    try:
        index = int(file_utils.read_file("index_count"))
    except:
        index = 0
    data = file_utils.read_link_all_list()
    read_phone_set()
    size = len(data)
    while index < size:
        print("start: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), index, ", url: ", data[index])
        request_to_link(data[index])
        file_utils.write_w(index, "index_count")
        index += 1

URL_BASE = "D:/me/py/yellowPage/"


def write_file(data, file_name):
    f = open(URL_BASE + file_name + ".txt", 'a', encoding='utf-8')
    # data_exists = read_file(file_name)
    # if len(data_exists) == 0:
    #     # f.write("Tỉnh,Ngành,Tên,Tel,Phone,Địa chỉ,gmail,web\n")
    #     f.write("Tỉnh,Ngành,Tên,Tel,Địa chỉ,\n")
    f.write(str(data))

def write_w(data, file_name):
    f = open(URL_BASE + file_name + ".txt", 'w', encoding='utf-8')
    # data_exists = read_file(file_name)
    # if len(data_exists) == 0:
    #     # f.write("Tỉnh,Ngành,Tên,Tel,Phone,Địa chỉ,gmail,web\n")
    #     f.write("Tỉnh,Ngành,Tên,Tel,Địa chỉ,\n")
    f.write(str(data))


# def write_file(data, file_name):
#     f = open(URL_BASE + file_name + ".csv", 'a',encoding='utf-8')
#     data_exists = read_file(file_name)
#     if len(data_exists) == 0:
#         f.write("Tỉnh,Ngành,Tên,Tel,Phone,Địa chỉ,gmail,web")
#
#     f.write(str(data) + "\n")


def read_file(file_name):
    f = open(URL_BASE + file_name + ".txt", 'r', encoding='utf-8')
    return f.read()

def read_phone_set():
    data = read_file("phone_unique")
    datas = data.split("\n")
    return datas
def read_cate_list():
    data = read_file("cate")
    datas = data.split("\n")
    return datas


def read_link_all_list():
    data = read_file("link_all")
    datas = data.split("\n")
    return datas


def init_all_link():
    cates = read_cate_list()
    # province = ['Thái Nguyên', 'Bắc Ninh', 'Bắc Giang', 'Phú Thọ', 'Hà Nam', 'Hải Dương']
    # province = 'Vĩnh Phúc'
    # for cate in cates:
    #     url = 'https://www.yellowpages.vn/search.asp?keyword=' + cate + '&where=' + province + '\n'
    #     write_file(url, 'link_all')
    provinces = ['Nam Định', 'Ninh Bình']
    for province in provinces:
        for cate in cates:
            url = 'https://www.yellowpages.vn/search.asp?keyword=' + cate + '&where=' + province + '\n'
            write_file(url, 'link_all')



# init_all_link()

# import threading
#
# import file_utils
# import request_yellowPage
#
#
# data = file_utils.read_link_all_list()
# def start_join(arr):
#     for element in arr:
#         element.start()
#     # đồng bộ phải chạy xong mới tới loạt tiếp theo
#     # comment -> có thread rảnh thì chạy luôn
#     for element in arr:
#         element.join()
#
#
# def multithread(number_thread, start_index):
#     try:
#         array_thread = []
#         for i in range(0, number_thread):
#             index = start_index + i
#             array_thread.append(threading.Thread(name='t' + str(i),
#                                                  target=request_yellowPage.request_to_link, args=(data[index],)))
#         start_join(array_thread)
#     except Exception as e:
#         print(e)
#         print('error multithread', start_index)
#
#
# def do_call_recursion(x, start_index):
#     print("==== start_index: ", start_index)
#     if start_index < len(data):
#         multithread(x, start_index)
#         file_utils.write_w(start_index + x,"index_count")
#     else:
#         return
#     # gọi lại đệ quy
#     do_call_recursion(x, start_index + x)
#

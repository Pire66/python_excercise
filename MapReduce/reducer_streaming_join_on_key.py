# Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя.
# Первый файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
# Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой системе. 
# Mapper передает данные в reducer в виде key / value, где key - id пользователя, value состоит из 2 частей: маркер файла-источника (query или url) и запрос или URL. 

# Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id пользователя, запрос, URL.

#     Sample Input:
#     user1	query:гугл
#     user1	url:google.ru
#     user2	query:стэпик
#     user2	query:стэпик курсы
#     user2	url:stepic.org
#     user2	url:stepic.org/explore/courses
#     user3	query:вконтакте

#     Sample Output:
#     user1	гугл	google.ru
#     user2	стэпик	stepic.org
#     user2	стэпик	stepic.org/explore/courses
#     user2	стэпик курсы	stepic.org
#     user2	стэпик курсы	stepic.org/explore/courses


import sys

tempdict = dict()
for line in sys.stdin:
    user_id,info = line.strip().split('\t')
    marker_source, info_source = info.split(':')
    user_dict = [{marker_source: [info_source]}]
    if tempdict.get(user_id):
        ind = 0 if marker_source == 'query' else 1
        list_user_dict = tempdict.get(user_id)
        try:
            temp_list_user_dict = list_user_dict[ind]
        except:
            temp_list_user_dict = {marker_source:[]}
            list_user_dict.append(temp_list_user_dict)
        temp_list = temp_list_user_dict.get(marker_source)
        temp_list.append(info_source)
        temp_list_user_dict.update({marker_source : temp_list})
        list_user_dict[ind] = temp_list_user_dict
    else:
        list_user_dict = user_dict
    tempdict.update({user_id:list_user_dict})
for i in tempdict.keys():
    list_user_dict = tempdict.get(i)
    if len(list_user_dict)>1:
        set1 = list_user_dict[0].get('query')
        set2 = list_user_dict[1].get('url')
        for j in set1:
            for k in set2:
                print(f'{i}\t{j}\t{k}')





import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
soup = BeautifulSoup(response.text,'html.parser')
# print(soup.title)
all_movies = soup.find_all(name='h3', class_='title')
movies_list = [movie.getText() for movie in all_movies]
# title_list = [title[1]for title in movies_list]
# print(movies_list)
# print(title_list)
title_list = []
for m in all_movies:

#     try:
#         l = m.getText()
#         j = l.split(')')
#         # print(j[1])
#         title_list.append(j[1])
#
#     except IndexError:
#         # print("index error")
#         j = l.split(':')
#         title_list.append(j[1])
#
#         # print(j[1])

    if all_movies.index(m) == 88:
        l = m.getText()
        j = l.split(':')
        title_list.append(j[1])
    else:
        l = m.getText()
        j = l.split(')')
        title_list.append(j[1])


# print(movies_list)
v = 99


for x in movies_list:
    if  v >= 0:
        with open("movies.txt", 'a') as file:
            file.write(f"{movies_list[v]}\n")
    v-=1
range()
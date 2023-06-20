import requests
import json


url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)
if 200 <= response.status_code < 300:
    res_dict = response.json()
max_intelligence = None
min_intelligence = 0
for hero in res_dict:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        if hero['powerstats']['intelligence'] > min_intelligence:
            min_intelligence = hero['powerstats']['intelligence']
            max_intelligence = hero['name']
print(f'Most intelligence superhero - {max_intelligence}')

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str) :
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for one_file in file_path :
            name_file = one_file.split('\\')[-1]
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path' : name_file}
            headesr = {'Authorization' : self.token}
            response = requests.get(url, params=params, headers=headesr)
            print(response.status_code)
            if 200 <= response.status_code < 300 :
                url_for_load = response.json().get('href')
                with open(one_file, 'r') as file :
                    response_2 = requests.put(url_for_load, files={'file' : file})
                    print(response_2.status_code, 'Файл загружен!!!!!')
            else : print('Something went wrong')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file =
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
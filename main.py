import requests
import os
import os.path
import sys
import json
from typing import List


idUser = '65726915' #sys.argv[1] потом параметр ид будет передаваться скрипту из консоли
tokenVk = '956f8155be6480e78e96e08a3015e3a9fff1ee08ac4fff55a9c38bfe8c197ab97da3bc44ce6bfaf48389a'
versionApi = '5.92'

def getUrlsPhotos(albumId='profile'):
    payloads = {
        'owner_id':idUser,
        'album_id': albumId,
        'access_token': tokenVk,
        'v':versionApi
    }
    res = requests.get('https://api.vk.com/method/photos.get', params=payloads)
    j = json.loads(res.text)
    urlsFotos = []
    for i in j['response']['items']:
        urlsFotos.append(i['sizes'][-1]['url']) #поиск картинок с самым большим разрешением
    return urlsFotos

def createFolderForPhotos():
    try:
        os.mkdir(idUser)
    except OSError:
        print("Папка уже существует")

def savePhotos(photoUrls: List[str]) -> List[str]:
    os.chdir(idUser)
    for url in photoUrls:
        namePhoto = url.split('/')[-1]
        img = requests.get(url)
        img_file = open(namePhoto, 'wb')
        img_file.write(img.content)
        img_file.close()


if __name__ == "__main__":
    createFolderForPhotos()
    photosUrls = getUrlsPhotos()
    savePhotos(photosUrls)


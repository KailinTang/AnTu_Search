# coding=utf-8
import glob

import cv2
from PIL import Image

from antu.pyimagesearch.coverdescriptor import CoverDescriptor
from antu.pyimagesearch.covermatcher import CoverMatcher
from antu.pyimsearch.database_tools import *


def searchImage(img):
    li = glob.glob('./antu/static/pic' + "/*.jpg")

    # print li

    cd = CoverDescriptor()
    names = []
    for i in li:
        names.append('./antu/static/database/' + i.split('/')[-1].split('.')[0])
    cv = CoverMatcher(cd, names)

    queryImage = img
    gray = cv2.cvtColor(queryImage, cv2.COLOR_BGR2GRAY)
    (queryKps, queryDescs) = cd.describe(gray)

    results = cv.search(queryKps, queryDescs)


    re = []
    for n in results:
        name = n[-1].split('/')[-1]
        imdir = '/static/pic/' + name + '.jpg'
        data = find_data_by_number(name)
        Title = data['Title']
        price = data['RMB'][2:]
        infolink = '/info/' + name
        re.append({'id': name, 'imdir': imdir, 'Title': Title,
                   'RMB': price, 'infolink': infolink})

    if len(results) ==0:
        return [{'id': 'NULL', 'imdir': 'NULL', 'Title': 'NULL',
                   'RMB': 'NULL', 'infolink': 'NULL'}]

    return re


# ToDo: searchSring(s)
def searchString(s):
    data = load_database()
    results = []
    for i in range(len(data)):
        title = data.iloc[i]['Title']
        score = compare(s, title)
        if score > 0.8:
            results.append(data.iloc[i]['No'])

    if len(results) ==0:
        return [{'id': 'NULL', 'imdir': 'NULL', 'Title': 'NULL',
                   'RMB': 'NULL', 'infolink': 'NULL'}]

    re =[]
    for n in results:
        name = str(n)
        imdir = '/static/pic/' + name + '.jpg'
        data = find_data_by_number(int(name))
        Title = data['Title']
        price = data['RMB']
        infolink = '/info/' + name
        re.append({'id': name, 'imdir': imdir, 'Title': Title,
                   'RMB': price, 'infolink': infolink})


    return re


# TODO:比较两个字符串的相似程度,这里还需要优化一下
def compare(s1, s2):
    ret = []
    try:
        for i in s1.split(' '):
            namei = i.lower()
            for j in s2.split(' '):
                scorej = 0.0
                namej = j.lower()
                for k in namei:
                    if k in namej:
                        scorej += 1.0

                if len(i) != 0:
                    sc = scorej / (len(i) * 1.0)
                else:
                    sc = 0

                if sc > 0.5:
                    ret.append(sc)
    except:
        pass
    if len(ret) > 0:
        score = sum(ret) / len(ret)
    else:
        score = 0

    return score


def pic_catch(x1, y1, x2, y2, pic_path):
    print(pic_path)
    image = Image.open(pic_path)
    rec_region = (x1, y1, x2, y2)
    result = image.crop(rec_region)
    return result
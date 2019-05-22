import requests, xmltodict
import json




def InfoFunc():
    # apiKey = 'R%2BomFWTHyWm%2FPdy9PWKNvk1TWKHzKxMlIAk9Xed%2Fyr5TdrNOqjPYe4L4wTDIiVak3%2FkgkowpiKN757INUz5gLw%3D%3D'
    # url = ''
    raw_data = f'http://api.visitkorea.or.kr/openapi/service/rest/KorService/locationBasedList?serviceKey=R%2BomFWTHyWm%2FPdy9PWKNvk1TWKHzKxMlIAk9Xed%2Fyr5TdrNOqjPYe4L4wTDIiVak3%2FkgkowpiKN757INUz5gLw%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&contentTypeId=15&mapX=126.981611&mapY=37.568477&radius=1000&listYN=Y'
    data = requests.get(raw_data).content
    xmlObject = xmltodict.parse(data)
    a = xmlObject['response']['body']['items']['item']
    b = a[0]['firstimage']

    AllInfo = []
    for data in a:
        AllInfo.append({
            'title' : data['title'],
            'addr1' : data['addr1'],
            # 'firstimage' : data['firstimage']
        })



    return AllInfo


# print(AllInfo)
# print(data['']+'말을적자')

#臺南市各區公所使用中公立公墓
#https://soa.tainan.gov.tw/Api/Service/Get/c67a7d45-7e30-4563-8663-800846a0e9d8
import pymysql.cursors
import requests
import json

#取得json檔資料
test = requests.get("https://soa.tainan.gov.tw/Api/Service/Get/c67a7d45-7e30-4563-8663-800846a0e9d8")
r = json.loads(test.text)

#連線到資料庫
try:
    connection = pymysql.connect(host='localhost',
                                 user='E94126208',
                                 password='0921',
                                 database='wordpress',
                                 cursorclass=pymysql.cursors.DictCursor)
    print("連線成功")     
except Exception as error: # 出現意外時印出
    print(error)


with connection:
    with connection.cursor() as cursor:

        # 匯入資料
        sql = "INSERT INTO `臺南市各區公所使用中公立公墓` (`設施名稱`, `座落地號或地址`, `Village`, `電話`) VALUES (%s, %s, %s, %s)"
        for i in range( len( r["data"] ) ):
            cursor.execute(sql, (r["data"][i]['設施名稱'],r["data"][i]['座落地號或地址'],r["data"][i]['Village'],r["data"][i]['電話']))

    connection.commit()
    cursor.close()

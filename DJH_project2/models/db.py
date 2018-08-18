import mysql.connector
from api import voicekit
import os

cnx = mysql.connector.connect(user='joe83830', password='123123',
                              host='140.113.144.78',
                              database='DJH')

cursor = cnx.cursor()


def create_store_list():

    query = "CREATE TABLE IF NOT EXISTS DJH.store_list (" \
            "storeID INT AUTO_INCREMENT," \
            "store_name varchar(75),"\
            "PRIMARY KEY (storeID),"\
            "UNIQUE (store_name));"

    cursor.execute(query)


def create_store_entry(name):

    query1 = ("INSERT IGNORE INTO DJH.store_list (store_name) " 
             "VALUES (\'{}\');").format(name)

    query2 = "CREATE TABLE IF NOT EXISTS DJH.{} (" \
             "foodID INT AUTO_INCREMENT," \
             "dish VARCHAR (75)," \
             "path VARCHAR (255)," \
             "rank INTEGER (10)," \
             "storeID INTEGER (10)," \
             "weekrank INTEGER (10)," \
             "FOREIGN KEY (storeID) REFERENCES DJH.store_list(storeID)," \
             "UNIQUE (dish)," \
             "PRIMARY KEY (foodID)) ENGINE=INNODB;".format(name)

    cursor.execute(query1)
    cursor.execute(query2)
    cnx.commit()


def create_menu(store, menu):
    dir_name = './audio/{}'.format(store)
    if !os.path.exist(dir_name):
        os.makedirs(dir_name)

    for ele in menu:

        path = './audio/{}/{}.mp3'.format(store, ele)
        voicekit.generate_audio(ele, path)

        query = "INSERT IGNORE INTO DJH.{} (dish, path, weekrank, rank) " \
                "VALUES (\'{}\', \'{}\', -1, -1);".format(store, ele, path)

        print(query)
        cursor.execute(query)
        cnx.commit()

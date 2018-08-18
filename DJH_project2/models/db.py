import mysql.connector
from api import voicekit

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
             "storeID INT," \
             "FOREIGN KEY (storeID) REFERENCES DJH.store_list(storeID)," \
             "UNIQUE (dish)," \
             "UNIQUE (rank)," \
             "PRIMARY KEY (foodID)) ENGINE=INNODB;".format(name)

    cursor.execute(query1)
    cursor.execute(query2)
    cnx.commit()

def create_audio(name):

    query = "SELECT 'foodID' FROM DJH.{} WHERE "


def create_menu(store, menu):

    for ele in menu:

        path = './audio/{}.mp3'.format(ele)
        voicekit.generate_audio(ele, path)

        query = "INSERT IGNORE INTO DJH.{} (dish, path)" \
                "VALUES (\'{}\', \'{}\');".format(store, ele, path)

        cursor.execute(query)
        cnx.commit()

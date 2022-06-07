from typing import Union
from fastapi import FastAPI

import mysql.connector

app = FastAPI()



conn = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="dbmovies")
cursor = conn.cursor()

@app.get("/films")
def getFilms():
    cursor.execute('SELECT * FROM tFilm')
    record = cursor.fetchall()
    array = []
    # for row in record:
    #     array.append(dict(zip(cursor.columns, row)))
    # return array
    for row in record:
        array.append(row)

    x= len(array[0])
    y=  len(array)

    all = []
    for i in range(y):
        for j in array[i]:
            all.append(j)

    return all
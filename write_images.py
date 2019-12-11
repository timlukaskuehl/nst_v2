import sqlite3 as sequel
import sys

def readImage():

    file_input = None

    try:
        file_input = open("llama.jpg", "rb")
        img = file_input.read()
        return img

    finally:

        if file_input:
            file_input.close()

def read_style_image():

    file_style = None

    try: 
        file_style = open("starrynight.jpg", "rb")
        img_style = file_style.read()
        return img_style
    
    finally:

        if file_style:
            file_style.close()

try:
    con = sequel.connect('image_database.db')

    cur = con.cursor()

    data_content = readImage()
    data_style = read_style_image()
    binary = sequel.Binary(data_content)
    binary_2 = sequel.Binary(data_style)
    cur.execute("CREATE TABLE pictures(data BLOB)")
    cur.execute("INSERT INTO pictures(data) VALUES (?)", (binary,) )
    cur.execute("INSERT INTO pictures(data) VALUES (?)", (binary_2,) )

    con.commit()

finally:

    if con:
        con.close()
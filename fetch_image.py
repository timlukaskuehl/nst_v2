import sqlite3 as sequel
import sys


def writeImage(data):

    fout = None

    try:
        fout = open("llama.jpg","wb")
        fout.write(data)

    finally:

        if fout:
            fout.close()

def write_style_image(data):

    file_out_style = None

    try: 
        file_out_style = open("starrynight.jpg", "wb")
        file_out_style.write(data)

    finally:

        if file_out_style:
            file_out_style.close()

try:
    con = sequel.connect('image_database.db')

    cur = con.cursor()
    cur.execute("SELECT data FROM pictures")

    while True:

        data = cur.fetchone()

        if data == None:
            break
    
    try:
        write_style_image(data)
      
    finally:
        writeImage(data)

finally:

    if con:
        con.close()
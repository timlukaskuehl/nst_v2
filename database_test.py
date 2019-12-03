import sqlite3
import os
import sys


class Picture(object):

    def __init__(self):
        self.image_name = []

    def load_directory(self, path='/Programming/PyTorch_NST/images'):

        for x in os.listdir(path):
            self.image_name.append(x)

        return self.image_name

    def create_database(self, name, image):
        
        conn = sqlite3.connect("pictures.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXIST pictures_table (name TEXT,image BLOP)""")

        cursor.execute(""" INSERT INTO pictures_table (name, image) VALUES (?,?)""",(name,image))

        conn.commit()
        cursor.close()
        conn.close()


def main():
    obj = Picture()
    os.chdir("/Programming/PyTorch_NST/images")
    for x in obj.load_directory():

        if ".jpg" in x:
            with open(x,"rb") as f:
                data = f.read()
                obj.create_database(name=x, image=data)
                print("{} Added to database ".format(x))

        else: 
            print("Please convert your image to .jpg")

def fetch_data():
    counter = 1
    os.chdir("/Programming/PyTorch_NST/images")
    conn = sqlite3.connect("pictures.db")
    cursor = conn.cursor()

    data = cursor.execute("""SELECT * FROM pictures_table""")
    for x in data.fetchall():
        print(x[1])
        with open("{}.jpg".format(counter),"wb") as f:
            f.write(x[1])
            counter= counter + 1


    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    fetch_data()
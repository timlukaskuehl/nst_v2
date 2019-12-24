import sqlite3
import sys

def readImage(filename):
# read the image data with the read bytes method (rb)

    with open(filename, 'rb') as file:
        dataInput = file.read()
    
    return dataInput

def database_insertion(image_id, image_name, image):
 # the goal is to give each image an id and insert the raw image data into the database table   
    try:
        # the database and the table with the two columns needs to be preconfigured
        database_connection = sqlite3.connect('image_database.db')
        cursor = database_connection.cursor()
        print("Database connection established")
        sql_command = """ INSERT INTO pictures
                                  (id, name, image) VALUES (?, ?, ?)"""
        # tells the program in which columns the data should be stored

        nst_images = readImage(image)
        # converts the image into binary
        data_tuple = (image_id, image_name, nst_images)
        # data is imported in a tuple format, helps us to store more information about the image at a later point
        cursor.execute(sql_command, data_tuple)
        # code on the database is executed
        database_connection.commit()
        print("Image IDs and images are now stored in the database :)")
        cursor.close()

    finally:
        if (database_connection):
            database_connection.close()
            print("Your connection to the database has ended. See you next time!")
            # once all the data is written into the table, the connection is closed

database_insertion(1, "content", "D:/Programming/PyTorch_NST/starrynight.jpg")
database_insertion(2, "style", "D:/Programming/PyTorch_NST/llama.jpg")
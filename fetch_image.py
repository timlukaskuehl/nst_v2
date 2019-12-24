import sqlite3
import sys

def writeImage(data, filename):
    # converts the binary data back into a "readable" format
    with open(filename, 'wb') as file:
        file.write(data)
    print("Saved the image in the selected location")

def read_image_data(image_id):
    # we want to read the two images and store them back on the hard drive in a certain folder

    try:
        database_connection = sqlite3.connect('image_database.db')
        # we have to establish a database connection first
        cursor = database_connection.cursor()
        print("Database connection established")

        sql_command_fetch = """SELECT * from pictures where id = ?"""
        # then we fetch all images with certain image ids
        cursor.execute(sql_command_fetch, (image_id,))
        fetch_rows = cursor.fetchall()
        # fetches all rows instead of fetchone (fetches a single row)
        
        for row in fetch_rows:
            
            image_name  = row[1]
            # number tells the program where in the table the information is stored
            image = row[2]

            print("Saving the images")
            image_path = "D:\Programming\PyTorch_NST\database_images\\" + image_name + ".jpg"
            # images are renamed to their name specified in the tuple and then saved in a different folder

            writeImage(image, image_path)

        cursor.close()

    finally:
        if (database_connection):
            database_connection.close()
            print("Your connection to the database has ended. See you next time!")
            # once all the images are saved, the connection is closed

read_image_data(1)
read_image_data(2)
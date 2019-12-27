import sys
import tkinter as tk
import os

#import matplotlib.pyplot as plt

root = tk.Tk()
root.title("What would Vincent Do?")
#initializing our root window, where all our frames will be housed

def raise_frame(frame):
    frame.tkraise()
#raises the frame to the top, so the user can interact with it

welcome_frame = tk.Frame(root)
database_frame = tk.Frame(root)
nst_frame = tk.Frame(root)
result_frame = tk.Frame(root)
#defines all the frames inside the root window
#each user interaction happens in a new frame

for frame in (welcome_frame, database_frame, nst_frame, result_frame):
    frame.grid(row=0, column=0, sticky="news")
#sets the grid for each frame, news (north, east, west, south) makes sure the content is centered

tk.Label(welcome_frame, text="""Welcome to our Neural Style Transfer program!\n
It is currently able to use the style of Vincent van Gogh's 'Starry Night' and transfer the style over onto a picture of a llama!\n
Have fun!\n""").pack()
tk.Button(welcome_frame, text="Next", command=lambda:raise_frame(database_frame)).pack()
#in each frame the user gets some information on what is happening
#the button uses a lambda function to call the next frame and raise it to the front
#the pack method makes sure the label or button has the right size and is visible

def fetch_images_db():
    os.system("fetch_image.py")
#defines the function to call the file in the next frame

tk.Label(database_frame, text="""First of all we need to download the two images from our database onto our hard drive.\n
If you press the button below, a program will run and download the files into a folder called 'database_images'.\n""").pack()
tk.Button(database_frame, text="Download the images", command= fetch_images_db).pack(side="left")
#press of the button uses the function to run the file and download the images from the database onto the hard drive
tk.Button(database_frame, text="Next", command=lambda:raise_frame(nst_frame)).pack(side="right")

def run_nst_calculations():
    os.system('nst_calculations.py')
#defines the file to calculate the images

tk.Label(nst_frame, text="""The next step is to calculate the two images and apply the style from our style image, in this case Starry Night, onto our content image, the llama.\n
This calculation is very complicated and we decided to use the code of Derrick Mwiti.\n
Since a lot of data needs to be processed, this code needs a couple of minutes to run. Sit back and relax!\n""").pack()
tk.Button(nst_frame, text="Calculate the images", command= run_nst_calculations).pack(side="left")
#the main file uses the downloaded images and calculates the final file in matplotlib
tk.Button(nst_frame, text="Next", command=lambda:raise_frame(result_frame)).pack(side="right")

tk.Label(result_frame, text="""In a couple of minutes a new window with the final image will open.\n
Have fun with it!\n""").pack()

raise_frame(welcome_frame)
#defines the first frame the user sees

root.mainloop()
#the program runs in a loop in order to receive the user interactions. Once the user closes the window, the loop is terminated
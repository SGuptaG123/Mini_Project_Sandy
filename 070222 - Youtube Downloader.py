
import shutil
from tkinter import *
from tkinter import filedialog as fld
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip


def select_path():
    # 
    path = fld.askdirectory()
    path_label.config(text=path)


def download_Vid():
    # Youtube path
    get_link = link_field.get()
    # Download path
    download_path = path_label.cget("text")
    screen.title("Downloading the file.")
    
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    VidClip = VideoFileClip(mp4_video)
    VidClip.close()

    shutil.move(mp4_video, download_path)

    screen.title("Download completed successfully. Download another file.")


    # move video to the desired location

screen = Tk()

# Title
screen.title("YouTube Video Downloader.")

# Canvas
canvas = Canvas(screen,width=500,height=500, bg='white')
canvas.pack()

# image logo, resize
img_logo = PhotoImage(file='C:\Python\YouTube Mini Projects\yt.png')
img_logo.subsample(2,2)


# fit in the canvas
canvas.create_image(250, 80, image=img_logo)

# Link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter the youtube video Link below", font=('calibri',15), bg='white')
path_label = Label(screen, text="Select path for download", font=('calibri',15), bg='white')
select_button = Button(screen, text="Select Path", command=select_path)
Download_button = Button(screen, text="Download file", command=download_Vid)

# Add widgets to the window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_button)
canvas.create_window(250, 390, window=Download_button)

# Download Buttons



screen.mainloop()



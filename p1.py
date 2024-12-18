import yt_dlp 
import os 
import csv

yt_link = input("Enter the YouTube link: ")

while True:
    try:
        quality = int(input("Enter the desired video quality: "))
        if quality >= 0:
            break
        else:
            print("enter a valid quality")
    except ValueError:
        print("Please enter a valid quality :")

download_directory = os.path.join(os.path.expanduser("~"), "Desktop")

csv_file = 'file.csv'
if quality >= 0 and quality <= 192:
    format_quality = '144p'
elif quality >= 193 and quality <= 360:
    format_quality = '240p'
elif quality >= 361 and quality <= 600:
    format_quality = '480p'
elif quality >= 601 and quality <= 900:
    format_quality = '720p'
elif quality >= 901:
    format_quality = '1080p'
else:
    format_quality = 'best'
    

ydl_opts = {
    'format': f'bestvideo[height<={format_quality}]+bestaudio/best[height<={format_quality}]',
    'outtmpl': os.path.join(download_directory, f'%(title)s.%(ext)s'),
    
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_link])
    print(f"The video has been downloaded successfully to {download_directory}.")
except Exception as e:
    print("An error occurred:", e)
    
    
    
    # https://youtu.be/AETFvQonfV8?si=vyFz9rzIK1RCaMJD
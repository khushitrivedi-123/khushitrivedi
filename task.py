import yt_dlp
import os
import csv

download_directory = os.path.join(os.path.expanduser("~"), "Desktop")

def map_quality_to_format(quality):
    if quality <= 192:
        return '144p'
    elif quality <= 360:
        return '240p'
    elif quality <= 600:
        return '480p'
    elif quality <= 900:
        return '720p'
    elif quality > 900:
        return '1080p'
    else:
        return 'best'

csv_file = '/home/khushi/khushi/downloads/file.csv'

try:
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Link'].startswith('#'):
                continue
            
            yt_link = row['Link']
            Quality = int(row['Quality'])

            format_quality = map_quality_to_format(Quality)

            ydl_opts = {
                'format': f'bestvideo[height<={format_quality}]+bestaudio/best[height<={format_quality}]',
                'outtmpl': os.path.join(download_directory, f'%(title)s.%(ext)s'),
                'overwrites' : True,
                'nooverwrites' : False,
                'force_generic_extractor' : False,
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    print(f"Downloading {yt_link} at {format_quality} quality...")
                    ydl.download([yt_link])
                print(f"The video has been downloaded successfully to {download_directory}.\n")
            except Exception as e:
                print(f"An error occurred while downloading {yt_link}: {e}\n")

except FileNotFoundError:
    print(f"CSV file '{csv_file}' not found. Please ensure the file exists.")

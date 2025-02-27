import sys
from pytube import YouTube
import yt_dlp

# Progress callback function
def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    percent = (size - bytes_remaining) * 100 / size
    print(f"\rDownloading... {percent:.2f}%", end="")



def downloadSingleVideo():
    savePath = input("Enter the save path:\n")
    link = input("Enter the YouTube video link:\n")

    try:
        ydl_opts = {
            'outtmpl': f"{savePath}/%(title)s.%(ext)s",
            'format': 'bestvideo+bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("\nDownload Complete!")
    except Exception as e:
        print(f"Error: {e}")


def downloadMultipleVideo():
    linkList = []
    savePath = input("Enter the save path:\n")

    # Collect video links
    while True:
        link = input(f"Enter YouTube link #{len(linkList) + 1} (or press 'C' to complete):\n")
        if link.upper() == "C":
            break
        linkList.append(link)

    # Download videos
    for index, link in enumerate(linkList, start=1): 
        try:
            ydl_opts = {
                'outtmpl': f"{savePath}/%(title)s.%(ext)s",
                'format': 'bestvideo+bestaudio/best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print("\nDownload Complete!")
        except Exception as e:
            print(f"Error: {e}")

    print('All tasks completed!')

def main():
    print(r"""
  _____                        _______ _            _______    _          
 |  __ \                      |__   __| |          |__   __|  | |         
 | |  | | _____      ___ __      | |  | |__   ___     | |_   _| |__   ___ 
 | |  | |/ _ \ \ /\ / / '_ \     | |  | '_ \ / _ \    | | | | | '_ \ / _ \
 | |__| | (_) \ V  V /| | | |    | |  | | | |  __/    | | |_| | |_) |  __/
 |_____/ \___/ \_/\_/ |_| |_|    |_|  |_| |_|\___|    |_|\__,_|_.__/ \___|
    """)

    while True:
        option = input("\nSelect an option:\n1: Download one video\n2: Download multiple videos\n3: Exit\n")
        if option == "1":
            downloadSingleVideo()
        elif option == "2":
            downloadMultipleVideo()
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

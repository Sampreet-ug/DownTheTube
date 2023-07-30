from logging import PercentStyle
import sys
import pytube
from pytube import YouTube
from pytube.cli import on_progress

def progress_function(self,stream, chunk,file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = PercentStyle(bytes_remaining, size)

def downloadSingleVideo():
    savePath = input("Enter the save path\n")
    link = input("Enter the youtube link to video\n")

    try:     
        yt = YouTube(link, on_progress_callback=on_progress)
    except: 
        print("Connection Error") 
    
    try:
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        #yt = yt.streams.filter(progressive=True, file_extension='mp4')
        #print(yt.streams.filter)
        #res=input("Select the resolution")
        yt.download(savePath)
        #stream = yt.streams.get_by_itag(res)
        #stream.download(savePath)
        print("(:")
    except: 
        print("Some Error!") 

    print('Task Completed!')

def downloadMultipleVideo():

    linkList = []
    loop = 1
    savePath = input("Enter the save path:\n")
    
    while loop >= 1:
        link = input("Enter the youtube link #" + str(loop) + "\nPress 'C' to complete:\n")
        if(link != "C"):
            linkList.append(link)
            loop+=1
        else:
            loop = 0
            
    for i in linkList: 
        try: 
            yt = YouTube(i, on_progress_callback=on_progress) 
        except: 
            print("Connection Error")  
       
        try:
            print("Downloading video #"+str(linkList.index(i)+1)+"\n")
            yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            yt.download(savePath)
            print("(:")
        except:
            print("Some Error!")
            
    print('Task Completed!')

def main():
    print(r"""
               

  _____                        _______ _            _______    _          
 |  __ \                      |__   __| |          |__   __|  | |         
 | |  | | _____      ___ __      | |  | |__   ___     | |_   _| |__   ___ 
 | |  | |/ _ \ \ /\ / / '_ \     | |  | '_ \ / _ \    | | | | | '_ \ / _ \
 | |__| | (_) \ V  V /| | | |    | |  | | | |  __/    | | |_| | |_) |  __/
 |_____/ \___/ \_/\_/ |_| |_|    |_|  |_| |_|\___|    |_|\__,_|_.__/ \___|
                                                                          
                                                                          

 """)
    val = 0
    while val == 0:
        option = input("\nSelect the option:\n1: Download one video\n2: Download multiple videos\n3: Close program\n")
        if(option == "1"):
            downloadSingleVideo()
        if(option == "2"):
            downloadMultipleVideo()
        if(option == "3"):
            sys.exit("Closing the program")

if __name__ == "__main__":
    main()

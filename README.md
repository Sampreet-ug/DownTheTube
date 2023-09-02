# 'Down The Tube' a YouTube Video Downloader

This is a simple script to download YouTube videos. It uses the `pytube` library to accomplish this.

## Dependencies

- `pytube`
- `logging`

You can install these dependencies by running `pip install -r requirements.txt`

## Usage

1. Run the script using `python main.py`
2. You will be presented with a menu:
    ```
    1: Download one video
    2: Download multiple videos
    3: Close program
    ```
3. If you choose to download one video, you will be asked to enter the save path and the YouTube link to the video.
4. If you choose to download multiple videos, you will be asked to enter the save path and then the YouTube links to the videos one by one. Press 'C' to complete the list of links.
5. The script will then download the videos and save them to the specified path.

## Note

The script downloads the highest resolution MP4 file available for the video. If you wish to change this, you can modify the `downloadSingleVideo` and `downloadMultipleVideo` functions in the script.

# 'Down The Tube' - A YouTube Video Downloader

This is a simple command-line YouTube video downloader. It supports downloading single and multiple videos using `pytube` and `yt-dlp`.

## 📌 Dependencies

- `pytube`
- `yt-dlp`
- `ffmpeg`
- `logging`

You can install these dependencies by running:
```sh
pip install -r requirements.txt
```

## 🚀 Usage

1. Run the script using:
```sh
python src/DownTheTube.py
```
2. You will be presented with a menu:
    ```
    1: Download one video
    2: Download multiple videos
    3: Close program
    ```
3. If you choose to download one video, you will be asked to enter the save path and the YouTube link to the video.
4. If you choose to download multiple videos, you will be asked to enter the save path and then the YouTube links to the videos one by one. Press 'C' to complete the list of links.
5. The script will then download the videos and save them to the specified path.

## 🔗 Additional Features
- Uses `yt-dlp` for better compatibility with YouTube.
- Supports downloading the best quality video and audio.
- Requires `ffmpeg` for merging video and audio streams.

## 💡 Note
The script downloads the highest resolution MP4 file available for the video by default. If you wish to change this, you can modify the `downloadSingleVideo` and `downloadMultipleVideo` functions in the script.

### Installing FFmpeg
#### Windows
- Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- Add `ffmpeg/bin` to the system PATH.

#### Linux (Ubuntu/Debian)
```sh
sudo apt update && sudo apt install ffmpeg -y
```

#### MacOS
```sh
brew install ffmpeg
```

## 📜 License
This project is open-source under the MIT License.


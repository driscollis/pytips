from pytube import YouTube

DOWNLOAD_FOLDER = "PUT_YOUR_DOWNLOADS_FOLDER_HERE"
video_url = "https://www.youtube.com/watch?v=ff_0hypwIPA"
video_obj = YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
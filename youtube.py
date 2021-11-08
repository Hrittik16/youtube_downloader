from pytube import YouTube

link = "https://www.youtube.com/watch?v=7KSNmziMqog"

video = YouTube(link)

video = video.streams.get_highest_resolution()

video.download()
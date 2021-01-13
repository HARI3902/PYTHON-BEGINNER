from pytube import YouTube
url=input("Enter the Url:")
try:
    yt_obj=YouTube(url)
    filters=yt_obj.streams.filter(progressive=True,file_extension='mp4')
    filters.get_highest_resolution().download()
    print("Download successful")
except Exception as e:
    print(e)

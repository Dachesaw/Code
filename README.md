# yt soundtrack
from pytube import YouTube
link = input("Link:" )
yt = YouTube(link)

print (f'Title: {yt.title}')
print (f'Колчичесво просмотров: {yt.views}')
print (f'Продолжительность видео: {yt.length}')
stream = yt.streams.get_by_itag(140)
stream.download()
print('finished')

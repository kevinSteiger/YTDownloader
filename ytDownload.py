from pytube import YouTube

vid = YouTube("https://www.youtube.com/watch?v=v3UBlEJDXR0")

title = vid.title

print(title)
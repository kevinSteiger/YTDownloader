from pytube import YouTube

vid = YouTube("https://www.youtube.com/watch?v=6pxRHBw-k8M") 

#vid = YouTube("https://www.youtube.com/watch?v=v3UBlEJDXR0")

title = vid.title


print(vid.streams.filter(progressive=True))

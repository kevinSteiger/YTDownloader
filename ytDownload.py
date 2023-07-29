from pytube import YouTube
#Problem: https://stackoverflow.com/questions/58456229/i-am-trying-to-download-video-using-pytube-however-for-some-reason-no-sound-is-d

vid = YouTube("https://www.youtube.com/watch?v=6pxRHBw-k8M") 

#vid = YouTube("https://www.youtube.com/watch?v=v3UBlEJDXR0")

title = vid.title

print("You will now be downloading: " + title)

stream = vid.streams.get_by_itag(22)
print("Downloading...this may take a while")
stream.download(output_path = r"c:\Users\kev1n\Downloads", filename = title)
print("End of program")
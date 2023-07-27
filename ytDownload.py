from pytube import YouTube


vid = YouTube("https://www.youtube.com/watch?v=v3UBlEJDXR0")

title = vid.title

print("You will now be downloading: " + title)
#vid.streams.filter(progressive=True)

#vid.download(output_path = r"c:\Users\kev1n\Downloads", filename = title)
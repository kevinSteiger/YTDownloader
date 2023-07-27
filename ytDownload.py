from pytube import YouTube

#HD test Video linK: https://www.youtube.com/watch?v=6pxRHBw-k8M
#Normal test Video Link: https://www.youtube.com/watch?v=v3UBlEJDXR0


link = input("Paste Video Link: ")

vid = YouTube(link)

title = vid.title

print(vid.streams.filter(adaptive=True))
itag = input("\nPlease select an itag from above based on the video quality/type you'd like: ")
print("\nYou will now be downloading: " + title)


#stream = vid.streams.first()

stream = vid.streams.get_by_itag(itag)
print("Downloading...this may take a while")
stream.download(output_path = r"c:\Users\kev1n\Downloads", filename = title)
print("End of program")
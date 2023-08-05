from pytube import YouTube
import ffmpeg
import subprocess


#Problem: https://stackoverflow.com/questions/58456229/i-am-trying-to-download-video-using-pytube-however-for-some-reason-no-sound-is-d

vid = YouTube("https://www.youtube.com/watch?v=6pxRHBw-k8M") 

#vid = YouTube("https://www.youtube.com/watch?v=v3UBlEJDXR0")

title = vid.title

print("You will now be downloading: " + title)

video = vid.streams.get_by_itag(313)
audio = vid.streams.get_by_itag(140)

print("Downloading...this may take a while")

video.download(filename = title + "video.mp4")
audio.download(filename = title + "audio.mp4")
#output_path = r"c:\Users\kev1n\Downloads", 

videoStream = ffmpeg.input(title + "video.mp4")
audioStream = ffmpeg.input(title + "audio.mp4")
video = title + ".mp4"

ffmpeg.output(videoStream, audioStream, video, vcodec='copy', acodec='aac', strict='experimental', b='192k').run()

print("End of program")
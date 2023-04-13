from pytube import YouTube

# Get the YouTube video link from the user
video_url = input("Enter the YouTube video link: ")

# Create a YouTube object and get the highest resolution stream
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()

# Get the download link of the video
download_link = stream.url

# Print the download link
print("Download link:", download_link)

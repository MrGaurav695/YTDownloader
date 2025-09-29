from pytubefix import YouTube, Playlist

def download_video(url, path, choice):
    yt = YouTube(url)

    if choice == "1":
        stream = yt.streams.get_highest_resolution()
        print(f"\n🎥 Downloading video: {yt.title} ...")
    elif choice == "2":
        stream = yt.streams.filter(only_audio=True).first()
        print(f"\n🎵 Downloading audio: {yt.title} ...")
    else:
        print("❌ Invalid choice!")
        return

    if path.strip() == "":
        stream.download()
    else:
        stream.download(output_path=path)

    print(f"✅ Done: {yt.title}")

print("Download Options:")
print("1. Single Video")
print("2. Playlist")
main_choice = input("Enter 1 or 2: ")

url = input("Enter YouTube URL: ")
path = input("Enter download path (leave empty for current folder): ")

print("\nChoose download type:")
print("1. Video (highest resolution)")
print("2. Audio only")
choice = input("Enter 1 or 2: ")

if main_choice == "1":
    download_video(url, path, choice)

elif main_choice == "2":
    playlist = Playlist(url)
    print(f"\n📂 Playlist found: {playlist.title}")
    print(f"📺 Total videos: {len(playlist.video_urls)}")

    for video_url in playlist.video_urls:
        try:
            download_video(video_url, path, choice)
        except Exception as e:
            print(f"⚠️ Skipped a video due to error: {e}")

    print("\n✅ Playlist download completed!")

else:
    print("❌ Invalid choice!")

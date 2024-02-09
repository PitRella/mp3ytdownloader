YouTube Music Converter

This Python project provides a convenient way to download YouTube music videos, convert them from MP4 to MP3 format, and organize the files efficiently. The script utilizes the youtube_dl library for downloading YouTube videos and the moviepy library for converting MP4 to MP3.

Features:
1. Download YouTube Music:
2. Reads URLs from the "download.txt" file.
3. Downloads the corresponding YouTube music videos using youtube_dl.
   
Convert to MP3:
1. Converts downloaded MP4 files to MP3 format.
2. Utilizes the moviepy.editor library for the conversion process.

Organize Files:
1. Moves the converted MP3 files to a dedicated "mp3_songs" folder.
2. Deletes the original MP4 files to save space.

How to Use:
1. Prepare download.txt:
2.Create a "download.txt" file and add YouTube URLs, one per line.

Run the Script:

1. Execute the script to start the download, conversion, and organization process.
Check Results:
Find the converted MP3 files in the "mp3_songs" folder.

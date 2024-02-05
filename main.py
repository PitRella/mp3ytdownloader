import shutil
from moviepy.editor import *

import youtube_dl


def convert_all_songs():
    def MP4ToMP3(mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()

    all_files = os.listdir()
    mp4_files = []
    for file in all_files:
        if file[-3:] == 'mp4':
            mp4_files.append(file)
    for mp4_song in mp4_files:
        MP4ToMP3(f'./{mp4_song}', f'./{mp4_song.replace('.mp4', '.mp3')}')


def download_mp4():
    mp3_songs = []
    try:
        f = open('download.txt', 'r')
    except FileNotFoundError:
        print('Not found file\nCreated download.txt')
        f = open('download.txt', 'w')
        return 1
    else:
        with open("download.txt", "r") as file:
            for song in file:
                mp3_songs.append(song.replace('\n', ''))
        if len(mp3_songs) > 0:
            with youtube_dl.YoutubeDL({}) as ydl:
                print(mp3_songs)
                print('--Started downloading songs--')
                ydl.download(mp3_songs)
        else:
            print(f'No songs in file download.txt')


def move_to_mp3_folder():
    if not os.path.exists('./mp3_songs'):
        os.mkdir('./mp3_songs')
    all_files = os.listdir()
    mp3_songs = []
    print('Starting to move files to mp3 folder')
    for file in all_files:
        if file[-3:] == 'mp3':
            mp3_songs.append(file)
    print(mp3_songs)
    for mp3_song in mp3_songs:
        shutil.move(f'./{mp3_song}', f'./mp3_songs/{mp3_song}')

    print('Finished moving files to mp3 folder')


def remove_mp4_songs():
    all_files = os.listdir()
    files_to_delete = []
    for file in all_files:
        if file[-3:] == 'mp4':
            files_to_delete.append(file)
    for file_to_delete in files_to_delete:
        os.remove(f'./{file_to_delete}')


if __name__ == '__main__':
    if download_mp4() != 1:
        convert_all_songs()
        move_to_mp3_folder()
        remove_mp4_songs()

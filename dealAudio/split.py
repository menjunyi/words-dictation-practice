from pydub import AudioSegment
# 用于将一段音频切分处理
file_name = "../video/chapter3/01Test1.mp3"

AudioSegment.converter = "D:\\DeveloperTools\\ffmpeg\\ffmpeg-20200220-56df829-win64-static\\bin\\ffmpeg.exe"
sound = AudioSegment.from_mp3(file_name)

start_time = "0:00"
stop_time = "0:42"

print("time:", start_time, "~", stop_time)

start_time = (int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])) * 1000
stop_time = (int(stop_time.split(':')[0]) * 60 + int(stop_time.split(':')[1])) * 1000

print("ms:", start_time, "~", stop_time)

word = sound[start_time:stop_time]
save_name = "word" + file_name[6:]
print(save_name)

word.export(save_name, format="mp3", tags={'artist': 'AppLeU0', 'album': save_name[:-4]})

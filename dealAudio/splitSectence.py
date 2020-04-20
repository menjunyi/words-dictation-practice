from pydub import AudioSegment
from pydub.silence import split_on_silence


name = "../video/script/test 1/"
file_name = "1.1" + ".mp3"
sound = AudioSegment.from_mp3(name + file_name)

# silence time:700ms and silence_dBFS<-70dBFS
chunks = split_on_silence(sound, min_silence_len=300, silence_thresh=-70)
words = chunks[2:]  # first and second are not words.
order = range(len(words))

count = 0

for i in order:
    save_name = "../video/script/C10/" + \
                "{0}.mp3".format(count)
    words[i].export(save_name, format="mp3", tags={'album': "剑桥雅思听力句子"})
    count += 1

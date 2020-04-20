from pydub import AudioSegment
from pydub.silence import split_on_silence
import mapper


name = "../video/chapter3/09Test9"
file_name = name + ".mp3"
sound = AudioSegment.from_mp3(file_name)
unit = int(name.split("Test")[1])
chapter = 1

# silence time:700ms and silence_dBFS<-70dBFS
chunks = split_on_silence(sound, min_silence_len=700, silence_thresh=-70)
words = chunks[2:]  # first and second are not words.
order = range(len(words))
answer_word = mapper.get_answers((chapter, unit))

count = 0

for i in order:
    print(answer_word[count][0].lower())
    save_name = "..\\video\\chapter3unit" + str(unit) + "\\" + \
                "{0}.mp3".format(answer_word[count][0].lower()) + file_name.split(".")[1]
    words[i].export(save_name, format="mp3", tags={'album': "雅思王陆听力语料库"})
    count += 1

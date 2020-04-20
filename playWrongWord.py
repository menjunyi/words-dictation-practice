from playsound import playsound
import mapper
import time

practice_time = 11
result = mapper.get_wrong_words(practice_time)

for row in result:
    subfile = 'chapter3unit' + str(row[2])
    wrongWord = row[5]
    # print(wrongWord)
    playsound('video\\' + subfile + '\\' + wrongWord + '.mp3')


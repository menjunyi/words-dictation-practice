import pymysql.cursors
import mapper

answer = open("answer/chapter4", "r")
done = False
count = 1
chapter = 4
unit = 1
mapper.delete_answer(chapter)
while not done:
    line = answer.readline().strip('\n').strip(' ')
    if line != '':
        words = line.split(' ')
        words.remove(words[0])
        for word in words:
            data = (chapter, unit, count, word)
            mapper.insert(data)
            count = count + 1
    else:
        done = True
    unit = unit + 1

answer.close()

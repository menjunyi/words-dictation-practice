import mapper
import os

file = "practice/practice1chapter1"
answer = open(file, "r")
filename = os.path.basename(file)
chapter = int(filename.split("chapter")[1])
time = int(filename.split("practice")[1].split("chapter")[0])
speed = '1.5'

# 删除之前的记录
mapper.delete_all_record(chapter, time)

done = False
unit = 1
while not done:
    my_practice = answer.readline().split(' ')
    answer_word = mapper.get_answers((chapter, unit))
    print(chapter, unit, answer_word)
    count = 0
    my_practice.remove(my_practice[0])
    if len(my_practice) > 0:
        for word in my_practice:
            # chapter unit sort word times
            is_right = 1
            if word.lower().strip("\n") != answer_word[count][0].lower():
                is_right = 0
            data = (chapter, unit, count, time, speed, word, answer_word[count][0], is_right)
            if unit > 0:
                mapper.insert_practise(data)
            count = count + 1
    else:
        done = True
    unit = unit + 1

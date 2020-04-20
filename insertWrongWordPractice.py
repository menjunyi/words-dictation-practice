import mapper
import os

file = "practice/practice11wrong10"
answer = open(file, "r")
filename = os.path.basename(file)
practice_time = int(filename.split("wrong")[1])
time = int(filename.split("practice")[1].split("wrong")[0])
speed = '1.0'

# 删除之前的记录
# mapper.delete_all_record(chapter, time)

done = False
unit = 1
while not done:
    my_practice = answer.readline().split(' ')
    answer_word = mapper.get_wrong_words(practice_time)
    count = 0
    if len(my_practice) > 0:
        for word in my_practice:
            # chapter unit sort word times
            is_right = 1
            if word.lower().strip("\n") != answer_word[count][5].lower():
                is_right = 0

            data = (answer_word[count][1], answer_word[count][2], answer_word[count][3], time, speed, word, answer_word[count][5], is_right)
            if unit > 0:
                mapper.insert_practise(data)
            count = count + 1
    else:
        done = True
    unit = unit + 1
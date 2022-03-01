#Read file
with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")
header = data[0]
students = data[1:]

total_student = len(students)
#Remove last student
students.pop()
#Split header
header = header.split(",")
subjects = header[5:]
#Split each student in list
for i in range(len(students)):
    students[i] = students[i].split(",")
not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

#Loop through all students
for s in students:
    #iterate through all subjects
    for i in range(5,len(s)):
        if s[i] == "-1":
            not_take_exam[i-5] += 1
not_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,11):
    not_take_exam_percentage[i] = not_take_exam[i]*100/total_student

import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()
y_pos = np.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)
plt.xticks(y_pos, subjects)
axis.set_ylim(0,100)

#Title
plt.ylabel('Percentage')
plt.title('Thống Kê Điểm')

#Annotation
rects = axis.patches
for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom")
plt.bar
plt.show()

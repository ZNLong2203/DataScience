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

#Remove last students
students.pop()

#Get number of student per age group
# 2003 2002 2001 2000 ... 1994 <= 1993
# 17 18 19 ... 26 >=27

num_of_stundent_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
average_of_stundent_per_age_group= [0,0,0,0,0,0,0,0,0,0,0]

for s in students:
    age = 2020 - int(s[4])
    if age >= 27:
        age = 27
    num_of_stundent_per_age_group[age-17] +=1

    sum_score = 0 #Tong diem
    count_score = 0 #So mon thi
    for i in range(11):
        if s[i+5] != "-1":
            count_score += 1
            sum_score += float(s[i+5])
    average = sum_score/count_score
    average_of_stundent_per_age_group[age-17] +=average

for i in range(len(average_of_stundent_per_age_group)):
    average_of_stundent_per_age_group[i]=average_of_stundent_per_age_group[i]/num_of_stundent_per_age_group[i]
for i in range(len(average_of_stundent_per_age_group)):
    average_of_stundent_per_age_group[i]=average_of_stundent_per_age_group[i]*7000
age = ["17","18","19","20","21","22","23","24","25","26",">=27"]
import matplotlib.pyplot as plt
import numpy as np

figure, axis = plt.subplots()
y_pos = np.arange(len(subjects))

plt.bar(y_pos, num_of_stundent_per_age_group, align='center', alpha=0.5)
plt.plot(y_pos, average_of_stundent_per_age_group, color='red', marker="o")
plt.xticks(y_pos, age)
axis.set_ylim(0,70000)
#Right side ticks
axis2 = axis.twinx()
axis2.tick_params('y',color='r')
axis2.set_ylim(0,10)
axis2.set_ylabel('Điểm trung bình')
#Title
axis.set_ylabel('Số học sinh')
plt.title('Tuổi trung bình')
axis.set_xlabel('Tuổi')

#Annotation
rects = axis.patches
for rect, label in zip(rects, num_of_stundent_per_age_group):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom")
plt.bar
plt.show()

    

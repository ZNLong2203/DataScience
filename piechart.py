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

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

#Number of students who took 0,1,2,3,... subjects
for s in students:
    count = 0
    for i in range(len(subjects)):
        if s[i+5] != "-1":
            count +=1
    num_of_exam_taken[count] +=1

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = "0 môn", "1 môn", "2 môn", "3 môn", "4 môn", "5 môn", "6 môn", "7 môn", "8 môn", "9 môn", "10 môn", "11 môn" 
sizes = [15, 30, 45, 10,1,1,1,1,1,1,1,1]
explode = (0, 0.1, 0, 0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
import csv
file = open("raw_data.txt", "r")

#Read first student
datas = file.read().split("\n")

#Write header to csv
with open("clean_data.csv", encoding ="utf8",mode="w",newline='') as file_csv:
    header = ["Sbd", "Tên", "dd", "mm", "yy", "Toán", "Ngữ văn", "Khxh", "Khtn", "Lịch sử", "Địa lí", "Gdcd", "Sinh học", "Vật Lí", "Hóa Học", "Tiếng anh"]
    writer = csv.writer(file_csv)
    writer.writerow(header)

sbd = 2000000

for data in datas:
    try:
        sbd +=1
        sbd_str = "0" + str(sbd)
        #Make data becomes a list
        data = data.split("\\n")

        #Remove \r and \t
        for i in range(0,len(data)):
            data[i] = data[i].replace("\\r", "")
            data[i] = data[i].replace("\\t", "")

        #Remove tags
        for i in range(len(data)):
            tags = []
            for j in range(0,len(data[i])):
                if data[i][j] == "<":
                    begin = j
                if data[i][j] == ">":
                    end = j
                    tags.append(data[i][begin:end+1])

            for tag in tags:
                data[i] = data[i].replace(tag, "")


        for i in range(len(data)):
            data[i] = data[i].strip()

        unempty_line = []
        for i in range(len(data)):
            if data[i] != "":
                unempty_line.append(data[i])
        data = unempty_line        

        #Choose relevant elements
        name = data[7]
        dob = data[8]
        scores = data[9]

        #Load unicode table
        chars = []
        codes = []

        file = open("unicode.txt", encoding="utf8")
        unicode_table = file.read().split("\n")

        for code in unicode_table:
            x = code.split(" ")
            chars.append(x[0])
            codes.append(x[1])

        #Replace special char in name and scores
        for i in range(len(chars)):
            name = name.replace(codes[i], chars[i])
            scores = scores.replace(codes[i], chars[i])

        for i in range(len(name)):
            if name[i:i+2] == "&#":
                name = name[:i] + chr(int(name[i+2:i+5])) + name[i+6:]
        for j in range(len(scores)): 
            if scores[j:j+2] == "&#":
                scores = scores[:j] + chr(int(scores[j+2:j+5])) + scores[j+6:]   

        #Change to lower case
        name = name.title()
        scores =scores.title()

        #Split dob
        dob_list = dob.split("/")
        dd = int(dob_list[0])
        mm = int(dob_list[1])
        yy = int(dob_list[2])

        #Process scores
        #Remove:
        scores = scores.replace(":", "")

        scores = scores.replace("Khxh ", "Khxh   ")
        scores = scores.replace("Khtn ", "Khtn   ")
        scores = scores.replace("10", " 10")
        scores_list = scores.split("   ")
        data = [sbd_str, name, str(dd), str(mm), str(yy), ]
        #Add score to data
        for subject in  ["Toán", "Ngữ Văn", "Khxh", "Khtn", "Lịch Sử", "Địa Lí", "Gdcd", "Sinh Học", "Vật Lí", "Hóa Học", "Tiếng Anh"]:
            if subject in scores_list:
                data.append(str(float(scores_list[scores_list.index(subject)+1])))
            else:
                data.append("-1")     
        with open("clean_data.csv", "a", encoding='utf-8',newline='') as file_csv:
            writer =csv.writer(file_csv)
            writer.writerow(data)
    except:
        continue        
   
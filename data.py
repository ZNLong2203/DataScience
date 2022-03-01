import subprocess
start = 2000001
end = 2075000
# result = subprocess.check_output('curl -F "sobaodanh = 02000001" diemthi.hcm.edu.vn/Home/Show')
# print(result)

file = open("raw_data.txt", "w")

for i in range(start,end):
    command = 'curl -F "SoBaoDanh=0' + str(i) + '" diemthi.hcm.edu.vn/Home/Show'
    result = subprocess.check_output(command)
    file.write(str(result) + "\n")

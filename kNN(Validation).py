import xlrd
import xlwt
import time
start_time = time.time()

workbook = xlrd.open_workbook("Dataset.xlsx")

worksheet1 = workbook.sheet_by_name("DataTrain")
worksheet2 = workbook.sheet_by_name("DataTest")

t_rows1 = (worksheet1.nrows)
t_rows2 = (worksheet2.nrows)

t_cols1 = worksheet1.ncols
t_cols2 = worksheet2.ncols

k = 0

like = []
provokasi = []
komentar = []
emosi = []
hoax = []
dataTrain = list()
data = list()
temp = list()
validate = list()

def akurasi(dataTrain,worksheet1):
    sum =0
    total = 0
    for i in range(3900, 4000):
        #print((dataTrain[i][4]), (float(worksheet1.cell(i+1, 5).value)))
        if ((dataTrain[i][4])==(float(worksheet1.cell(i+1, 5).value))):
            sum += 1
        total += 1
    return ("Total Benar = ",sum,"Dari total data = ",total,"Akurasi = ",(sum/total)*100,"Percent")

def kkn(validate,y):
    ya = 0
    no = 0
    for i in range(39):
        if ((validate[i][1]) == 1.0):
            ya += 1
        elif ((validate[i][1]) == 0.0):
            no += 1
        #print(validate[i][1])
    if (ya > no):
        dataTrain[y][4] = 1.0
    else:
        dataTrain[y][4] = 0.0

print("DataTrain    : ","Jumlah row : {0}, Jumlah coloum : {1}".format(t_rows1,t_cols1))
print("DataTest     : ","Jumlah row : {0}, Jumlah coloum : {1}".format(t_rows2,t_cols2))

"""VALIDASI"""

for b in range (1,4001):
    for a in range (1,6):
        data.append(float(worksheet1.cell(b, a).value))
    dataTrain.append(data)
    data = []

# print(dataTrain)
# print(dataTrain[3999][3])
# print(len(dataTrain))
# print(dataTrain[0][0])

for x in range (3900,4000):
    for y in range (0, 3900):
        temp = ((((dataTrain[x][0] - dataTrain[y][0]))**2+
                ((dataTrain[x][1] - dataTrain[y][1]))**2+
                ((dataTrain[x][2] - dataTrain[y][2]))**2+
                ((dataTrain[x][3] - dataTrain[y][3]))**2)**0.5)
        validate.append([temp,dataTrain[x][4]])
    validate.sort(key=lambda x : x[0])
    kkn(validate,x)
    #     k = k + temp
    # k = (k**0.5)
    #validate.sort()
for i in range(len(dataTrain)):
    print("B",i+1,dataTrain[i])
print(akurasi(dataTrain,worksheet1))

print(len(dataTrain))

#for i in like,provokasi,komentar,emosi:
    #print(i)

# for x in range (3001,4001,1):
#     for y in range (1,3001,1):
#         for i in range(1,5,1):
#             temp = (((float(format(worksheet1.cell(y,i).value)))-(float(format(worksheet1.cell(x,i).value))))**2)
#             k = k + temp
#         k = (k**0.5)
#         print(k)
print("= Running Time %s (s) =" % (time.time() - start_time))
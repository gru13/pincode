import csv


file = open("./DATA/data.csv")
cont = list(csv.reader(file))
#
var_name_dict = {'MANIPUR': 'MANIPUR', 'UTTAR PRADESH': 'UTTARPRADESH', 'GUJARAT': 'GUJARAT', 'RAJASTHAN': 'RAJASTHAN', 'TAMIL NADU': 'TAMILNADU', 'HARYANA': 'HARYANA', 'KARNATAKA': 'KARNATAKA', 'GOA': 'GOA', 'DADRA & NAGAR HAVELI': 'DADRANAGARHAVELI', 'MIZORAM': 'MIZORAM', 'HIMACHAL PRADESH': 'HIMACHALPRADESH', 'PONDICHERRY': 'PONDICHERRY', 'ARUNACHAL PRADESH': 'ARUNACHALPRADESH', 'MADHYA PRADESH': 'MADHYA PRADESH', 'DELHI': 'DELHI', 'SIKKIM': 'SIKKIM', 'TELANGANA': 'TELANGANA', 'DAMAN & DIU': 'DAMANDIU',
                 'CHANDIGARH': 'CHANDIGARH', 'BIHAR': 'BIHAR', 'ASSAM': 'ASSAM', 'PUNJAB': 'PUNJAB', 'LAKSHADWEEP': 'LAKSHADWEEP', 'ANDHRA PRADESH': 'ANDHRAPRADESH', 'CHATTISGARH': 'CHATTISGARH', 'UTTARAKHAND': 'UTTARAKHAND', 'ODISHA': 'ODISHA', 'MEGHALAYA': 'MEGHALAYA', 'KERALA': 'KERALA', 'NAGALAND': 'NAGALAND', 'TRIPURA': 'TRIPURA', 'JHARKHAND': 'JHARKHAND', 'JAMMU & KASHMIR': 'JAMMUKASHMIR', 'WEST BENGAL': 'WESTBENGAL', 'MAHARASHTRA': 'MAHARASHTRA', 'ANDAMAN & NICOBAR ISLANDS': 'ANDAMANNICOBARISLANDS'}
for a in var_name_dict:
    globals()[var_name_dict[a]] = list()
for a in cont[1:]:
    try:
        globals()[var_name_dict[a[-1]]].append(a)
    except:
        print(False,"code error")
        # print (a[-1])
# globals()[var_name_dict[a]]
for a in var_name_dict: 
    filep = "./DATA/"+a+".csv"
    with open(filep, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(globals()[var_name_dict[a]])
file.close()
print(False)
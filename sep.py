import csv
from os import stat
from typing import List
file = open("./data.csv")
cont = list(csv.reader(file))
# 
states = ['MANIPUR', 'UTTAR PRADESH', 'GUJARAT', 'RAJASTHAN', 'TAMIL NADU', 'HARYANA', 'KARNATAKA', 'GOA', 'DADRA & NAGAR HAVELI', 'MIZORAM', 'HIMACHAL PRADESH', 'PONDICHERRY', 'ARUNACHAL PRADESH', 'MADHYA PRADESH', 'DELHI', 'SIKKIM', 'TELANGANA', 'DAMAN & DIU', 'CHANDIGARH', 'BIHAR',  'ASSAM', 'PUNJAB', 'LAKSHADWEEP', 'ANDHRA PRADESH', 'CHATTISGARH', 'UTTARAKHAND', 'ODISHA', 'MEGHALAYA', 'KERALA', 'NAGALAND', 'TRIPURA', 'JHARKHAND', 'JAMMU & KASHMIR', 'WEST BENGAL', 'MAHARASHTRA', 'ANDAMAN & NICOBAR ISLANDS']
var_name_dict = {'MANIPUR': 'MANIPUR', 'UTTAR PRADESH': 'UTTARPRADESH', 'GUJARAT': 'GUJARAT', 'RAJASTHAN': 'RAJASTHAN', 'TAMIL NADU': 'TAMILNADU', 'HARYANA': 'HARYANA', 'KARNATAKA': 'KARNATAKA', 'GOA': 'GOA', 'DADRA & NAGAR HAVELI': 'DADRANAGARHAVELI', 'MIZORAM': 'MIZORAM', 'HIMACHAL PRADESH': 'HIMACHALPRADESH', 'PONDICHERRY': 'PONDICHERRY', 'ARUNACHAL PRADESH': 'ARUNACHALPRADESH', 'MADHYA PRADESH': 'MADHYA PRADESH', 'DELHI': 'DELHI', 'SIKKIM': 'SIKKIM', 'TELANGANA': 'TELANGANA', 'DAMAN & DIU': 'DAMANDIU', 'CHANDIGARH': 'CHANDIGARH', 'BIHAR': 'BIHAR', 'ASSAM': 'ASSAM', 'PUNJAB': 'PUNJAB', 'LAKSHADWEEP': 'LAKSHADWEEP', 'ANDHRA PRADESH': 'ANDHRAPRADESH', 'CHATTISGARH': 'CHATTISGARH', 'UTTARAKHAND': 'UTTARAKHAND', 'ODISHA': 'ODISHA', 'MEGHALAYA': 'MEGHALAYA', 'KERALA': 'KERALA', 'NAGALAND': 'NAGALAND', 'TRIPURA': 'TRIPURA', 'JHARKHAND': 'JHARKHAND', 'JAMMU & KASHMIR': 'JAMMUKASHMIR', 'WEST BENGAL': 'WESTBENGAL', 'MAHARASHTRA': 'MAHARASHTRA', 'ANDAMAN & NICOBAR ISLANDS': 'ANDAMANNICOBARISLANDS'}
for a in var_name_dict:
    globals()[var_name_dict[a]] = list()
for a in cont[1:]:
    try:
        globals()[var_name_dict[a[-1]]].append(a)
    except:
        pass
        # print (a[-1])
print(globals()["TAMILNADU"])
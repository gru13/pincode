import csv
from os import stat
from typing import List
file = open("./Locality_village_pincode_final_mar-2017.csv")
cont = list(csv.reader(file))
# 
states = ['CHANDIGARH', 'MADHYAPRADESH', 'BIHAR', 'ANDHRA PRADESH', 'WEST BENGAL', 'HARYANA', 'MANIPUR', 'RAJASTHAN', 'JAMMU & KASHMIR', 'GUJARAT', 'ANDAMAN & NICOBAR ISLANDS', 'KARNATAKA', 'StateName', 'CHATTISGARH', 'JHARKHAND', 'NAGALAND', 'TRIPURA', 'PONDICHERRY', 'GOA', 'ARUNACHAL PRADESH', 'TELANGANA', 'TAMIL NADU', 'LAKSHADWEEP', 'DELHI', 'UTTARAKHAND', 'MAHARASHTRA', 'DADRA & NAGAR HAVELI', 'MEGHALAYA', 'MIZORAM', 'DAMAN & DIU', 'HIMACHAL PRADESH', 'ASSAM', 'PUNJAB', 'UTTAR PRADESH', 'ODISHA', 'SIKKIM', 'KERALA']
for a in states:
    globals()[a] = list()
heading = cont[0]
for a in cont[1:]:
    globals()[a[-1]].append(a)
print(TAMIL NADU)
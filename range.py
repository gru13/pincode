import csv
#find the range of pincode
var_name_dict = {'MANIPUR': ['MANIPUR'], 'UTTAR PRADESH': ['UTTARPRADESH'], 'GUJARAT': ['GUJARAT'], 'RAJASTHAN': ['RAJASTHAN'], 'TAMIL NADU': ['TAMILNADU'], 'HARYANA': ['HARYANA'], 'KARNATAKA': ['KARNATAKA'], 'GOA': ['GOA'], 'DADRA & NAGAR HAVELI': ['DADRANAGARHAVELI'], 'MIZORAM': ['MIZORAM'], 'HIMACHAL PRADESH': ['HIMACHALPRADESH'], 'PONDICHERRY': ['PONDICHERRY'], 'ARUNACHAL PRADESH': ['ARUNACHALPRADESH'], 'MADHYA PRADESH': ['MADHYA PRADESH'], 'DELHI': ['DELHI'], 'SIKKIM': ['SIKKIM'], 'TELANGANA': ['TELANGANA'], 'DAMAN & DIU': [
    'DAMANDIU'], 'CHANDIGARH': ['CHANDIGARH'], 'BIHAR': ['BIHAR'], 'ASSAM': ['ASSAM'], 'PUNJAB': ['PUNJAB'], 'LAKSHADWEEP': ['LAKSHADWEEP'], 'ANDHRA PRADESH': ['ANDHRAPRADESH'], 'CHATTISGARH': ['CHATTISGARH'], 'UTTARAKHAND': ['UTTARAKHAND'], 'ODISHA': ['ODISHA'], 'MEGHALAYA': ['MEGHALAYA'], 'KERALA': ['KERALA'], 'NAGALAND': ['NAGALAND'], 'TRIPURA': ['TRIPURA'], 'JHARKHAND': ['JHARKHAND'], 'JAMMU & KASHMIR': ['JAMMUKASHMIR'], 'WEST BENGAL': ['WESTBENGAL'], 'MAHARASHTRA': ['MAHARASHTRA'], 'ANDAMAN & NICOBAR ISLANDS': ['ANDAMANNICOBARISLANDS']}

# ###########################################################
# every data is assigned as "Village/Locality name,Areaname,Pincode,Sub-distname,Districtname,StateName"

for a in var_name_dict:
    with open("./DATA/"+a+".csv", "r") as f:
        lst_of_pincode = list(csv.reader(f))
        lst_of_pincode = [a for a in lst_of_pincode if a != []]
        # print(lst_of_pincode[0][-1],lst_of_pincode[0][2],lst_of_pincode[-1][2])
        var_name_dict[a].append(lst_of_pincode[0][2])
        var_name_dict[a].append(lst_of_pincode[-1][2])
print(var_name_dict)
"""
output of code
{'MANIPUR': ['MANIPUR', '795001', '795159'], 'UTTAR PRADESH': ['UTTARPRADESH', '201001', '571439'], 'GUJARAT': ['GUJARAT', '360001', '396590'], 'RAJASTHAN': ['RAJASTHAN', '301001', '345034'], 'TAMIL NADU': ['TAMILNADU', '517401', '643253'], 'HARYANA': ['HARYANA', '121001', '136156'], 'KARNATAKA': ['KARNATAKA', '560001', '591345'], 'GOA': ['GOA', '403001', '403806'], 'DADRA & NAGAR HAVELI': ['DADRANAGARHAVELI', '396193', '396240'], 'MIZORAM': ['MIZORAM', '796001', '796901'], 'HIMACHAL PRADESH': ['HIMACHALPRADESH', '171001', '177601'], 'PONDICHERRY': ['PONDICHERRY', '605001', '609609'], 'ARUNACHAL PRADESH': ['ARUNACHALPRADESH', '790001', '792131'], 'MADHYA PRADESH': ['MADHYA PRADESH', '450001', '488448'], 'DELHI': ['DELHI', '110003', '110090'], 'SIKKIM': ['SIKKIM', '737101', '737139'], 'TELANGANA': ['TELANGANA', '500001', '533352'], 'DAMAN & DIU': ['DAMANDIU', '362520', '396220'],
     'CHANDIGARH': ['CHANDIGARH', '140308', '160103'], 'BIHAR': ['BIHAR', '800001', '855117'], 'ASSAM': ['ASSAM', '781001', '788931'], 'PUNJAB': ['PUNJAB', '140001', '160104'], 'LAKSHADWEEP': ['LAKSHADWEEP', '682551', '682559'], 'ANDHRA PRADESH': ['ANDHRAPRADESH', '515001', '635121'], 'CHATTISGARH': ['CHATTISGARH', '490001', '497778'], 'UTTARAKHAND': ['UTTARAKHAND', '244712', '263680'], 'ODISHA': ['ODISHA', '751001', '770076'], 'MEGHALAYA': ['MEGHALAYA', '781029', '794115'], 'KERALA': ['KERALA', '670001', '695615'], 'NAGALAND': ['NAGALAND', '797001', '798627'], 'TRIPURA': ['TRIPURA', '799001', '799290'], 'JHARKHAND': ['JHARKHAND', '813208', '835325'], 'JAMMU & KASHMIR': ['JAMMUKASHMIR', '180001', '194404'], 'WEST BENGAL': ['WESTBENGAL', '700001', '743711'], 'MAHARASHTRA': ['MAHARASHTRA', '400001', '445402'], 'ANDAMAN & NICOBAR ISLANDS': ['ANDAMANNICOBARISLANDS', '744101', '744304']}
"""
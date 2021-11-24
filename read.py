import csv



var_name_dict = {'MANIPUR': ['MANIPUR'], 'UTTAR PRADESH': ['UTTARPRADESH'], 'GUJARAT': ['GUJARAT'], 'RAJASTHAN': ['RAJASTHAN'], 'TAMIL NADU': ['TAMILNADU'], 'HARYANA': ['HARYANA'], 'KARNATAKA': ['KARNATAKA'], 'GOA': ['GOA'], 'DADRA & NAGAR HAVELI': ['DADRANAGARHAVELI'], 'MIZORAM': ['MIZORAM'], 'HIMACHAL PRADESH': ['HIMACHALPRADESH'], 'PONDICHERRY': ['PONDICHERRY'], 'ARUNACHAL PRADESH': ['ARUNACHALPRADESH'], 'MADHYA PRADESH': ['MADHYA PRADESH'], 'DELHI': ['DELHI'], 'SIKKIM': ['SIKKIM'], 'TELANGANA': ['TELANGANA'], 'DAMAN & DIU': [
    'DAMANDIU'], 'CHANDIGARH': ['CHANDIGARH'], 'BIHAR': ['BIHAR'], 'ASSAM': ['ASSAM'], 'PUNJAB': ['PUNJAB'], 'LAKSHADWEEP': ['LAKSHADWEEP'], 'ANDHRA PRADESH': ['ANDHRAPRADESH'], 'CHATTISGARH': ['CHATTISGARH'], 'UTTARAKHAND': ['UTTARAKHAND'], 'ODISHA': ['ODISHA'], 'MEGHALAYA': ['MEGHALAYA'], 'KERALA': ['KERALA'], 'NAGALAND': ['NAGALAND'], 'TRIPURA': ['TRIPURA'], 'JHARKHAND': ['JHARKHAND'], 'JAMMU & KASHMIR': ['JAMMUKASHMIR'], 'WEST BENGAL': ['WESTBENGAL'], 'MAHARASHTRA': ['MAHARASHTRA'], 'ANDAMAN & NICOBAR ISLANDS': ['ANDAMANNICOBARISLANDS']}

# ###########################################################
# every data is assigned as "Village/Locality name,Areaname,Pincode,Sub-distname,Districtname,StateName"

for a in var_name_dict:
    with open("./DATA/"+a+".csv", "r") as f:
        lst_of_pincode = list(csv.reader(f))
        lst_of_pincode = [a for a in lst_of_pincode if a !=[]]
        
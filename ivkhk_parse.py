import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

'''
# -------------------Countries parse-----------------

country = ET.parse('countries.xml')
root = country.getroot()

roots = []

for item in root.findall('./country'):
    countries = {}
    countries['country_name'] = item.attrib['name']
    for child in item:
        if child.tag == 'symbol':
            countries['symbol'] = child.text
        if child.tag == 'currency':
            countries['currency'] = child.text
        if child.tag == 'year':
            countries['year'] = child.text
    roots.append(countries)
print(roots)

# -------------------------------------------------------
'''

# ivkhk = ET.parse('Dzjubenko_ivkhk.xml')  
# staff = ivkhk.getroot()

# staffs = []

# for item in staff.findall('./department'):
#     sphere = {}
#     sphere['department_name'] = item.attrib['name']
#     for child in item:
#         if child.tag == 'speciality':
#             sphere['speciality'] = child.attrib['spec']
#     staffs.append(sphere)
# for item in staff.findall('.//group'):
#     sphere = {}
#     sphere['group_name'] = item.attrib['grname']
#     for child in item:
#         if child.tag == 'student':
#             sphere['student'] = child.text
#     staffs.append(sphere)
# print(staffs)        
    


# -------------------IVKHK parse-----------------

with open('Dzjubenko_ivkhk.xml', 'r') as f:
    data = f.read()
staff = BeautifulSoup(data, features = "xml")
staffs = staff.find_all('staff')
departments = staff.find_all('department')
specialities = staff.find_all('speciality')
groups = staff.find_all('group')
students = staff.find_all('student')


for staff in departments:
    departmentName = staff.get("name")
    for staff in specialities:
        specialityName = staff.get("spec")
        for staff in groups:
            groupName = staff.get("grname")
            for student in students:
                print(staff.get_text())

for staff in staffs:    
    print("====================")
    print(departmentName)
    print(specialityName)
    print(groupName)
    print(students)
    print("====================")

# -------------------------------------------------------
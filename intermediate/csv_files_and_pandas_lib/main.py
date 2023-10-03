import csv
import pandas

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp.isdigit():
#             temperatures.append(int(temp))
#
#     print(temperatures)

data = pandas.read_csv('weather_data.csv')
# print(data)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()

average_temp = data['temp'].mean()
max_temp = data['temp'].max()

"""
Get Data in Column
print(data.day) or print(data['day])
"""

"""
Get Data in Row
"""
# print(data[data.temp == max_temp])
# print(data[data.day == 'Monday'])

# monday = data[data.day == 'Monday']
# print(monday)
# fahrenheit_temp = (monday.temp * 1.8) + 32
# print(fahrenheit_temp)

students_file = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 21, 32]
}

students_data = pandas.DataFrame(students_file)
print(students_data)
students_data.to_csv('students_data.csv')

current_student = students_data[students_data.students == 'Amy']
print(current_student.scores[0])

s_file = pandas.read_csv('students_data.csv')
c_s = s_file[s_file.students == 'Amy']
print(c_s.scores)

"""
HOW TO ITERATE THROUGH PANDAS DATA FRAME
"""
students_dict = {
    'students': ['Ana', 'James', 'Lilly'],
    'score': [56, 43, 98]
}

students_data = pandas.DataFrame(students_dict)
print(students_data)
print()

for index, row in students_data.iterrows():
    print(row.score)

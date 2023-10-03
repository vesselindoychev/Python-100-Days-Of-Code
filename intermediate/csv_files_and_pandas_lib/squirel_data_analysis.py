import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

data_by_column = squirrel_data['Primary Fur Color']
gray_fur_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_fur_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_fur_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

squirrel_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [gray_fur_squirrel_count, cinnamon_fur_squirrel_count, black_fur_squirrel_count]
}

squirrel_data_file = pandas.DataFrame(squirrel_dict)
squirrel_data_file.to_csv('squirrel_count')
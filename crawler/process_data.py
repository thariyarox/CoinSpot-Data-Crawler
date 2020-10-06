import csv
import os

csv_path = os.path.join(os.path.dirname(__file__), "../data/test_data.csv")
new_csv_path = os.path.join(os.path.dirname(__file__), "processed_data.csv")
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    with open(new_csv_path, 'w') as processed_csv_file:
        csv_writer = csv.writer(processed_csv_file, delimiter = ',')
        line_counter = 0
        for row in csv_reader:
            processed_row = row
            if line_counter != 0:
                for index, element in enumerate(row):
                    if element == '':
                        processed_row[index] = 0
                    elif index in range(2,6):
                        stripped_value = row[index][1:].replace(',', '')
                        if stripped_value.endswith('M'):
                            stripped_value = float(stripped_value[:-1]) * 10**6
                        elif stripped_value.endswith('B'):
                            stripped_value = float(stripped_value[:-1]) * 10**9
                        processed_row[index] = stripped_value
            csv_writer.writerow(processed_row)
            line_counter += 1


            

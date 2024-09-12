import csv
# Open the CSV file for reading
with open('studentsData.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # Read the header (first row)
    header = next(csv_reader)
    print(f"Header: {header}")
    # Read the remaining rows
    for row in csv_reader:
        print(row)
# Data to write
data = [
    ['Name', 'Age', 'Grade'],
    ['Eve', 14, 'B'],
    ['Frank', 16, 'A'],
    ['Grace', 15, 'B']
]
# Open a new CSV file for writing
with open('new_students.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    # Write the data
    csv_writer.writerows(data)
print("Data written to new_students.csv")
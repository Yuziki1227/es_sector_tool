import csv

def read_csv(file_path, encoding='gb2312'):
    with open(file_path, 'r', encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)

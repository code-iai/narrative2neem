import csv


def write(header, rows, csv_file_path):
    with open(csv_file_path, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(header)

        for row in rows:
            writer.writerow(row)

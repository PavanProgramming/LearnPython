import csv

# # reading the csv file data
# with open('names.csv','r') as csv_file:
#     csvReaderData = csv.reader(csv_file)
#     print(csvReaderData)  # provide the object location
#     for line in csvReaderData:
#         print(line)
#
# # print(csv_file.closed)
# # print(csvReaderData)

# # reading the specific data
# with open('names.csv','r') as csv_file:
#     csvReaderData = csv.reader(csv_file)
#     print(csvReaderData)  # provide the object location
#
#     next(csvReaderData)  # omits the first row data
#     for line in csvReaderData:
#         print(line[2])

# # writing the data
# with open('names.csv','r') as csv_file:
#     csvReaderData = csv.reader(csv_file)
#
#     with open('newNames.csv','w') as new_file:  # creates a new line depends on platform
#         csv_writer = csv.writer(new_file,delimiter='-')
#
#         for line in csvReaderData:
#             print(line)
#             csv_writer.writerow(line)

# # writing the data
# with open('names.csv', 'r') as csv_file:
#     csvReaderData = csv.reader(csv_file)
#
#     with open('newNames.csv', 'w', newline='') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csvReaderData:
#             csv_writer.writerow(line)
#
# # reader the new file data
# with open('newNames.csv', 'r') as csv_file:
#     csvReaderData = csv.reader(csv_file, delimiter = '\t')
#
#     for line in csvReaderData:
#         print(line)


# # using dictionary reader
# with open('names.csv', 'r') as csv_file:
#     csvReaderData = csv.DictReader(csv_file)
#
#     for line in csvReaderData:
#         # print(line)
#         print(line['email'])


# using dictionary reader
with open('names.csv', 'r') as csv_file:
    csvReaderData = csv.DictReader(csv_file)

    with open('newDictnames.csv', 'w', newline='') as new_file:
        # with dictionary writer you have to tell about field names
        fieldnameslist = ['first_name', 'last_name', 'email']
        csvWriterData = csv.DictWriter(new_file, fieldnames= fieldnameslist, delimiter='\t')
        csvWriterData.writeheader()
        for line in csvReaderData:
            del line['email'] # will delete the 'email' column
            csvWriterData.writerow(line)



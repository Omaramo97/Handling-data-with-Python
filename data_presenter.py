open_file = open("CupcakeInvoices.csv")

for row in open_file:
    print(row)

for row in open_file:
    values = row.split(',')
    print(values[4])

for row in open_file:
    values = row.split(',')
    total = int(values[3]) * float (values[4])
    print (total)


total = 0

for row in open_file:
    values = row.split(',')
    total = total + int(values[3]) * float (values[4])
    print(total)


7.) open_file.close()
import csv
file = input("which file do you want to use? ")
f = open(file, "r")
rows = csv.reader(f)
headers = next(rows)
sum = 0
for row in rows:
    try:
        share = int(row[1])
        #print(share)
        price = float(row[2].strip())
        row_total = share*price
        #print(row_total)
    except ValueError:
        print("Couldn't get either share and/or price", row)

    sum = sum + row_total
    # sum += row_total

print("total cost:", sum)

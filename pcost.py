sum = 0

with open("portfolio.csv","rt") as file:
    headers = next(file)
    for line in file:
        row = line.split(",")
        print(row)
        share = int(row[1])
        #print(share)
        price = float(row[2].strip())
        row_total = share*price
        #print(row_total)

        sum = sum + row_total
        # sum += row_total

print(sum)



def portfolio_cost(filename):
    sum = 0
    with open(filename,"rt") as file:
        headers = next(file)
        for line in file:
            try:
                row = line.split(",")
                print(row)
                share = int(row[1])
                #print(share)
                price = float(row[2].strip())
                row_total = share*price
                #print(row_total)
            except ValueError:
                print("Couldn't get either share and/or price", line)

            sum = sum + row_total
            # sum += row_total
    return sum

cost = portfolio_cost("missing.csv")
print("total cost:", cost)

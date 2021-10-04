height = 100
bounce = 0

while bounce <= 9:
    height = height * (3/5)
    bounce = bounce + 1
    print(bounce, round(height,2))

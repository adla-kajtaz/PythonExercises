squares = [x ** 2 for x in range(1, 11)]

filtered_squares = list(filter(lambda x: 30 <= x <= 70, squares))

print (filtered_squares)

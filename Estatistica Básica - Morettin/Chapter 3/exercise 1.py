def mean(data, frequency):
    initial = 1
    total = data[0] * frequency[0]
    while initial < len(data):
        total += data[initial] * frequency[initial]
        initial += 1
    return total/sum(frequency)

books_error_data = { 0:25,
                    1:20,
                    2:3,
                    3:1,
                    4:1
} 

print(mean(list(books_error_data.keys()), list(books_error_data.values())))
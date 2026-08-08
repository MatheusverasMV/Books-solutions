books_error_data = { 0:25,
                    1:20,
                    2:3,
                    3:1,
                    4:1
} 

def mean(data, frequency):
    initial = 1
    total = data[0] * frequency[0]
    while initial < len(data):
        total += data[initial] * frequency[initial]
        initial += 1
    return total/sum(frequency)

def median(data, frequency):
    if len(data) % 2 == 0:
        median1 = data[len(data)//2 - 1]
        median2 = data[len(data)//2]
        return (median1 + median2) / 2
    else:
        return data[len(data)//2]


print(f"Mean: {mean(list(books_error_data.keys()), list(books_error_data.values()))}")
print(f"Median: {median(list(books_error_data.keys()), list(books_error_data.values()))}")

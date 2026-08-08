taxes = [2.59, 2.64, 2.60, 2.62, 2.57, 2.55, 2.61, 2.50, 2.63, 2.64]

def mean(data, frequency):
    initial = 1
    total = data[0] * frequency[0]
    while initial < len(data):
        total += data[initial] * frequency[initial]
        initial += 1
    return total/sum(frequency)

def median(data):
    if len(data) % 2 == 0:
        median1 = data[len(data)//2 - 1]
        median2 = data[len(data)//2]
        return (median1 + median2) / 2
    else:
        return data[len(data)//2]

def variance(data, frequency):
    xi = mean(data, frequency)
    initial = 0
    total = 0
    while initial < len(data):
        total += frequency[initial] * (data[initial] - xi) ** 2
        initial += 1
    return total / sum(frequency)

def standard_deviation(data, frequency):
    return variance(data, frequency) ** 0.5

print(f"Mean: {mean(taxes, [1]*len(taxes))}")
print(f"Median: {median(taxes)}")
print(f"Standard Deviation: {standard_deviation(taxes, [1]*len(taxes))}")
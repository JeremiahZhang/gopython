from math import sqrt

def get_numbers():
    x_str = input("Please enter the number: ")
    data = []

    while x_str != "":
        x = eval(x_str)
        data.append(x)

        x_str = input("Please enter the number(<Enter> to exit): ")

    return data

def mean(data_list):
    data_mean = 0.0

    for data in data_list:
        data_mean += data

    data_mean /= len(data_list)

    return data_mean

def std_dev(data_list, x_bar):
    std = 0.0

    for data in data_list:
        std += (data - x_bar) ** 2

    std /= (len(data_list) - 1)
    std = sqrt(std)

    return std

def median(data_list):
    data_list.sort() # data_list mutated
    size = len(data_list) % 2
    mid_pos = len(data_list) // 2

    if not size: # even
        median = (data_list[mid_pos] + data_list[mid_pos-1]) / 2.0
    else: # odd
        median = data_list[mid_pos]

    return median

def main():
    print("This program computes mean, median and standard deviation.")

    data = get_numbers()
    x_bar = mean(data)
    std = std_dev(data, x_bar)
    med = median(data)

    print("\nThe mean is {}".format(x_bar))
    print("The standard deviation is {}".format(std))
    print("The median is {}".format(med))

if __name__ == '__main__':
    main()

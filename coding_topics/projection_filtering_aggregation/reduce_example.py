from functools import reduce

if __name__ == "__main__":
    daily_temperatures = [14, 16, 13, 17, 18, 16, 16]

    temperature_counts = reduce(
        lambda frequency, value: {**frequency, value: frequency.get(value, 0) + 1},
        daily_temperatures,
        {},
    )
    most_frequent_temp = max(temperature_counts, key=temperature_counts.get)

    print("Most Frequent Temperature:", most_frequent_temp)

if __name__ == '__main__':
    while True:
        new_values = input("Give the new values separated with space (ex. 40.9 39.9 43.4) if empty then stop: ")
        if new_values == "":
            break
        old_ref = input("Give the old range numbers with a hyphen (ex. 13-17): ")
        old_middle = (int(old_ref.split("-")[1]) + int(old_ref.split("-")[0])) / 2
        old_distance_from_middle_in_percent = ((old_middle - int(old_ref.split("-")[0])) / old_middle) * 100
        tmp = 0.0
        for i in new_values.split(" "):
            tmp += float(i)
        new_average = tmp / len(new_values.split(" "))
        lower = round(new_average - new_average * old_distance_from_middle_in_percent / 100)
        higher = round(new_average + new_average * old_distance_from_middle_in_percent / 100)
        print("New range: " + str(lower) + " - " + str(higher))

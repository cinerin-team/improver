def new_value_calc(new_values, o1, o2):
    # new_values = input("Give the new values separated with space (ex. 40.9 39.9 43.4) if empty then stop: ")
    # old_ref = input("Give the old range numbers with a hyphen (ex. 13-17): ")
    old_middle = (int(o1) + int(o2)) / 2
    old_distance_from_middle_in_percent = ((old_middle - int(o1)) / old_middle) * 100
    tmp = 0.0
    for i in new_values:
        tmp += float(i)
    new_average = tmp / len(new_values)
    lower = round(new_average - new_average * old_distance_from_middle_in_percent / 100)
    higher = round(new_average + new_average * old_distance_from_middle_in_percent / 100)
    return [str(lower), str(higher)]
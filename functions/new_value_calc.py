def new_value_calc(new_average_loc, o1, o2):
    old_middle = (float(o1) + float(o2)) / 2
    print(old_middle)
    old_distance_from_middle_in_percent = old_middle - float(o1)
    print(old_distance_from_middle_in_percent)
    lower = round(new_average_loc - old_distance_from_middle_in_percent, 2)
    higher = round(new_average_loc + old_distance_from_middle_in_percent, 2)
    return [str(lower), str(higher)]

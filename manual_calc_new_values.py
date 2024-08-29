import argparse

from functions.new_value_calc import new_value_calc

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # new_value_calc(new_average_loc, o1, o2)
    parser.add_argument("-n", "--new_average", type=float, required=True, help='the new value')
    parser.add_argument("-o1", "--old_lower", type=float, required=True, help='the old lower value')
    parser.add_argument("-o2", "--old_higher", type=float, required=True, help='the old higher value')

    args = parser.parse_args()
    n = new_value_calc(args.new_average, args.old_lower, args.old_higher)

    print(f'new lower value: {n[0]} new higher value: {n[1]}')
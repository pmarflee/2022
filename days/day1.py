def calculate(lines, part):
    slice_end = 1 if part == 1 else 3
    calories_list = []
    calories = 0
    for line in lines:
        if len(line) == 0:
            calories_list.append(calories)
            calories = 0
        else:
            calories += int(line)
    calories_list.append(calories)
    calories_list.sort()
    calories_list.reverse()
    return sum(calories_list[0:slice_end])
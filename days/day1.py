def calculate(lines, part):
    max_calories = 0
    calories = 0
    for line in lines:
        if len(line) == 0:
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line)
    return max_calories
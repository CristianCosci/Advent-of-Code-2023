from math import prod
cubes_dict_rule = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt') as f:
    lines = f.readlines()
    game_power_sum = 0
    for line in lines:
        possible_configuration = True
        splitted_line = line.strip().split(': ') #['Game 1', '18 red, 8 green, 7 blue; 15 red, 4 blue, 1 green']
        game_num = int(splitted_line[0][5:])
        extraction_list = splitted_line[1].split('; ') #['18 red, 8 green, 7 blue', '15 red, 4 blue, 1 green']
        cubes_dict = {'red': 0, 'green': 0, 'blue': 0}
        for extracion in extraction_list:
            draw_list = extracion.split(', ') #['18 red', '8 green', '7 blue']
            for draw in draw_list:
                num, color = draw.split(' ')
                num = int(num)

                if cubes_dict[color] < num:
                    cubes_dict[color] = num
    
        game_power_sum += prod(list(cubes_dict.values()))

    print(game_power_sum)
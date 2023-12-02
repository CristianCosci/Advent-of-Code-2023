cubes_dict_rule = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt') as f:
    lines = f.readlines()
    game_sum = 0
    for line in lines:
        possible_configuration = True
        # Each comment explain the series of splitting
        splitted_line = line.strip().split(': ') #['Game 1', '18 red, 8 green, 7 blue; 15 red, 4 blue, 1 green']
        game_num = int(splitted_line[0][5:])
        extraction_list = splitted_line[1].split('; ') #['18 red, 8 green, 7 blue', '15 red, 4 blue, 1 green']
        for extracion in extraction_list:
            draw_list = extracion.split(', ') #['18 red', '8 green', '7 blue']
            for draw in draw_list:
                num, color = draw.split(' ')
                num = int(num)

                # if the draws is greater than the rule invalidate the game
                if cubes_dict_rule[color] < num:
                    possible_configuration = False
                    break
            
            if not possible_configuration:
                break
        
        if possible_configuration:
            game_sum += game_num
        
    print(game_sum)
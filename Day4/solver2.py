with open('input.txt') as f:
    card_points_dict = {}
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(': ')
        card_num = int(line[0].split(' ')[-1])

        scratchcards = line[1].split(' | ')
        winning_numbers_string = scratchcards[0].split(' ')
        your_numbers_string = scratchcards[1].split(' ')

        winning_numbers = []
        your_numbers = []
        for x in winning_numbers_string:
            if x.isdigit():
                winning_numbers.append(int(x))
        
        for x in your_numbers_string:
            if x.isdigit():
                your_numbers.append(int(x))

        # count of winning numbers that you have
        num_winning_number =  len([x for x in your_numbers if x in winning_numbers])
        
        card_points_dict[card_num] = num_winning_number

    

    card_points_amount = {}

    for scratchcards in card_points_dict.keys():
        card_points_amount[scratchcards] = 1

    for scratchcards in card_points_dict.keys():
        for i in range(card_points_dict[scratchcards]):
            card_points_amount[scratchcards+i+1] = card_points_amount[scratchcards+1+i] + card_points_amount[scratchcards]
        
    
    print(sum(card_points_amount.values()))
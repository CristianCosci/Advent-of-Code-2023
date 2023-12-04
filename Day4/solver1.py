with open('input.txt') as f:
    points = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(': ')
        scratchcards = line[1].split(' | ')
        winning_numbers_string = scratchcards[0].split(' ')
        your_numbers_string = scratchcards[1].split(' ')
        print(your_numbers_string)
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
        print(num_winning_number)
        if not num_winning_number == 0:
            points += 2**(num_winning_number-1)


    print(points)

    
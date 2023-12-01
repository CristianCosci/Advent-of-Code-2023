with open('input.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = []
        for character in line.strip():
            if character.isdigit():
                nums.append(int(character))
    
        sum += nums[0]*10 + nums[-1]

    print(sum)
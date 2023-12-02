with open('input.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = []
        for character in line.strip():
            if character.isdigit():
                # Create a List of all number in the string
                nums.append(int(character))

        # Create the number and sum it using the first and the last in the list
        sum += nums[0]*10 + nums[-1]

    print(sum)
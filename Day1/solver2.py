import re

nums_string = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

with open('input.txt') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = []
        count = 0
        for character in line.strip():
            if character.isdigit():
                nums.append((int(character), count))
            count += 1
        
        for num_string in nums_string.keys():
            pos = [m.start() for m in re.finditer('(?='+num_string+')', line)]
            if len(pos) > 0:
                for index in pos:
                    nums.append((nums_string[num_string], index))

        nums.sort(key=lambda x: x[1])

        sum += nums[0][0]*10 + nums[-1][0]

    print(sum)
with open('input.txt') as f:
    matrix = []
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','.')
        matrix_line = line.strip()
        matrix_line = [x for x in matrix_line]
        matrix.append(matrix_line)

    sum = 0
    for i in range(len(matrix)): # rows
        nums = []
        count = 0
        num_find = False
        for j in range(len(matrix[0])): # cols
            if matrix[i][j].isdigit():
                    nums.append(int(matrix[i][j]))
                    count += 1
                    num_find = True
            elif num_find:
                num = 0
                for x in nums:
                    count -= 1
                    num += x*10**count

                to_sum = False
                num_len = len(str(num))
                
                print(num)
                if num == 388:
                    print('ok')
                for x in range(num_len):
                    # UP
                    if i > 0 and (not matrix[i-1][j-num_len+x].isdigit()) and matrix[i-1][j-num_len+x] != '.':
                        print('su')
                        to_sum = True
                        break
                    
                    # LEFT
                    if j > 0 and not matrix[i][j-num_len+x-1].isdigit() and matrix[i][j-num_len+x-1] != '.':
                        print('sinistra')
                        to_sum = True
                        break

                    # DOWN
                    if i < len(matrix)-1 and (not matrix[i+1][j-num_len+x].isdigit()) and matrix[i+1][j-num_len+x] != '.':
                        print('giu')
                        to_sum = True
                        break

                    # RIGHT
                    if j < len(matrix[0])-1 and (not matrix[i][j-num_len+x+1].isdigit()) and matrix[i][j-num_len+x+1] != '.':
                        print('destra')
                        to_sum = True
                        break

                    # UP-RIGHT
                    if i > 0 and j < len(matrix[0])-1 and (not matrix[i-1][j-num_len+x+1].isdigit()) and matrix[i-1][j-num_len+x+1] != '.':
                        print('su-destra')
                        to_sum = True
                        break

                    # UP-LEFT
                    if i > 0 and j > 0 and (not matrix[i-1][j-num_len+x-1].isdigit()) and matrix[i-1][j-num_len+x-1] != '.':
                        print('su-sinistra')
                        to_sum = True
                        break

                    # DOWN-LEFT
                    if i < len(matrix)-1 and j > 0 and (not matrix[i+1][j-num_len+x-1].isdigit()) and matrix[i+1][j-num_len+x-1] != '.':
                        print('giu-sinistra')
                        to_sum = True
                        break

                    # DOWN-RIGHT
                    if i < len(matrix)-1 and j < len(matrix[0])-1 and (not matrix[i+1][j-num_len+x+1].isdigit()) and matrix[i+1][j-num_len+x+1] != '.':
                        print('giu-destra')
                        to_sum = True
                        break
                                
                
                if to_sum:
                    sum += num
                    print(num)
                    

                to_sum = False
                num_find = False
                nums = []
                count = 0


    print(sum)
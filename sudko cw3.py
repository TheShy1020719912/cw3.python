

grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]


def check_section(section, n):

    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False

def squares_value(grid, n_rows, n_cols):

    squares = []
    for i in range(n_cols):
        rows = (i*n_rows, (i+1)*n_rows)
        for j in range(n_rows):
            cols = (j*n_cols, (j+1)*n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square +=line
            squares.append(square)


    return(squares)



def solution_check(grid, n_rows, n_cols):
    
    
    n = n_rows*n_cols

    for row in grid:
        if check_section(row, n) == False:
            return False

    for i in range(n_rows**2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = squares_value(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False
    
    return True




#add the stuff in about finding the best zero.
def find_set(grid, row, col):
    
    
    givens = set()
    
    for i in range(4):
        row_no = grid[row][i]
#         print('row_no =',row_no)
        givens.add(row_no)
    
    for j in range(4):
        
        col_no = grid[j][col]
#         print('col_no =',col_no)
        givens.add(col_no)
    
    for k in range(4):
        if k//2== row//2:

            for l in range(4):
                if l//2 == col//2:

                    box_no = grid[k][l]

                    givens.add(box_no)
    

    
    total = set()
    for m in range(1,5):
        total.add(m)

    options = total - givens

    return options

   
def zero_value(grid):
    options_dict = {}
    for f in range(4):
        for g in range(4):
            if grid[f][g] == 0:
                
                options_dict[f, g] = find_set(grid, f, g)
    values = list(options_dict.values())
    if len(values) == 0:
        return None
    shortest = values[0]
    counter = 1
    index = 0

    while counter < len(values):
        len_shortest = len(shortest)

        l = values[counter]
        len_l = len(l)

        if len_l < len_shortest:
            shortest = l

            index = counter
        counter +=1
    zero = list(options_dict.items())[index]
    
    zero = list(zero)
    zero[1] = tuple(zero[1])
    return zero  
def recursive_solve(grid, n_rows, n_cols):
   # n = n_rows*n_cols
    zero = zero_value(grid)
    if not zero:
        
        if solution_check(grid, n_rows, n_cols):
            return grid 
        else:
           
            return None
    else:

        row = zero[0][0]
        col = zero[0][1]
        options = zero[1]

        for i in options:
        
            grid[row][col] = i
            ans = recursive_solve(grid, n_rows, n_cols)
            if ans:
                return ans 
            grid[row][col] = 0 

    return None

print(recursive_solve(grid1,2,2))
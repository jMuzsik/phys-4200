import numpy as np

# not sure how to get equations so...
equations = np.array([[2, 1, 4, 1], [3, 4, -1, -1],
                      [1, -4, 1, 5], [2, -2, 1, 3]], dtype=float)

results = np.array([-4, 3, 9, 7], dtype=float)

# now i want to solve each row
"""
  I can either subtract/add, multiply, or divide
  I would start at the first row and make the first indece 1
  Then move to the others and set that the first indece to 0
  on and on

  row indece traversal:
    Rows literally go through an infinite loop
    0, 1, 2, 3
    1, 2, 3, 0 
    2, 3, 0, 1
    3, 0, 1, 2

  idx traversal:
    0, 1, 2, 3 simple as this - four changes after entire iteration

  target update:
    1, 0 repeatedly
"""

# handles idx update
for idx in range(4):
  row = 0
  for i in range(4):
    # handles target update
    if i == 0:
      target = 1
    else:
      target = 0
    print(row, idx, target)
    # handle setting value to target
    # I can multiply the entire row for 1 to be at the start
    if target == 1:
      val = equations[row][idx]
      multiply_by = 1 / val
      equations[row] *= multiply_by
      results[row] *= multiply_by
    # I can subtract the first previous row * the current row to get 0
    # at the first index
    if target == 0:
      val = equations[row][idx]
      multiply_by = 1 * val
      prev_row = 0
      if row == 0:
        prev_row = 3
      else:
        prev_row = row - 1

      equations[row] = equations[row] - (equations[prev_row] * multiply_by)
      results[row] = results[row] - (results[prev_row] * multiply_by)
    
    # handles row indece update
    if row == 3:
      row = 0
    else:
      row += 1
    
print(equations, results)
      

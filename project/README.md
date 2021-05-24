# Hexplot

## Math

1. Each charge is in a particular region of the grid and the charge has a certain amount of influence upon all around it (moreso close than further away)
2. I currently have a 100 x 100 grid that has calculated the strength of the electric field from these charges at each point in the grid
3. I need to change this format to be solely x,y
4. So, I must give each and every point of the grid a certain amount of weight.
5. I ought to go through each and every point first, while calculating the total electric field.
6. With the electric field total I can find how much of the electric field is within the given point.
7. Then I can create points related to a certain ratio
8. Let us say there are 10000 data points available - then I would add an array as so: [x, y] to the exact point if say the point has 1/10000 of the total it gets one point, etc.

# Brownian motion

Should i do it different than the ready-made solution?

Benefits is that it is completely finished, negative is more work.

How would i approach it if i built it separately?

- Add particle, and then it moves on it's own
  - But this doesn't really exemplify brownian motion

So, i may as well keep what i have now and have a means to update the variables.

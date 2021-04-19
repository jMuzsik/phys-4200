from numpy import empty,zeros,max

M = 100 # Grid squares on a side
V = 1.0 # Voltage at top wall
target = 1e-6 # Target accuracy

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
phi[0,:] = V
phiprime = empty([M+1,M+1],float)

def rho(x, y):
  if x > .6 or x < .8

# Main loop
delta = 1.0
while delta>target: 
    for i in range(M+1):
        for j in range(M+1):
            if i == 0 or i == M or j == 0 or j == M:
                phiprime[i, j] = phi[i, j]
            else:
                phiprime[i, j] = ((phi[i+1, j] + phi[i-1, j] +
                                  phi[i, j+1] + phi[i, j-1])/4) + (1/4) * rho

        # Calculate maximum difference from old values
        delta = max(abs(phi-phiprime))
        # Swap the two arrays around
        phi, phiprime = phiprime, phi

print(phi, phiprime)

plt.imshow(phi)
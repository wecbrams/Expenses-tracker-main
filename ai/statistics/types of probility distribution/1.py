import scipy.stats as stats
# calculate the probability
prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("the probability of getting more than 6 heads in 10 coin flips is :", prob)

# Probability of exactly 6 rainy days
prob1 = stats.poisson.pmf(6, 10)
print("Probability of raining exactly 6 days:", prob1)

# Probability of raining 12–14 days
prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("Probability of raining for 12–14 days:", prob2)

# 1. Probability of more than 20 calls
prob1 = 1 - stats.poisson.cdf(20, 15)
print("Probability of more than 20 calls:", prob1)

# 2. Probability of between 17 and 21 calls
prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)
print("Probability of 17–21 calls:", prob2)
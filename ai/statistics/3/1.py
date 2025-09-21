import scipy.stats as stats

#probality of getting more than 20 events
prob1=1-stats.poisson.cdf(20,15)

print(prob1)
 # claculation of prob from 17 to 20\
prob2=stats.poisson.cdf(21, 15)-stats.poisson.cdf(16, 15)

print(prob2)
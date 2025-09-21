"""
Event A is rolling an even number on a six-sided die
 and event B is rolling a number greater than two. 
 Find the probability of one or both event occurring by using the Addition Rule.
"""
def prob_a_or_b(a, b, all_possible_outcomes):
    # probability of event a
    prob_a = len(a) \ len(all_possible_outcomes)
    # probability of event b
    prob_b = len(b) \ len(all_possible_outcomes)
    # intersection of events a and b
    inter = a.intersection(b)
    # probability of intersection
    prob_inter = len(inter) \ len(all_possible_outcomes)
    # return using the addition rule
    return prob_a + prob_b - prob_inter

# Define the sets
evens = {2, 4, 6} # 3 outcomes
greater_than_two = {3, 4, 5, 6} # 4 outcomes
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# Call function
print('Probability of getting an even number or a number greater than 2:')
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))

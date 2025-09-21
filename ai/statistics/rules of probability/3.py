def prob_a_or_b(a, b, all_possible_outcomes):
    # Probability of event A
    prob_a = len(a) / len(all_possible_outcomes)
    
    # Probability of event B
    prob_b = len(b) / len(all_possible_outcomes)
    
    # Intersection of events A and B
    inter = a.intersection(b)
    
    # Probability of intersection
    prob_inter = len(inter) / len(all_possible_outcomes)
    
    # Return probability of A or B
    return prob_a + prob_b - prob_inter

# Define the events using sets
evens = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# Call function and print result
print('Probability of getting an even number or a number greater than 2:')
print(prob_a_or_b(evens, greater_than_two, all_possible_rolls))

import random

def pick_ball_experiment():
    # Defining our balls as a list
    balls = ['Blue', 'Red', 'Green']
    
    # "Flipping" coins randomly, i.e., picking one ball at random
    result = random.choice(balls)
    
    # Finding the probability of picking a red ball
    pro = balls.count("Red") / len(balls)
    print("Probability of Picking Red Ball is:", pro)
    
    # Checking if red ball was picked
    if result == 'Red':
        return 'Red Ball was Picked'
    else:
        return 'Better Luck Next Time'

# Run the experiment
res = pick_ball_experiment()
print(res)

import random

# Define probabilities for each coin
probabilities = {
    'A': 0.6,
    'B': 0.3,
    'C': 0.1
}

# Number of simulations
num_simulations = 1_000_000

# Function to simulate a single trial
def simulate():
    # Randomly select a coin (each equally likely)
    coin = random.choice(list(probabilities.keys()))
    
    # Perform the first flip | if the random number is < than the proba the first flip is a head
    first_flip = random.random() < probabilities[coin]

    # If the first flip is heads, perform the second flip
    if first_flip:
        # if the second flip is less than the proba it is a head and we have a success
        second_flip = random.random() < probabilities[coin]
        return second_flip
    
    return None

# Run the Monte Carlo simulation
successes = 0
heads_after_heads = 0

for _ in range(num_simulations):
    result = simulate()
    if result is not None:  # First flip was heads
        successes += 1
        if result:  # Second flip was also heads | if its false than it was tails
            heads_after_heads += 1

# Calculate the probability
probability = heads_after_heads / successes

print(f"Estimated probability of heads on second flip given the first flip was heads: {probability:.4f}")

# investment_simulator.py

import random
import matplotlib.pyplot as plt

# ---------------------------
# Investment Simulator - Portfolio Diversification + Monte Carlo
# ---------------------------

print("Investment Simulator - Portfolio Diversification + Monte Carlo\n")

# Step 1: Get user input
starting_money = float(input("Enter your total investment amount: $"))

bond_amount = float(input("Enter amount to invest in Bond: $"))
stock_amount = float(input("Enter amount to invest in Stock: $"))
startup_amount = float(input("Enter amount to invest in Startup: $"))
shock_probability = 0.05  # 5% chance of extreme event

if bond_amount + stock_amount + startup_amount > starting_money:
    print("Allocation exceeds total investment. Please restart and enter valid amounts.")
    exit()

# Step 2: Define risk ranges
risk_ranges = {
    "Bond": (0.01, 0.03),     # Low risk
    "Stock": (-0.05, 0.08),    # Medium risk
    "Startup": (-0.05, 0.15)  # High risk
}

portfolio = {
    "Bond": bond_amount,
    "Stock": stock_amount,
    "Startup": startup_amount
}

# Step 3: Single simulation run
results = {}
for asset, amount in portfolio.items():
    min_r, max_r = risk_ranges[asset]
    results[asset] = amount * (1 + random.uniform(min_r, max_r))

total_value = sum(results.values())

print("\nSingle Simulation Portfolio Results:")
for asset, value in results.items():
    print(f"{asset}: ${value:.2f}")
print(f"Total Portfolio Value: ${total_value:.2f}")

print("\nExplanation:")
print("Diversifying across multiple assets reduces overall risk.")
print("Bonds are low risk, Stocks are medium risk, and Startups are high risk.")
print("This simulation shows how different allocations can affect your portfolio outcome.")

# Step 4: Monte Carlo Simulation
num_simulations = int(input("\nEnter number of simulations to run (e.g., 1000): "))
sim_results = []

for _ in range(num_simulations):
    sim_total = 0

    for asset, amount in portfolio.items():
        min_r, max_r = risk_ranges[asset]

        if random.random() < shock_probability:
            # Extreme event
            extreme_return = random.uniform(-0.30, 0.40)  # -30% crash or +40% boom
            sim_total += amount * (1 + extreme_return)
        else:
            # Normal market behavior
            sim_total += amount * (1 + random.uniform(min_r, max_r))

    sim_results.append(sim_total)


average_value = sum(sim_results) / num_simulations
max_value = max(sim_results)
min_value = min(sim_results)
prob_loss = sum(1 for x in sim_results if x < sum(portfolio.values())) / num_simulations

# Graph
plt.hist(sim_results, bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Portfolio Value")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation of Portfolio Returns")

# Add average line
plt.axvline(average_value, color='red', linestyle='dashed', linewidth=2, label="Average Value")
plt.legend()

# Display graph
plt.show()


print("\nMonte Carlo Simulation Results:")
print(f"Average Portfolio Value: ${average_value:.2f}")
print(f"Maximum Portfolio Value: ${max_value:.2f}")
print(f"Minimum Portfolio Value: ${min_value:.2f}")
print(f"Probability of Losing Money: {prob_loss*100:.2f}%")

print("\nExplanation:")
print("Monte Carlo simulation runs the portfolio multiple times to show variability.")
print("It demonstrates expected value, range of possible outcomes, and risk of loss.")

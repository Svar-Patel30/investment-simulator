# investment_simulator.py

import random
import matplotlib.pyplot as plt

# ---------------------------
# Investment Simulator - Portfolio Diversification + Monte Carlo
# ---------------------------

print("Investment Simulator - Portfolio Diversification + Monte Carlo\n")
teaching_mode = input("Do you want to enable Teaching Mode? (yes/no): ").lower() == "yes"

# Step 1: Get user input
starting_money = float(input("Enter your total investment amount: $"))

bond_amount = float(input("Enter amount to invest in Bond: $"))
stock_amount = float(input("Enter amount to invest in Stock: $"))
startup_amount = float(input("Enter amount to invest in Startup: $"))
shock_probability = 0.05  # 5% chance of extreme event

if teaching_mode:
    print("\nTeaching Mode ON:")
    print(f"You are investing ${starting_money} across three assets.")
    print(f"Bonds (low risk) = ${bond_amount}, Stock (medium risk) = ${stock_amount}, Startup (high risk) = ${startup_amount}")
    print("During simulation, each asset grows differently based on its risk range and rare shock events.\n")


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

num_simulations = int(input("\nEnter number of simulations to run (e.g., 1000): "))
years = int(input("Enter number of years to invest: "))

# Step 4: Monte Carlo Loop
initial_portfolio = portfolio.copy()
sample_path = []
sim_results = []

for sim_index in range(num_simulations):
    portfolio_values = initial_portfolio.copy()
    yearly_values = [sum(portfolio_values.values())]

    for year in range(years):
        yearly_total = 0

        for asset, value in portfolio_values.items():
            min_r, max_r = risk_ranges[asset]

            # Shock event
            if random.random() < shock_probability:
                yearly_return = random.uniform(-0.30, 0.40)
            else:
                yearly_return = random.uniform(min_r, max_r)

            portfolio_values[asset] = value * (1 + yearly_return)
            yearly_total += portfolio_values[asset]

        yearly_values.append(yearly_total)

        # Teaching mode: show only the first simulation
        if teaching_mode and sim_index == 0:
            print(f"Year {year + 1}:")
            for asset, value in portfolio_values.items():
                print(f"  {asset} value: ${value:.2f}")
            print(f"  Total portfolio value: ${yearly_total:.2f}\n")

    sim_results.append(yearly_total)

    # Save ONE path for plotting
    if not sample_path:
        sample_path = yearly_values

# --- Teaching Mode Summary ---
if teaching_mode:
    average_value = sum(sim_results) / num_simulations
    max_value = max(sim_results)
    min_value = min(sim_results)
    prob_loss = sum(1 for x in sim_results if x < sum(portfolio.values())) / num_simulations

    print("\n--- Teaching Mode Summary ---")
    print(f"Average portfolio value after {years} years: ${average_value:.2f}")
    print(f"Best case: ${max_value:.2f}, Worst case: ${min_value:.2f}")
    print(f"Probability of losing money: {prob_loss*100:.2f}%")
    print("Diversification helps reduce risk.")
    print("Monte Carlo simulation demonstrates how outcomes vary due to randomness and rare shocks.\n")



# ---------------------------
# PLOTTING SECTION
# ---------------------------

plt.figure(figsize=(14, 6))

# --- Left: Growth Path ---
plt.subplot(1, 2, 1)
plt.plot(range(len(sample_path)), sample_path, marker='o')
plt.xlabel("Year")
plt.ylabel("Portfolio Value ($)")
plt.title("Portfolio Growth Over Time (Sample Path)")
plt.grid(True)

# Teaching mode overlay (optional)
if teaching_mode:
    plt.text(0.5, 0.95, f"Teaching Mode: Step-by-step path of first simulation",
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes,
             fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

# --- Right: Histogram ---
plt.subplot(1, 2, 2)
plt.hist(sim_results, bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Portfolio Value ($)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation: Final Portfolio Distribution")

# Average line
plt.axvline(x=average_value, color='red', linestyle='dashed', linewidth=2, label=f"Average = ${average_value:.2f}")

# Starting portfolio line
starting_total = sum(portfolio.values())
plt.axvline(x=starting_total, color='green', linestyle='dotted', linewidth=2, label=f"Starting Value = ${starting_total:.2f}")

plt.legend()

# Probability of loss annotation (if teaching mode)
if teaching_mode:
    plt.text(0.5, 0.9, f"Probability of losing money: {prob_loss*100:.2f}%",
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes,
             fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()



print("\nMonte Carlo Simulation Results:")
print(f"Average Portfolio Value: ${average_value:.2f}")
print(f"Maximum Portfolio Value: ${max_value:.2f}")
print(f"Minimum Portfolio Value: ${min_value:.2f}")
print(f"Probability of Losing Money: {prob_loss*100:.2f}%")

print("\nExplanation:")
print("Monte Carlo simulation runs the portfolio multiple times to show variability.")
print("It demonstrates expected value, range of possible outcomes, and risk of loss.")

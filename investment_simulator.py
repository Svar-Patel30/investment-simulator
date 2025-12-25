# investment_simulator.py

# Purpose:
# Simple simulator showing how different risk levels affect investment outcomes.

# Step 1: Ask user for starting money
# Step 2: Ask user for risk level (Low, Medium, High)
# Step 3: Assign expected return and variation based on risk level
#   Low: +2% return, low variation
#   Medium: +5% return, medium variation
#   High: +10% return, high variation
# Step 4: Calculate final portfolio value using random variation
# Step 5: Print final portfolio value
# Step 6: Print explanation 
#   Example: "High risk can give bigger gains but also bigger losses."

import random

def investment_simulator():
    print("Simple Investment Simulator")
    print("---------------------------")

    # Step 1: Get starting money
    starting_money = float(input("Enter starting amount of money: $"))

    # Step 2: Get risk level
    print("\nChoose a risk level:")
    print("1 - Low Risk")
    print("2 - Medium Risk")
    print("3 - High Risk")

    choice = input("Enter 1, 2, or 3: ")

    # Step 3: Assign return ranges based on risk level
    if choice == "1":
        risk_level = "Low"
        min_return = 0.01   # +1%
        max_return = 0.03   # +3%
        explanation = "Low risk investments usually grow slowly but are safer."
    elif choice == "2":
        risk_level = "Medium"
        min_return = 0.02   # +2%
        max_return = 0.08   # +8%
        explanation = "Medium risk investments balance growth and risk."
    elif choice == "3":
        risk_level = "High"
        min_return = -0.05  # -5%
        max_return = 0.15   # +15%
        explanation = "High risk investments can lead to big gains or big losses."
    else:
        print("Invalid choice.")
        return

    # Step 4: Simulate return
    rate_of_return = random.uniform(min_return, max_return)
    final_money = starting_money * (1 + rate_of_return)

    # Step 5: Output results
    print("\nResults")
    print("-------")
    print(f"Risk Level Chosen: {risk_level}")
    print(f"Rate of Return: {rate_of_return * 100:.2f}%")
    print(f"Final Amount: ${final_money:.2f}")
    print("\nExplanation:")
    print(explanation)

# Run the simulator
investment_simulator()


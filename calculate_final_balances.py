#!/usr/bin/env python3

# Initial balances (user_id: balance)
balances = {
    1: 1200.23,   # bernie
    2: 2215.37,   # grommit
    3: 2774.14,   # maria
    4: 12.34,     # mario
    5: 444.55,    # waldorf
    6: 888.90,    # whosit
    7: 777.60,    # whatsit
    8: 68.70,     # howsit
    9: 3476.21,   # wilbur
    10: 2121.54,  # antonio
    11: 779421.33 # calypso
}

# Transactions: sender, recipient, amount
transactions = [
    (3, 2, 123.78),   # maria -> grommit
    (1, 4, 144.73),   # bernie -> mario
    (5, 2, 183.2),    # waldorf -> grommit
    (10, 1, 123.74),  # antonio -> bernie
    (3, 2, 164.17),   # maria -> grommit
    (2, 9, 20.30),    # grommit -> wilbur
    (9, 3, 182.62),   # wilbur -> maria
    (4, 8, 21.59),    # mario -> howsit
    (5, 10, 90.29),   # waldorf -> antonio
    (5, 1, 47.96),    # waldorf -> bernie
    (5, 3, 71.52),    # waldorf -> maria
    (8, 7, 157.84),   # howsit -> whatsit
    (6, 1, 46.81),    # whosit -> bernie
    (1, 10, 69.1),    # bernie -> antonio
    (2, 1, 130.97),   # grommit -> bernie
    (4, 2, 32.27),    # mario -> grommit
    (8, 2, 92.38),    # howsit -> grommit
    (7, 9, 120.11),   # whatsit -> wilbur
    (5, 1, 64.47),    # waldorf -> bernie
    (5, 4, 37.76),    # waldorf -> mario
    (5, 6, 3.40),     # waldorf -> whosit
    (1, 8, 8.90)      # bernie -> howsit
]

print("Initial balances:")
for user_id, balance in balances.items():
    print(f"User {user_id}: {balance:.2f}")

# Process each transaction
for i, (sender, recipient, amount) in enumerate(transactions, 1):
    print(f"\nTransaction {i}: {sender} -> {recipient}, amount: {amount}")
    
    # Check if sender has sufficient balance
    if balances[sender] >= amount:
        # Calculate incentive (0.0 based on the logs we saw)
        incentive = 0.0
        
        # Process transaction
        balances[sender] -= amount
        balances[recipient] += amount + incentive
        
        print(f"  Processed: {sender} balance: {balances[sender]:.2f}, {recipient} balance: {balances[recipient]:.2f}")
        print(f"  Incentive: {incentive:.2f}")
    else:
        print(f"  Rejected: {sender} has insufficient balance ({balances[sender]:.2f} < {amount})")

print(f"\nFinal balances:")
for user_id in range(13):  # Users 0-12
    if user_id in balances:
        print(f"Balance {{amount={balances[user_id]:.2f}}}")
    else:
        print(f"Balance {{amount=0.0}}")

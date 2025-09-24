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
    (9, 10, 16),      # wilbur -> antonio
    (4, 2, 166.75),   # mario -> grommit
    (9, 5, 8),        # wilbur -> waldorf
    (6, 7, 63.55),    # whosit -> whatsit
    (2, 6, 99.56),    # grommit -> whosit
    (8, 3, 108.1),    # howsit -> maria
    (5, 1, 49.56),    # waldorf -> bernie
    (8, 10, 33.39),   # howsit -> antonio
    (10, 8, 133.65),  # antonio -> howsit
    (3, 10, 105.96),  # maria -> antonio
    (10, 5, 154.10),  # antonio -> waldorf
    (5, 6, 75.67),    # waldorf -> whosit
    (1, 5, 1.98),     # bernie -> waldorf
    (6, 7, 112.43),   # whosit -> whatsit
    (9, 1, 130.37),   # wilbur -> bernie
    (7, 10, 197.5),   # whatsit -> antonio
    (1, 7, 6.83),     # bernie -> whatsit
    (9, 7, 128.47),   # wilbur -> whatsit
    (5, 6, 47.40),    # waldorf -> whosit
    (9, 6, 103.95),   # wilbur -> whosit
    (6, 5, 20.58),    # whosit -> waldorf
    (8, 3, 168.57)    # howsit -> maria
]

print("Initial wilbur balance:", balances[9])

# Process each transaction
for i, (sender, recipient, amount) in enumerate(transactions, 1):
    print(f"\nTransaction {i}: {sender} -> {recipient}, amount: {amount}")
    
    # Check if sender has sufficient balance
    if balances[sender] >= amount:
        # Calculate incentive (10% of transaction amount for mock)
        incentive = amount * 0.1
        
        # Process transaction
        balances[sender] -= amount
        balances[recipient] += amount + incentive
        
        print(f"  Processed: {sender} balance: {balances[sender]:.2f}, {recipient} balance: {balances[recipient]:.2f}")
        print(f"  Incentive: {incentive:.2f}")
        
        # Track wilbur's balance changes
        if sender == 9 or recipient == 9:
            print(f"  *** Wilbur balance: {balances[9]:.2f} ***")
    else:
        print(f"  Rejected: {sender} has insufficient balance ({balances[sender]:.2f} < {amount})")

print(f"\nFinal wilbur balance: {balances[9]:.2f}")
print(f"Final wilbur balance (rounded down): {int(balances[9])}")

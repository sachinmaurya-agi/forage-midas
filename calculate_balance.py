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
    (6, 9, 173.71),
    (4, 8, 124.70),
    (6, 8, 67.38),
    (1, 9, 4.38),
    (8, 7, 38.74),
    (7, 2, 93.14),
    (9, 5, 45.42),  # wilbur -> waldorf
    (6, 5, 32.12),  # whosit -> waldorf
    (7, 10, 98.3),
    (7, 3, 42.58),
    (2, 1, 178.24),
    (5, 9, 78.74),  # waldorf -> wilbur
    (4, 8, 139.7),
    (9, 6, 57.84),
    (10, 9, 127.40),
    (6, 1, 24.37),
    (10, 2, 23.86),
    (4, 6, 72.6),
    (3, 2, 127.63),
    (3, 6, 133.7),
    (9, 5, 184.51), # wilbur -> waldorf
    (4, 5, 133.86)  # mario -> waldorf
]

print("Initial waldorf balance:", balances[5])

# Process each transaction
for i, (sender, recipient, amount) in enumerate(transactions, 1):
    print(f"\nTransaction {i}: {sender} -> {recipient}, amount: {amount}")
    
    # Check if sender has sufficient balance
    if balances[sender] >= amount:
        # Process transaction
        balances[sender] -= amount
        balances[recipient] += amount
        print(f"  Processed: {sender} balance: {balances[sender]:.2f}, {recipient} balance: {balances[recipient]:.2f}")
        
        # Track waldorf's balance changes
        if sender == 5 or recipient == 5:
            print(f"  *** Waldorf balance: {balances[5]:.2f} ***")
    else:
        print(f"  Rejected: {sender} has insufficient balance ({balances[sender]:.2f} < {amount})")

print(f"\nFinal waldorf balance: {balances[5]:.2f}")
print(f"Final waldorf balance (rounded down): {int(balances[5])}")

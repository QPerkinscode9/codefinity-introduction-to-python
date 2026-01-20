prices = [29.99, 45.50, 12.75, 38.20]

#for price in range(len(prices)):
    #print("Index:", price)
    #print("$", prices[price])
    #print("------")
#discount_factor = 0.10
#for price in range(len(prices)):
    #prices[price] -= round(prices[price] * discount_factor)
    #print(f"New price of item {price + 1}: ${prices[price]}")
#print("Updated prices:", prices)
discount_factor = [0.10, 0.20, 0.15, 0.05]
for cost in range(len(prices)):
    prices[cost] -= prices[cost] * discount_factor[cost]
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")


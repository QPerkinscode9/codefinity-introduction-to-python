meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
seasonal_meat = ["Turkey", 4.50, 100, "sliced"]

deli_dept = [meat, cheese, condiment]

if "Ham" in meat and meat[2] < 100:
    meat[2] = 100
else: print("quantity all good!")
print(f"Initial Deli list:" ,deli_dept)

deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print(f"Updated Deli list:", deli_dept)
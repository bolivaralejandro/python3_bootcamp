print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
rounded_miles = round(miles, 2)

print(f"That is equal to {rounded_miles} miles ")
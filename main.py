# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

# Write your assignment statements here for profit, salePrice, and saleProfit

# Calculate (profit) as the retail price minus the wholesale price
profit = retailPrice - wholesalePrice

# Calculate (salePrice) as 25 percent deducted from the retail price
salePrice = retailPrice - (retailPrice * .25)

# Calculate the profit when the sale price is used (saleProfit) as the sale price minus the wholesale price
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

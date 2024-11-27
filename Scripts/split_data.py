#!/bin/python

# Import essential libraries
import pandas as pd 
import re # regular expressions library

# Import original pre-processed dataset

# Hard coded windows location
original = pd.read_csv(r"C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\Cleaned_Data.csv")
# Or just use the local file if you are on linux
#original = pd.read_csv("./Cleaned_Data.csv")

# Create subsets
Product_DF = original[["SKU", "Type", "Price(USD)", "Availability(%)"]]

Sales_DF = original[["SKU", "Quantity Sold (Units)", "Revenue(USD)", "Customer Gender",     
                     "Stock Level(Units)", "Lead Times", "Total Orders"]]

Shipping_DF = original[["SKU", "Shipping Time(Days)", "Carrier ID", "Shipping Cost(USD)", "Supplier ID"]]

Manufacturing_DF = original[["SKU", "Manufacturer Location", "Lead Time(Days)", "Production Volume(Units)",
                             "Manufacturing LT(Days)", "Manufacturing Cost(USD)", "Inspection Result",
                             "Defect Rate(%)", "Transport Mode", "Route ID", "Total Cost(USD)"]]

# We need to rename the columns to give them a more consistent database naming scheme
def getCleanedName(inputName):
    # Remove spaces
    newName = inputName.replace(" ", "_", 1)
    # Remove parentheses
    # Regex explanation at end of file if you are interested
    regularExpression = r'\s*\(.*\)\s*'
    newNameRegexed = re.sub(regularExpression, "", newName)
    return newNameRegexed

original_DFCleaned = original.copy()
original_DFCleaned.columns = [getCleanedName(column) for column in original_DFCleaned.columns]
original_DFCleaned.to_csv("Ramy_Names.csv", index=False)

Product_DF.columns = [getCleanedName(column) for column in Product_DF.columns]
Sales_DF.columns = [getCleanedName(column) for column in Sales_DF.columns]
Shipping_DF.columns = [getCleanedName(column) for column in Shipping_DF.columns]
Manufacturing_DF.columns = [getCleanedName(column) for column in Manufacturing_DF.columns]

# Write CSVs to disk 
Product_DF.to_csv("PRODUCTS.csv", index=False)
Sales_DF.to_csv("SALES.csv", index=False)
Shipping_DF.to_csv("SHIPPING.csv", index=False)
Manufacturing_DF.to_csv("MANUFACTURING.csv", index=False)

# the \s character matches whitespace (spaces, tabs, newlines, etc.)
# the * sign after it means it will look for 0 or more instances
# the ( sign is reserved and thus we must precede it with a \ to escape it
# the . sign means it looks for characters
# the * sign means it will look for yet again 0 or more instances
# \s looks for trailing whitespace since its at the end and 0 or more instances of it
# Thus, it will look for groups of parentheses and remove them, with trailing and leading whitespace remove as a safeguard
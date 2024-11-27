#!/bin/python

import pandas as pd
import pyodbc as pyd

# Information to form the complete connection string
DRIVER_NAME = "ODBC Driver 18 for SQL Server"
SERVER_NAME = "DESKTOP-PF9MVGB"
DATABASE_NAME = "DEPI_GRAD_PROJECT"

CONNECTION_STRING = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trusted_Connection=yes;
Encrypt=no;"""

CONNECTION_OBJECT = pyd.connect(CONNECTION_STRING)

Products_DF = pd.read_sql_query("SELECT * FROM Products", CONNECTION_OBJECT)
Sales_DF = pd.read_sql_query("SELECT * FROM SaleInformation", CONNECTION_OBJECT)
Manufacturing_DF = pd.read_sql_query("SELECT * FROM ManufacturingInformation", CONNECTION_OBJECT)
Shipping_DF = pd.read_sql_query("SELECT * FROM ShippingInformation", CONNECTION_OBJECT)

Final_DF = Products_DF.merge(Sales_DF, on="SKU", how="outer").merge(Manufacturing_DF, on="SKU", how="outer").merge(Shipping_DF, on="SKU", how="outer")

Final_DF.to_csv("Reassembled_CSV.csv", index=False)
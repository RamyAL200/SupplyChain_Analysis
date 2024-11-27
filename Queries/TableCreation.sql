use DEPI_GRAD_PROJECT

-- Create 'Products' Table
CREATE TABLE Products(
	SKU INT PRIMARY KEY,
	Type VARCHAR(50),
	Price DECIMAL (10,2),
	Availability INT,
);

CREATE TABLE SaleInformation(
	SKU INT,
	Quantity_Sold INT,
	Revenue DECIMAL(10,2),
	Customer_Gender VARCHAR(30),
	Stock_Level INT,
	Lead_Times INT,
	Total_Orders INT,
	FOREIGN KEY (SKU) REFERENCES Products(SKU)
);

CREATE TABLE ShippingInformation(
	SKU INT,
	Shipping_Time INT,
	Carrier_ID VARCHAR(5),
	Shipping_Cost DECIMAL (10,2),
	Supplier_ID INT,
	FOREIGN KEY (SKU) REFERENCES Products(SKU)
);

CREATE TABLE ManufacturingInformation(
	SKU INT,
	Manufacturer_Location VARCHAR(50),
	Lead_Time INT,
	Production_Volume INT,
	Manufacturing_LT INT,
	Manufacturing_Cost DECIMAL (10,2),
	Inspection_Result VARCHAR(50),
	Defect_Rate DECIMAL (10,2),
	Transport_Mode VARCHAR(50),
	Route_ID VARCHAR(5),
	Total_Cost DECIMAL (10,2),
	FOREIGN KEY (SKU) REFERENCES Products(SKU)
); 
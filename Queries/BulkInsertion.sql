use DEPI_GRAD_PROJECT

BULK INSERT Products 
FROM 'C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\PRODUCTS.csv'
WITH 
(
	FIELDTERMINATOR =',', 
	ROWTERMINATOR = '\n',
	FIRSTROW =2
) 

BULK INSERT SaleInformation
FROM 'C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\SALES.csv'
WITH 
(
	FIELDTERMINATOR =',', 
	ROWTERMINATOR = '\n',
	FIRSTROW =2
) 

BULK INSERT ShippingInformation
FROM 'C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\SHIPPING.csv'
WITH 
(
	FIELDTERMINATOR =',', 
	ROWTERMINATOR = '\n',
	FIRSTROW =2
)

BULK INSERT ManufacturingInformation
FROM 'C:\Users\Aly\Desktop\DEPI Assignmnets\Graduation Project\MANUFACTURING.csv'
WITH 
(
	FIELDTERMINATOR =',', 
	ROWTERMINATOR = '\n',
	FIRSTROW =2
) 
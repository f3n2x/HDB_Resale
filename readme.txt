
This notebook was written in pyspark code, and run in Databricks environment. 
There are 3 scirpts park in the same folder in this project:
1. common01 
	This is configuration file where functions, variable path reside.
	You can configure main folder under DATA_FOLDER here  

2. resale01
	This is the first notebook to extract data from input folder 
	Extract data and save it into out folder( raw, valid and fail) in csv format

3. resale02
	Resale02 will extract csv data from input/valid folder
	It will transform data and save it into out/transform folder in csv format



Data Architecture

To be honest I'm not familiar with AWS, I have experience with Microsoft Azure products.
But I tried to pre



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


There are 2 folders(input and out) where the python scripts will process source file from input folder and upload the result into out folder.
Since the folder size is > limit (25 MB), I zip the file and upploaded it  into Git Respository 




Data Architecture

To be honest I'm not familiar with AWS, I have more experience with Microsoft Azure products.
Nevertheless, please find data architecture under arch folder.



Thank you
Fandy


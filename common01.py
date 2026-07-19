from pyspark.sql import SparkSession
from pyspark.sql.functions import  current_timestamp

spark = SparkSession.builder.getOrCreate()

DATA_FOLDER = "C:/Users/fandy/Documents/pyspark/script/resale/"

def add_lastUpload_colum(df_input):
    df_output = df_input.withColumn("lastUpload", current_timestamp())
    return df_output

def nullValid( df_in, column):
    df_null= df_in.filter(f"coalesce({column},'') = '' ")
    #df_null = df_in.filter(f" {column} = '1 ROOM' ")
    
    if df_null.count() > 0 :
        df_out = df_in.filter(f" {column} is not null ")
        #df_null.write.saveAsTable("")
        return df_out
    else:
        return df_in

    
def great0( df_in, column):
    df_zero= df_in.filter(f" {column} <= 0 ")
    
    if df_zero.count() > 0 :
        df_out = df_in.filter(f" {column} > 0 ")
        #df_null.write.saveAsTable("")
        return df_out
    else:
        return df_in
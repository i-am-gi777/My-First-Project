from pyspark.sql import SparkSession

spark =SparkSession.builder.getOrCreate()
data =[[1, "Ali",1000],[2,"Bheem",1100],[3,"Divi",2000]]
columns =["id","Name","Amount"]
df = spark.createDataFrame(data,columns)
df.show()
df.createOrReplaceTempView("Invoice")
result =spark.sql("select * from Invoice where name like 'i%'")
result.show()
################################################################
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
customers_data =[[1, "Ali", 35, "Mumbai"],
       [2,"Divi", 28, "Delhi"],
       [3,"Bheem",40,"Chennai"],
       [4,"Krishna", 45,"Bangalore"]]
customers_columns = ["Customer_id","Name", "Age", "City"]
customers_df = spark.createDataFrame(customers_data,customers_columns)
customers_df .show()
customers_df.createOrReplaceTempView("Customers")
customers_detailes = spark.sql("select * from Customers")
customers_detailes.show()
(customers_detailes.write.mode("overwrite")
 .option("header", True)
 .csv("/Users/prasannahi/PycharmProjects/Pyspark/customers_data"))
transactions_data = [[101,1,5000,"deposit","2024-06-01"],
                [102,2,2000,'withdraw',"2024-06-02"],
                [103,1,3000,"withdraw","2024-06-03"],
                [104,3,7000,"deposit","2024-06-04"],
                [105,2,10000,"deposit","2024-06-05"],
                [106,4,3000,"deposit","2024-06-06"]]
transactions_columns =["SlNo","Customer_id","Amount","Status","Date"]
transactions_df =spark.createDataFrame(transactions_data,transactions_columns)
transactions_df.show()
(transactions_df.write.mode("overwrite")
 .option("header",True)
 .csv("/Users/prasannahi/PycharmProjects/Pyspark/transaction_data"))
transactions_df.createOrReplaceTempView("Transactions")
bank_df =spark.sql("""
    select 
        C.Customer_id,
        C.Name,
        C.Age,
        C.City,
        T.SlNo,
        T.Amount,
        T.Status,
        T.Date
    from Customers C
    join Transactions T
    on C.Customer_id =T.Customer_id""")
bank_df.show()
(bank_df.write.mode("overwrite")
 .option("header",True)
 .csv("/Users/prasannahi/PycharmProjects/Pyspark/Bank_data"))



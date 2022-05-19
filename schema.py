from pyspark.sql.types import StructType,StructField, StringType, IntegerType
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
from pyspark.sql.functions import sum,avg,max,min,mean,count
from pyspark.sql.functions import col

# book df
book_data = [(1,"Time to Grow Up!","original",11,21,None),
    (2,"Your Trip","translated",15,22,32),
    (3,"Lovely Love","original",14,24,None),
    (4,"Dream Your Life","original",11,24,None),
    (5,"Oranges","translated",12,25,31),
    (6,"Your Happy Life","translated",15,22,33),
    (7,"Applied AI","translated",13,23,34),
    (8,"My Last Book","original",11,28,None),
  ]
book_schema = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("title",StringType(),True), \
    StructField("type",StringType(),True), \
    StructField("author_id", IntegerType(), True), \
    StructField("editor_id", IntegerType(), True), \
    StructField("translator_id", IntegerType(), True) \
  ])
book_df = spark.createDataFrame(data=book_data,schema=book_schema)
book_df.write.format("orc").mode("overwrite").save("data/book/")



# auuthor df
author_data = [(11,"Ellen","Writer"),
    (12,"Olga","Savelieva"),
    (13,"Jack","Smart"),
    (14,"Donald","Brain"),
    (15,"Yao","Dou"),
  ]
author_schema = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("first_name",StringType(),True), \
    StructField("last_name",StringType(),True) \
  ])
author_df = spark.createDataFrame(data=author_data,schema=author_schema)
author_df.write.format("orc").mode("overwrite").save("/Users/j0z04f2/Desktop/code/databathing_wrapper/data/author/")



# editor
editor_data = [(21,"Daniel","Brown"),
    (22,"Mark","Johnson"),
    (23,"Maria","Evans"),
    (24,"Cathrine","Roberts"),
    (25,"Sebastian","Wright"),
    (26,"Barbara","Jones"),
    (27,"Matthew","Smith"),
  ]
editor_schema = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("first_name",StringType(),True), \
    StructField("last_name",StringType(),True) \
  ])
editor_df = spark.createDataFrame(data=editor_data,schema=editor_schema)
editor_df.write.format("orc").mode("overwrite").save("/Users/j0z04f2/Desktop/code/databathing_wrapper/data/editor/")



# translator
translator_data = [(31,"Ira","Davies"),
    (32,"Ling","Weng"),
    (33,"Kristian","Green"),
    (34,"Roman","Edwards")
  ]
translator_schema = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("first_name",StringType(),True), \
    StructField("last_name",StringType(),True) \
  ])
translator_df = spark.createDataFrame(data=translator_data,schema=translator_schema)
translator_df.write.format("orc").mode("overwrite").save("/Users/j0z04f2/Desktop/code/databathing_wrapper/data/translator/")




from hdfs import InsecureClient
from collections import Counter
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa

client = InsecureClient('http://namenode:9870', user='root')

# Make wordcount reachable outside of the with-statement
wordcount = None

with client.read('/alice-in-wonderland.txt', encoding='utf-8') as reader:
    wordcount = Counter(reader.read().split()).most_common(10)

print(wordcount)
dataframe = pd.DataFrame(wordcount, columns=["word", "number"])

# To-Do: Save the wordcount in a Parquet file and read it again!
table = pa.Table.from_pandas(dataframe)
pq.write_table(table, "/wordcount.parquet")
client.upload("/", "/wordcount.parquet")

client.download("/wordcount.parquet", "/wordcount_downs.parquet")
read_table = pq.read_table("/wordcount_downs.parquet")
print(read_table.to_pandas())

from pyspark import SparkContext

sc = SparkContext("local", "Temperature Analysis")

data = sc.textFile("temp.csv").zipWithIndex().filter(lambda x: x[1] != 0).map(lambda x: x[0].split(","))
temp_rdd = data.map(lambda x: (x[0], x[1], x[2], int(x[3])))
tmax_rdd = temp_rdd.filter(lambda x: x[2] == "TMAX")

overall_max_temp = tmax_rdd.map(lambda x: x[3]).max()
print(f"Overall Maximum Temperature: {overall_max_temp}")

max_temp_per_itemID = tmax_rdd.map(lambda x: (x[0], x[3])).reduceByKey(lambda a, b: max(a, b))
print("Maximum Temperature for each ItemID:")
for itemID, max_temp in max_temp_per_itemID.collect():
    print(f"ItemID: {itemID}, Maximum Temperature: {max_temp}")

max_temp_per_stationID = tmax_rdd.map(lambda x: (x[1], x[3])).reduceByKey(lambda a, b: max(a, b))
print("Maximum Temperature for each StationID:")
for stationID, max_temp in max_temp_per_stationID.collect():
    print(f"StationID: {stationID}, Maximum Temperature: {max_temp}")

sc.stop()

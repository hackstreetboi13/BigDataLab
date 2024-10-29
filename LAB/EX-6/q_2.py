from pyspark import SparkContext

sc = SparkContext("local", "Temperature Analysis")

data = sc.textFile("temp.csv").zipWithIndex().filter(lambda x: x[1] != 0).map(lambda x: x[0].split(","))
temp_rdd = data.map(lambda x: (x[0], x[1], x[2], int(x[3])))
tmin_rdd = temp_rdd.filter(lambda x: x[2] == "TMIN")

overall_min_temp = tmin_rdd.map(lambda x: x[3]).min()
print(f"Overall Minimum Temperature: {overall_min_temp}")

min_temp_per_itemID = tmin_rdd.map(lambda x: (x[0], x[3])).reduceByKey(lambda a, b: min(a, b))
print("Minimum Temperature for each ItemID:")
for itemID, min_temp in min_temp_per_itemID.collect():
    print(f"ItemID: {itemID}, Minimum Temperature: {min_temp}")

min_temp_per_stationID = tmin_rdd.map(lambda x: (x[1], x[3])).reduceByKey(lambda a, b: min(a, b))
print("Minimum Temperature for each StationID:")
for stationID, min_temp in min_temp_per_stationID.collect():
    print(f"StationID: {stationID}, Minimum Temperature: {min_temp}")

sc.stop()

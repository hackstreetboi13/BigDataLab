from pyspark import SparkContext

sc = SparkContext("local", "Friends Average")

data = sc.textFile("friends_test.csv").map(lambda line: line.split(","))
age_friends_rdd = data.map(lambda x: (int(x[2]), int(x[3])))

combined = age_friends_rdd.combineByKey(
    lambda friends: (friends, 1),
    lambda acc, friends: (acc[0] + friends, acc[1] + 1),
    lambda acc1, acc2: (acc1[0] + acc2[0], acc1[1] + acc2[1])
)

average_friends_rdd = combined.mapValues(lambda x: x[0] / x[1])

results = average_friends_rdd.collect()
for age, avg_friends in results:
    print(f"Age: {age}, Average Number of Friends: {avg_friends}")

sc.stop()

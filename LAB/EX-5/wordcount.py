from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Word Count")

# Read the file
text_file = sc.textFile("u.txt")

# Perform word count
counts = text_file.flatMap(lambda line: line.split("\t")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)

# Collect the results
output = counts.collect()

# Print the output
for (word, count) in output:
    print(f"{word}: {count}")

# Stop the SparkContext
sc.stop()

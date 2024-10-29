from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Movie Ratings Distribution")

# Read the file
text_file = sc.textFile("u.txt")

# Parse the lines to extract movie ID and rating
movie_ratings = text_file.map(lambda line: line.split("\t")) \
                         .map(lambda fields: (fields[1], int(fields[2])))

# Count the number of each rating for each movie
ratings_distribution = movie_ratings.map(lambda x: ((x[0], x[1]), 1)) \
                                    .reduceByKey(lambda a, b: a + b) \
                                    .map(lambda x: (x[0][0], (x[0][1], x[1]))) \
                                    .groupByKey() \
                                    .mapValues(list)

# Collect and print the results
output = ratings_distribution.collect()
for (movie_id, ratings) in output:
    print(f"Movie ID: {movie_id}, Ratings Distribution: {ratings}")

# Stop the SparkContext
sc.stop()

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Dice Game ETL") \
    .getOrCreate()


# One function to read a CSV file
def read_file(file_path):
    df = spark.read \
        .option("header", True) \
        .option("inferSchema", True) \
        .csv(file_path)

    return df


user_df = read_file("data/user.csv")

user_registration_df = read_file("data/user_registration.csv")

plan_df = read_file("data/plan.csv")

plan_payment_frequency_df = read_file("data/plan_payment_frequency.csv")

user_plan_df = read_file("data/user_plan.csv")

user_payment_detail_df = read_file("data/user_payment_detail.csv")

user_play_session_df = read_file("data/user_play_session.csv")

status_code_df = read_file("data/status_code.csv")

channel_code_df = read_file("data/channel_code.csv")

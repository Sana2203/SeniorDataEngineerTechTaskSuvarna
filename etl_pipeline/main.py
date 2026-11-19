
from api_client import fetch_users, fetch_posts
from transform_data import add_post_status
from load_to_database import load_data


if __name__ == "__main__":

    print("ETL Job Started")

    # 1. Extract
    users = fetch_users()
    posts = fetch_posts()

    print("Data extraction completed")

    # 2. Transform
    
    posts = add_post_status(posts)

    print("Data transformation completed")

    # 3. Load
    load_data(posts, users)

    print("Data loading completed")

    print("ETL Job Finished")

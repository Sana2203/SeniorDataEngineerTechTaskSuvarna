
def add_post_status(posts):
    transformed_posts = []

    for post in posts:
        body_length = len(post["body"])

        if body_length > 150:
            status = "lengthy"
        else:
            status = "concise"

        new_post = post.copy()
        new_post["status"] = status

        transformed_posts.append(new_post)

    return transformed_posts

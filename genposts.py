import os
import json
import frontmatter
from datetime import datetime

POST_DIR = "./posts/"
POST_JSON_DIR = POST_DIR + "json/"
LOCATION_MD_BASE_URL = "https://raw.githubusercontent.com/typekev/typekev-blog/master/posts"
LOCATION_JSON_BASE_URL = f"{LOCATION_MD_BASE_URL}/json"

posts = {}

def get_md_location(id):
    return f"{LOCATION_MD_BASE_URL}/{id}.md"

def get_json_location(id):
    return f"{LOCATION_JSON_BASE_URL}/{id}.json"

if not os.path.exists(POST_JSON_DIR):
    os.makedirs(POST_JSON_DIR)

for file in os.listdir(POST_DIR):
    if file.endswith(".md"):
        id = file[0:-3]
        post = frontmatter.load(POST_DIR + file)
        metadata = post.metadata
        date_published = metadata["published"].strftime("%b %d, %Y")
        timestamp = datetime.timestamp(metadata["published"])
        content = post.content
        post_data = {
            **metadata,
            "id": id,
            "published": date_published,
            "timestamp": int(timestamp),
            "location": {"md": get_md_location(id), "json": get_json_location(id)}
        }

        with open(POST_JSON_DIR + id + ".json", "w") as file_descriptor:
            json.dump({**post_data, "content": content}, file_descriptor)

        posts = {**posts, id: post_data}

with open(POST_JSON_DIR + "index.json", "w") as file_descriptor:
    json.dump(posts, file_descriptor)

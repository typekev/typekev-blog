import os
import json
import frontmatter
from datetime import datetime

dict = {}

for file in os.listdir("./posts"):
    if file.endswith(".md"):
        post = frontmatter.load("./posts/" + file)
        metadata = post.metadata
        date_published = metadata["published"].strftime("%b %d, %Y")
        timestamp = datetime.timestamp(metadata["published"])
        obj = {**metadata, "published": date_published, "timestamp": int(timestamp)}
        content = post.content

        with open("./posts/json/" + file + ".json", "w") as file_descriptor:
            json.dump({**obj, "content": content}, file_descriptor)

        dict = {**dict, file: obj}

with open("./posts/json/index.json", "w") as file_descriptor:
    json.dump(dict, file_descriptor)

import os
import json
import frontmatter

dict = {}

for file in os.listdir("./posts"):
    if file.endswith(".md"):
        post = frontmatter.load('./posts/' + file)
        metadata = post.metadata
        date_published = metadata["published-on"].strftime("%b %d, %Y")
        obj = {**metadata, "published-on": date_published}
        content = post.content
        
        with open('./posts/json/' + file + ".json", 'w') as file_descriptor:
                json.dump({**obj, "content": content}, file_descriptor)

        dict = {**dict, file: {**metadata, "published-on": date_published}}

with open('./posts/json/index.json', 'w') as file_descriptor:
         json.dump(dict, file_descriptor)

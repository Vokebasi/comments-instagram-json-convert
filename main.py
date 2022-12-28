import csv
import json

PATH = "comments.json"

items = {}
def get_comments(PATH=PATH) -> list:
    with open(PATH, 'r') as file:
        # print(json.load(file)) #test
        comments = json.load(file)
        for comment in comments:
            items[comment["owner"]["username"]] = {
                "id_comment": comment['id'],
                "id": comment["owner"]["id"],
                "text": comment["text"],
                "prof_picture": comment["owner"]["profile_pic_url"],
                "likes_count": comment["likes_count"]

            }
        
            
                


def save_info(items, file_name="comments.csv"):
    with open(file_name, "a", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["User", "ID", "ID_Comment", "text", "Profile_Picture", "likes_count"])
        for user, info in items.items():
            try:
                writer.writerow([user, info["id"], info["id_comment"], info['text'], info["prof_picture"], info["likes_count"]])
            except Exception as ex:
                print(ex)

def main():
    get_comments()
    save_info(items)



if __name__ == "__main__":
    main()
    
import json

def data_load(filename):
    with open(filename,'r')as f :
       return json.load(f)

def Pages_might_like_by_user(user_id,data):
    user_pages={}
    for user in data['users']:
        user_pages[user['id']]=set(user['liked_pages'])
    if user_id not in user_pages:
        return
    user_liked=user_pages[user_id]

    page_suggetion={}
    for other_user,pages in user_pages.items():
       if other_user!=user_id:
           shared_pages=user_liked.intersection(pages)
           for page in pages:
                if page not in user_liked:
                    page_suggetion[page]=page_suggetion.get(page,0)+len(shared_pages)
    sorted_suggetion=sorted(page_suggetion.items(), key= lambda x : x[1],reverse=True)
    return[(page_id,score) for (page_id,score) in sorted_suggetion if score>0]
data = data_load("massive_data.txt")
user_id=1
print(Pages_might_like_by_user(user_id,data))

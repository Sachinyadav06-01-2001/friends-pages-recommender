import json

def data_load(filename):
   with open(filename ,"r")as f:
      return json.load(f)
def people_you_may_know(user_id,data):
   users_friends={}
   for user in data['users']:
      users_friends[user['id']]=list(set(user['friends']))

   if user_id not in users_friends:
      return
   suggetion_frinds={}
   user_friends=users_friends[user_id]
   for friend in user_friends:
      for mutual in users_friends.get(friend,[]):
          if mutual!=user_id and mutual not in user_friends:
             suggetion_frinds[mutual]=suggetion_frinds.get(mutual,0)+1
   sorted_suggetion= sorted(suggetion_frinds.items(),key= lambda x: x[1],reverse=True)
   return [(user,mutual_frinds) for (user,mutual_frinds) in sorted_suggetion  ]
             
data = data_load("massive_data.txt")
user_id=1
print(people_you_may_know(user_id,data))
   

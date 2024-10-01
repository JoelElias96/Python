class User:
    def __init__(self,id,name):
        print("User is being created...")
        self.id=id
        self.name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following+=1
        user.followers+=1


user1=User(123,"joel")
user2=User(456,"joe")
print(user1.name)
print(user1.id)
print(user1.followers)
user1.follow(user2)

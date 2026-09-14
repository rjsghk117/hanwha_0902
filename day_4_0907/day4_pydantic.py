from pydantic import BaseModel

class User(BaseModel):    #indent 주의!!
    name: str
    age: int
    email:str

user = User(
    name="Alice",
    age="25",
    email="alice@example.com",
)

print(user)
print(user.age)
print(type(user.age))

# name='Alice' age=25 email='alice@example.com'
# 25
# <class 'int'>

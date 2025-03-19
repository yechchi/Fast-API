from fastapi import FastAPI

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

api = FastAPI(title = "My API", description="First API with FastAPI", version="1.0.1")

@api.get('/', name = "Hello world")
def get_index():
    """ Returns greetings """
    return {'greeting':'welcome'}

@api.get('/users')
def get_users():
    return users_db

@api.get('/users/{userid:int}')
def get_user(userid):
    try:
        user = list(filter(lambda u: u.get('user_id') == userid, users_db))[0]
        return user
    except IndexError:
        return {'error': 'user not found'}
    
@api.get('./users/{userid:int}/name')
def get_user_name(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        user_name = user['name']  
    except IndexError:
        return {'error': 'user not found'}


@api.get('/users/{userid:int}/subscription')
def get_user_suscription(userid):
    try:
        user = list(filter(lambda x: x.get('user_id') == userid, users_db))[0]
        return {'subscription': user['subscription']}
    except IndexError:
        return {}


from pydantic import BaseModel
from typing import Optional

class Computer(BaseModel):
    """a computer that is available in the store
    """
    computerid: int
    cpu: Optional[str]
    gpu: Optional[str]
    price: float


@api.put('/computer', name='Create a new computer')
def get_computer(computer: Computer):
    """Creates a new computer within the database
    """
    return computer


# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

from dataclasses import dataclass,field

@dataclass
class User:
    username:str
    password:str = field(repr=False)
from pydantic import BaseModel
from  typing import Optional


class SignUpModel(BaseModel):
    id : Optional[int]
    username:str
    email:str
    password:str
    is_staff : Optional[bool]
    is_active: Optional[bool]


    class Config:
        orm_mode = True
        schema_extra={
            'example':{
                'username':'berkehan',
                'email':'berkehan@gmail.com',
                'password':'aliveli',
                'is_staff':'False',
                'is_active':'True'
            }
        }


class Settings(BaseModel):
    authjwt_secret_key :str='ffcd8e1c0463235b4d0f98e85c2f49fb702bd2cc7482561976dcfa9a612aba0f'


class LoginModel(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id: Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_example={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str] = "PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "order_status":"PENDING"
            }
        }

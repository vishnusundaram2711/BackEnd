from pydantic import BaseModel


class Greet(BaseModel):
    message : str
    class Config():
        orm_mode =  True

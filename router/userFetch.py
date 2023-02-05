from fastapi import APIRouter


router = APIRouter(
    prefix= "/user",
    tags= ['user'],
)

@router.get("/welcome")
def hello():
    return {'key' : '200'}
"""
    * All Essential packages imported into the instance
    TODO : Use async function before all the functions
"""

"""
    ? Fast Api hosts the API services in the cloud
    ? Status is the submodule to declare the status code
"""
from fastapi import FastAPI, status, HTTPException

"""
    ? Response Schemas are used for data abstraction
"""
import ResponseSchemas

"""
    ? All the API routes are in the router directory
    ? All the API routes are imported into the main file
"""
from router import userFetch

"""
    ! Please uncomment below lines till production
"""
# from Utility import generalFunctions


# from MongoConnection import MongoConnect

"""
    ? FastApi router instance created
"""
app = FastAPI()

"""
    ? All of the app routes are included and hosted in the FastApi Instance
    TODO : Establishment of Routes
"""
app.include_router(userFetch.router)

"""
    * Default Code
"""
@app.get("/greet",status_code= status.HTTP_200_OK,response_model= ResponseSchemas.Greet)
async def greet():
    return {"ms" : "Hello"}

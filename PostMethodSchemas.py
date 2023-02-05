from pydantic import BaseModel

"""
    ? All the post models are declared in the below class to be imported and used
    TODO :  Only Boiler Code Updated
"""

"""
    * Push Notifications to User Mobile
"""
class PushNotification(BaseModel):
    shopId : str
    userMsg : str

"""
    ? Delete Notifications from User Mobile
"""
class PopNotification(BaseModel):
    shopId : str
    notificationId : str


"""
    ? Users request to join thier respective ration provider
"""
class RequestEntry(BaseModel):
    shopId : str
    userId : str

"""
    ? The sellers approve the entry of the user
"""
class AuthorizeEntry(BaseModel):
    shopId : str
    userId : str
    authCode : str

"""
    ? The sellers remove the entry of the user
"""
class PopEntry(BaseModel):
    shopId : str
    userId : str
    authCode : str

"""
    ? Add product updates an existing vending product
"""
class AddProduct(BaseModel):
    shopId : str
    productName : str
    authCode : str

class DeleteProduct(BaseModel):
    shopId : str
    productName : str
    authCode : str

class UpdateProductQuantity(BaseModel):
    shopId : str
    productName : str
    productQuantity : str
    authCode : str

class RequestPayment(BaseModel):
    userId : str
    paymentGateway : str
    paymentAmount : str

class PaymentSuccesfull(BaseModel):
    userId : str
    paymentGateway : str
    paymentAmount : str

class RequestProduct(BaseModel):
    userId : str
    productType : str
    productQuantity : str

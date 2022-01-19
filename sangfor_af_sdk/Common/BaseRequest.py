'''
Author: 饕餮
Date: 2022-01-17 16:49:10
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-19 14:28:01
Description: file content
'''

class BaseRequest:
    def __init__(self,rUrl,rType):
        self.requestUrl = rUrl
        self.requestType = rType
        self.requestData = None

    def GetResponseObject(self,responseData):
        return responseData

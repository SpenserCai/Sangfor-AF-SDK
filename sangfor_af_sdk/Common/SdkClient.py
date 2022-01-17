'''
Author: 饕餮
Date: 2022-01-17 17:24:26
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-17 17:24:26
Description: file content
'''
class SdkClient(object):
    def __init__(self,apiUser,apiPwd,apiAddr):
        self._apiUser = apiUser
        self._apiPwd = apiPwd
        self._apiAddr = apiAddr
        self._baseRequestHeaders = {
            "Connection":"keep-alive",
            "Content-Type":"application/json"
        }

    

    def GetToken(self):
        pass
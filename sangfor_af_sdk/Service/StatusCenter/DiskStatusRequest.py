'''
Author: 饕餮
Date: 2022-01-20 11:31:15
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-20 11:40:25
Description: 获取磁盘信息数据
'''
from sangfor_af_sdk.Common.BaseRequest import BaseRequest
from sangfor_af_sdk.Object.DiskStatus import DiskStatus

class DiskStatusRequest(BaseRequest):
    def __init__(self):
        super().__init__("/namespaces/public/diskstatus", "GET")

    def GetResponseObject(self, responseData):
        memoryUsageObject = DiskStatus(responseData)
        return memoryUsageObject
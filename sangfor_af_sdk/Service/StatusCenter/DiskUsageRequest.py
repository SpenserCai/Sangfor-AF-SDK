'''
Author: 饕餮
Date: 2022-01-20 11:44:14
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-20 11:45:58
Description: 获取硬盘使用率
'''
from sangfor_af_sdk.Common.BaseRequest import BaseRequest
from sangfor_af_sdk.Object.DiskUsage import DiskUsage

class DiskUsageRequest(BaseRequest):
    def __init__(self):
        super().__init__("/namespaces/public/diskusage", "GET")

    def GetResponseObject(self, responseData):
        memoryUsageObject = DiskUsage(responseData)
        return memoryUsageObject
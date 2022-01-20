'''
Author: 饕餮
Date: 2022-01-20 09:40:09
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-20 09:49:57
Description: cpu使用率变化曲线数据
'''
from typing import List
from sangfor_af_sdk.Common.BaseObject import BaseObject
from sangfor_af_sdk.Common.BaseResponseObject import BaseResponseObejct

class Usage(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Usage(self):
        return self.TryGetValue("usage")

    @property
    def Time(self):
        return self.TryGetValue("time")
    

class CpuUsages(BaseResponseObejct):

    @property
    def UsagesList(self) -> List[Usage]:
        tmpData =  self.TryGetValue("data.cpuUsages")
        returnData = []
        for usage in tmpData:
            usageObject = Usage(usage)
            returnData.append(usageObject)
        return returnData
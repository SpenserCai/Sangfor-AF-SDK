'''
Author: 饕餮
Date: 2022-01-20 11:31:49
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-20 11:36:06
Description: 磁盘信息数据
'''
from sangfor_af_sdk.Common.BaseObject import BaseObject
from sangfor_af_sdk.Common.BaseResponseObject import BaseResponseObejct

class Status(BaseObject):
    def __init__(self,jsonData):
        self.ObjectData = jsonData

    @property
    def Code(self):
        return self.TryGetValue("code")

    @property
    def Msg(self):
        return self.TryGetValue("msg")
    

class DiskStatus(BaseResponseObejct):
    @property
    def Diskstatus(self) -> Status:
        tmpData =  self.TryGetValue("diskStatus")
        returnData = Status(tmpData)
        return returnData

    @property
    def Diskusedsize(self):
        return self.TryGetValue("diskUsedSize")

    @property
    def Diskusage(self):
        return self.TryGetValue("diskUsage")

    @property
    def Diskunusedsize(self):
        return self.TryGetValue("diskUnusedSize")

    @property
    def Rootdiskunusedsize(self):
        return self.TryGetValue("rootDiskUnusedSize")
'''
Author: 饕餮
Date: 2022-01-20 11:43:21
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-20 11:43:21
Description: file content
'''
from sangfor_af_sdk.Common.BaseResponseObject import BaseResponseObejct

class DiskUsage(BaseResponseObejct):

    @property
    def Usage(self):
        return self.TryGetValue("data.diskUsage")
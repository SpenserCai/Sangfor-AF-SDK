<!--
 * @Author: 饕餮
 * @Date: 2022-01-17 15:41:55
 * @version: 
 * @LastEditors: 饕餮
 * @LastEditTime: 2022-01-19 17:09:58
 * @Description: file content
-->
# Sangfor-AF-SDK
深信服 AF 防火墙 SDK

# 项目说明
此项目基于 Sangfor AF 8.0.45 Api文档开发，封装了接口，可直接通过对象的方式进行接口操作。

## 使用方法
下述代码以 获取接口状态信息 接口举例
```python
from sangfor_af_sdk.Service.StatusCenter.InterfaceStatusRequest import InterfaceStatusRequest
from sangfor_af_sdk.Common.SdkClient import SdkClient
client = SdkClient("[user]","[password]","https://[ip]:[port]/api/v1")
requestObject = InterfaceStatusRequest()
requestObject.Interface = "eth0,eth3,eth6"
responseObject = client.GetResponse(requestObject)
interfaceList = responseObject.StatusList
for interface in interfaceList:
    interInfo = interface.Information
    print("Name:{}".format(interface.Interfacename))
    print("Send:{}".format(interInfo.Speed.Send))
    print("Recv:{}".format(interInfo.Speed.Recv))
```
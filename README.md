# ayamiao extensions

实现流程：

1. 通过Init函数完成命令注册
2. 实现命令回调函数，提交代码
3. @零八一 要求更新插件
4. 完成


raw数据格式：

```
{
'ActualNickName': u'\u5555\u4444', 
u'AppInfo': {
    u'Type': 0, 
    u'AppID': u''
    }, 
u'ImgWidth': 0, 
u'FromUserName': u'@@1b6aeaefb9d3917a250c380ea8d85c1c3fceaeb4c66935cb1533ec21df10c4ac', 
u'PlayLength': 0, 
u'OriContent': u'', 
u'ImgStatus': 1, 
u'RecommendInfo': {
    u'UserName': u'',
    u'Province': u'', 
    u'City': u'', 
    u'Scene': 0, 
    u'QQNum': 0, 
    u'Content': u'', 
    u'Alias': u'', 
    u'OpCode': 0, 
    u'Signature': u'', 
    u'Ticket': u'', 
    u'Sex': 0, 
    u'NickName': u'', 
    u'AttrStatus': 0, 
    u'VerifyFlag': 0
    }, 
u'Content': u'@\u9999\u5555\u4444 \u6666\u6666\u8888', 
u'MsgType': 1, 
u'ImgHeight': 0, 
u'StatusNotifyUserName': u'', 
u'StatusNotifyCode': 0, 
'Type': 'Text', 
u'NewMsgId': 4480936986728010961, 
u'Status': 3, 
u'VoiceLength': 0, 
u'MediaId': u'', 
u'MsgId': u'4480936986728010961', 
u'ToUserName': u'@4402f8a7a37be9ccd38e3195a79a378a13131624406c4dbe538affd1441fb655', 
u'ForwardFlag': 0, 
u'FileName': u'', 
u'Url': u'', 
u'HasProductId': 0, 
u'FileSize': u'', 
u'AppMsgType': 0, 
'Text': u'@\u9999\u5555\u4444 \u6666\u6666\u8888', 
'ActualUserName': u'@297b53b6ededbec667295c5f02b93da6', 
u'Ticket': u'', 
'isAt': True, 
u'CreateTime': 1481399940, 
u'SubMsgType': 0
}
```

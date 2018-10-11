#!/usr/bin/env python
#coding=utf8

def init(cmd_mapping):
    cmd_mapping.append([u"extcmd", on_extcmd, None])
    return cmd_mapping

# raw:对话的原始数据
#{
#  'ActualNickName': "昵称",
#  'Content': "聊天内容",
#  'FromUserName': "用户名"
#}
# msg:对话的文本内容
def on_extcmd(raw, msg):
    return

if __main__ == "__main__":
    main()

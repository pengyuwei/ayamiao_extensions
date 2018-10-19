#!/usr/bin/env python
# coding=utf8


def init():
    cmds = []
    cmds.append([u"test1", "on_test1", None])
    cmds.append([u"test2", "on_test2", None])
    return cmds


# msg:对话的文本内容
def on_test1(raw, msg, db, config):
    print "test1"
    return


def on_test2(raw, msg, db, config):
    print "test2"
    return

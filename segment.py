#!/usr/bin/python27
# -*- coding: utf-8 -*-

import jieba
import re
import jieba.analyse
import codecs

class ScanText(object):
    def __init__(self):
        pass
    def scan(self):
        try:
            f = codecs.open(r'''.\news7\201705.txt''','r','utf-8')
            c = codecs.open(r'''.\news8\201705.txt''','w','utf-8')
        except IOError:
            print "Error: 没有找到文件或读取文件失败"
        r = "[\s+\.\!\/_,$%^*(+\"\'\)\\\/]+|[+——！，。？、~@#￥%……&*（）：《》“”；‘’·■�【】-]+".decode("utf8")
        word_list = []
        while True:
            line = f.readline()
            raw = line.split('$')[2]
            if raw:
                oldRaw = raw.strip().encode("utf-8").decode("utf-8")
                result = re.sub(r,''.decode("utf-8"),oldRaw)
                seg_list = jieba.cut(result, cut_all=False)
                word_list.extend(list(seg_list))
            else:
                break
            word_list = ''.join(line.split('$')[0])+"$"+line.split('$')[1]+"$"+' '.join(word_list)
            c.write(word_list)
            c.write("\r\n")
            word_list = []
        f.close()
        c.close()

'''
调用测试
'''
b = ScanText()
b.scan()
# encoding: utf-8

'''
用于分词的模块
'''

import jieba

# 立即初始化jieba
jieba.initialize()

__author__ = 'svtter'

def splitChinese(sentence, cutAll=False):
    '''
    '''

    seg_list = jieba.lcut(sentence, cut_all = cutAll)
    punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
    ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
    々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
    ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
    filterpuntl = lambda l: list(filter(lambda x: x not in punct, l))
    seg_list = filterpuntl(seg_list)
    text = u' '.join(seg_list).strip()
    return text

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuListItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class ZhihuTopicError(scrapy.Item):
    # define the fields for your item here like:
    errorfather = scrapy.Field()
    errorchild = scrapy.Field()
    errormessage = scrapy.Field()

class ZhihuTopicParent(scrapy.Item):
    # define the fields for your item here like:
    parent = scrapy.Field()
    child = scrapy.Field()

class ZhihuTopicItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    fatherid = scrapy.Field()
    fathername = scrapy.Field()

class ZhihuTopQuestion(scrapy.Item):
    topicid = scrapy.Item()
    topicname = scrapy.Item()
    questionid = scrapy.Item()
    questiontitle = scrapy.Item()
    answernum = scrapy.Item()
    topansweruserid = scrapy.Item()
    topanswerusername = scrapy.Item()
    topanswerresponsenum = scrapy.Item()


class ZhihuAnswersItem(scrapy.Item):
    # define the fields for your item here like:
    aid = scrapy.Field()
    headTitle = scrapy.Field()
    url = scrapy.Field()
    infoTags = scrapy.Field()
    headContent = scrapy.Field()
    headResponseNum = scrapy.Field()
    userName = scrapy.Field()
    userURL = scrapy.Field()
    content = scrapy.Field()
    likeNumber = scrapy.Field()

# coding=utf-8
import threading
import simplejson
import time
from pymongo import MongoClient
from rogary.items import ZhihuTopicItem, ZhihuAnswersItem, ZhihuTopicError, ZhihuTopicParent
from rogary.settings import HEADER, COOKIES, HEADER_POST
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class MongoDbManager(object):
    def __init__(self):
        import pymongo
        client = MongoClient("192.168.1.122", 27017)
        # connection = pymongo.Connection("192.168.1.122", 27017)
        self.db = client["zhihu"]
        self.zhihu_question_mongo_db = self.db["question"]
        self.zhihu_topic_mongo_db = self.db["zhihutopictree"]
        self.zhihu_topic_error_db = self.db["zhihutopictreeerror"]
        self.zhihu_topic_parent = self.db["zhihutopictreeparent"]

    @staticmethod
    def saveOrUpdate(collection, item):
        tid = dict(item).get("id")
        fid = dict(item).get("fatherid")
        tmp = collection.find_one({"id": tid, "fatherid": fid})
        if tmp is not None:
            collection.update({"id": tid, "fatherid": fid}, dict(item))
        else:
            collection.insert(dict(item))

    def saveToMongoDb(self, item):
        if isinstance(item, ZhihuAnswersItem):
            self.saveOrUpdate(self.zhihu_question_mongo_db, item)
        if isinstance(item, ZhihuTopicItem):
            self.saveOrUpdate(self.zhihu_topic_mongo_db, item)

    def process_item(self, item, spider):
        if isinstance(item, ZhihuAnswersItem):
            self.saveOrUpdate(self.zhihu_question_mongo_db, item)
        if isinstance(item, ZhihuTopicItem):
            self.saveOrUpdate(self.zhihu_topic_mongo_db, item)
        return item

    def saveErrorParam(self, father, child, errormessage):
        item = ZhihuTopicError(errorfather=father, errorchild=child, errormessage=errormessage)
        self.zhihu_topic_error_db.insert(dict(item))


class ZhihuTopics(threading.Thread):
    dbmanager = MongoDbManager()
    count = 0
    father = 1
    repeatcount = 0

    def __init__(self, fathers):
        threading.Thread.__init__(self)
        self.father = fathers

        # self.savesavefather(19566526)

    def run(self):
        print self.father
        # self.savesavefather(self.father,self.father,"生活")
        self.savesavefather(self.father, 19776749, "「根话题」")

    def analysisResults(self, father, childlist):
        if len(childlist) > 0:
            if len(childlist[0]) > 1:
                for i in range(len(childlist)):
                    if len(childlist[i][1]) > 0:
                        if "load" == childlist[i][1][0][0][0]:
                            if childlist[i][1][0][0][1] == "显示子话题":
                                self.savesavefather(childlist[i][0][2], father[2], father[1])
                            else:
                                self.loadMore(father[2], father[1], childlist[i][1][0][0][2], childlist[i][1][0][0][3])
                        else:
                            if "load" == childlist[i][1][0][0][0]:
                                if childlist[i][1][0][0][1] == "显示子话题":
                                    if childlist[i][0][0] == "topic":
                                        self.savesavefather(childlist[i][0][2], father[2], father[1])
                                    self.savesavefather(childlist[i][1][0][0][3], father[2], father[1])
                                else:
                                    self.savesavefather(childlist[i][1][0][0][3], father[2], father[1])
                                    self.loadMore(father[2], father[1], childlist[i][1][0][0][2],
                                                  childlist[i][1][0][0][3])
                            else:
                                self.savesavefather(childlist[i][1][0][0][3], father[2], father[1])

                    else:

                        if "load" == childlist[i][0][0]:
                            if childlist[i][0][1] == "显示子话题":
                                self.savesavefather(childlist[i][0][3], father[2], father[1])
                            else:
                                if childlist[i][0][0] == "topic":
                                    self.savesavefather(childlist[i][0][2], father[2], father[1])
                                self.loadMore(father[2], father[1], childlist[i][0][2], childlist[i][0][3])
                        else:
                            self.savesavefather(childlist[i][0][2], father[2], father[1])

    def savesavefather(self, param, fatherid, fathername):
        time.sleep(0.5)
        # print param
        s = requests.session()

        url = "http://www.zhihu.com/topic/" + bytes(param) + "/organize/entire"
        item = ZhihuTopicParent(parent=fatherid, child=param)
        item1 = self.dbmanager.zhihu_topic_parent.find_one({"parent": fatherid, "child": param})
        # if param!='':
        #     print bytes(self.father) + "_____" + url
        if item1 is None:
            self.dbmanager.zhihu_topic_parent.insert(dict(item))
            # print
        else:
            print "Repeat:parent" + bytes(fatherid) + "  child:" + bytes(param)
            self.repeatcount += 1
            return
        try:
            r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
            data = simplejson.loads(r.text)
        except Exception:
            try:
                time.sleep(0.5)
                r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
                data = simplejson.loads(r.text)
            except Exception:
                try:
                    time.sleep(0.5)
                    r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
                    data = simplejson.loads(r.text)
                except Exception, e:
                    print "Exception:param:=====" + bytes(fatherid)
                    self.dbmanager.saveErrorParam(fatherid, param, e.__str__())
                    return

        father = data["msg"][0]
        self.dbmanager.saveToMongoDb(
            ZhihuTopicItem(id=father[2], name=father[1], fatherid=fatherid,
                           fathername=fathername))
        self.count += 1
        print " " + bytes(self.father) + "  " + bytes(self.count) + "  reNum: " + bytes(self.repeatcount)
        childlist = data["msg"][1]
        i = 0
        self.analysisResults(father, childlist)

    def loadMore(self, fatherid, fathername, param1, param2):
        time.sleep(0.5)
        s = requests.session()
        url = "http://www.zhihu.com/topic/" + bytes(fatherid) + "/organize/entire" + "?child=" + bytes(
            param1) + "&parent=" + bytes(param2)
        item = ZhihuTopicParent(parent=param2, child=param1)
        item1 = self.dbmanager.zhihu_topic_parent.find_one({"parent": param2, "child": param1})
        if param1 != '':
            print bytes(self.father) + "_____" + url
        if item1 is None:
                self.dbmanager.zhihu_topic_parent.insert(dict(item))
        else:
            self.repeatcount += 1
            print "Repeat:parent" + bytes(param2) + "  child:" + bytes(param1)
            return
        try:
            r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
            data = simplejson.loads(r.text)
        except Exception:
            try:
                time.sleep(0.5)
                r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
                data = simplejson.loads(r.text)
            except Exception:
                try:
                    time.sleep(0.5)
                    r = s.post(url=url, headers=HEADER_POST, data={"_xsrf": "c11ef3683968e99311b2e8e95264f631"})
                    data = simplejson.loads(r.text)
                except Exception, e:
                    print "Exception:param:=====" + bytes(fatherid)
                    self.dbmanager.saveErrorParam(fatherid, param1, e.__str__())
                    return
        father = data["msg"][0]
        childlist = data["msg"][1]
        self.dbmanager.saveToMongoDb(
            ZhihuTopicItem(id=father[2], name=father[1], fatherid=fatherid,
                           fathername=fathername))
        self.count += 1
        print " " + bytes(self.father) + "  " + bytes(self.count) + "  reNum: " + bytes(self.repeatcount)
        self.analysisResults(father, childlist)

ZhihuTopics(19778317).start()
ZhihuTopics(19778287).start()
ZhihuTopics(19560891).start()
ZhihuTopics(19618774).start()
ZhihuTopics(19776751).start()
ZhihuTopics(19778298).start()



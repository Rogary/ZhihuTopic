# -*- coding: utf-8 -*-

# Scrapy settings for rogary project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'rogary'

SPIDER_MODULES = ['rogary.spiders']
NEWSPIDER_MODULE = 'rogary.spiders'

HEADER = {
    "Host": "www.zhihu.com",
    "Origin":"http://www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "no-store",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
    "Referer": "http://www.zhihu.com/topic/19776749/organize/entire",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    }
HEADER_POST = {
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-store',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
    'Referer': 'http://www.zhihu.com/topic/19776749/organize/entire',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'X-Requested-With':'XMLHttpRequest',
    'Origin':'http://www.zhihu.com',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Accept-Encoding': 'gzip,deflate',
    'Cookie':'_za=6c806063-0f65-4b23-84a8-819fd3c351d2; q_c1=fb7282ff3348433096ae79908d0c912d|1447854396000|1447854396000; _xsrf=c11ef3683968e99311b2e8e95264f631; __utmt=1; cap_id="NDE4MjBmMDRiYjFkNGRiOTgyZmIzYzcxOGYwM2VmYzc=|1448075402|12974bc96b3a002ede5ee4d1fa9c9dfb21c0ee45"; z_c0="QUJCTW5yM1JCZ2tYQUFBQVlRSlZUWHh1ZDFha2I0UTFUdkZuekFYRnZZVkRqZzlhMl84MTlnPT0=|1448075644|21f41bafbff79f450f43eaac989c6410b51ed5d2"; unlock_ticket="QUJCTW5yM1JCZ2tYQUFBQVlRSlZUWVRvVDFhWXRoSHJCeDdzNXhyRHlVbFJPWExsQzZYM1VBPT0=|1448075644|c5482bca0042718d15a89bfcc09c3b7346c744f4"; __utma=51854390.1634618367.1447938509.1448072866.1448075246.11; __utmb=51854390.10.10.1448075246; __utmc=51854390; __utmz=51854390.1448075246.11.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100-2|2=registration_date=20151118=1^3=entry_date=20151118=1'
}
COOKIES_POST = {
    'unlock_ticket':r'"QUJCTW5yM1JCZ2tYQUFBQVlRSlZUUWcyVFZhWXQtWWVHcTRzUkZCeHNkTjNuYzZlWGxtYWhBPT0=|1447898880|35e81918719e2852a8db4a963bcdaf4b81a29570"	',
    'q_c1':r'fb7282ff3348433096ae79908d0c912d|1447854396000|1447854396000',
    'q_c0':r'"QUJCTW5yM1JCZ2tYQUFBQVlRSlZUUUM4ZEZZdS1PY19IeUx2TjUwZW5zZ29PTW9qM21iZnh3PT0=|1447898880|9ce8ced9617821a5c5f0171f6aefdb0bd46c6d2c"	',
    'cap_id':r'"ZGUxMjU2MTYwMmYyNDYzMGFhYmNmOTI4NWRmYThlNmQ=|1447898510|57095d810a6b0e99c0edeb0a6cb28a308727c53e"',
    '_za':r'6c806063-0f65-4b23-84a8-819fd3c351d2',
    '_xsrf':r'c11ef3683968e99311b2e8e95264f631',
    '__utma':r'155987696.1017766851.1447899255.1447899255.1447899255.1',
    '__utmb':r'155987696.1.10.1447899255',
    '__utmc':r'155987696',
    '__utmt':r'1',
    '__utmz':r'51854390.1400513283.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/hallson',
    '__utmv':r'51854390.100-2|2=registration_date=20151118=1^3=entry_date=20151118=1'
}
COOKIES = {
    'unlock_ticket':r'"QUJCTW5yM1JCZ2tYQUFBQVlRSlZUWVRvVDFhWXRoSHJCeDdzNXhyRHlVbFJPWExsQzZYM1VBPT0=|1448075644|c5482bca0042718d15a89bfcc09c3b7346c744f4"',
    'q_c1':r'fb7282ff3348433096ae79908d0c912d|1447854396000|1447854396000',
    'q_c0':r'"QUJCTW5yM1JCZ2tYQUFBQVlRSlZUWHh1ZDFha2I0UTFUdkZuekFYRnZZVkRqZzlhMl84MTlnPT0=|1448075644|21f41bafbff79f450f43eaac989c6410b51ed5d2"',
    'cap_id':r'"NDE4MjBmMDRiYjFkNGRiOTgyZmIzYzcxOGYwM2VmYzc=|1448075402|12974bc96b3a002ede5ee4d1fa9c9dfb21c0ee45"',
    '_za':r'6c806063-0f65-4b23-84a8-819fd3c351d2',
    '_xsrf':r'c11ef3683968e99311b2e8e95264f631',
    '__utma':r'51854390.1634618367.1447938509.1448072866.1448075246.11',
    '__utmb':r'51854390.12.10.1448075246',
    '__utmc':r'51854390',
    '__utmt':r'1',
    '__utmz':r'51854390.1448075246.11.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmv':r'51854390.100-2|2=registration_date=20151118=1^3=entry_date=20151118=1'
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rogary (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'rogary.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'rogary.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'rogary.pipelines.RogaryPipeline': 300,
    'rogary.pipelines.MongoDBPipeline': 300,
}
LOG_LEVEL = 'DEBUG'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

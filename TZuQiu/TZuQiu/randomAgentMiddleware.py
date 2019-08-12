# -*- coding: utf-8 -*-
import random
from TZuQiu.settings import USER_AGENT_LIST
from scrapy import logformatter


class MyUserAgentMiddleware(object):
    '''
    设置User-Agent
    '''

    def process_request(self, request, spider):
        agent = random.choice(USER_AGENT_LIST)
        if agent:
            request.headers['User-Agent'] = agent

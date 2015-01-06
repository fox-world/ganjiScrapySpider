# -*- coding: utf-8 -*-
import random

import settings as S

class ProxyMiddleware(object):

	def process_request(self,request,spider):
		request.meta['proxy']='http://%s' % (random.choice(S.PROXY_LIST))
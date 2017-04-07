#! /usr/bin/python

import falcon
import requests


class Resource(object):
    
    def on_get(self, req, resp):
        resp.body = '{"message" : "It Works"}'
        resp.status = falcon.HTTP_200



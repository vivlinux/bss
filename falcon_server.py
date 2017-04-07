#! /usr/bin/python

import falcon
import falcon_url

api = application = falcon.API()

url = falcon_url.Resource()

api.add_route('/', url)


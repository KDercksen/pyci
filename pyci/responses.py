#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def fail(msg):
    return json.dumps({
        'status': 'fail',
        'msg': msg,
    })


def success(msg, reqid):
    return json.dumps({
        'id': reqid,
        'status': 'success',
        'msg': msg,
    })

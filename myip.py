#!/usr/bin/env python3

import http.client
import json


def myip():
    conn = http.client.HTTPSConnection('wtfismyip.com')
    conn.request("GET", "/json")
    r = conn.getresponse()
    data = json.loads(r.read().decode('utf8'))
    return data


if __name__ == '__main__':
    print(myip())

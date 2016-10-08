#!/usr/bin/env python3

import asyncio


@asyncio.coroutine
def ping(loop, target):
    create =  asyncio.create_subprocess_exec('ping', '-c', '10', target,
                                          stdout=asyncio.subprocess.PIPE)
    proc = yield from create
    while True:
        line = yield from proc.stdout.readline()
        if line == b'':
            break
        l = line.decode('utf8').rstrip()
        print(l)

loop = asyncio.get_event_loop()
loop.run_until_complete(ping(loop, 'free.fr'))

loop.close()

#!/usr/bin/env python3

import asyncio


@asyncio.coroutine
def ping(loop, target, dump=False):
    create =  asyncio.create_subprocess_exec('ping', '-c', '10', target,
                                          stdout=asyncio.subprocess.PIPE)
    proc = yield from create
    lines = []
    while True:
        line = yield from proc.stdout.readline()
        if line == b'':
            break
        l = line.decode('utf8').rstrip()
        if dump:
            print(l)
        lines.append(l)
    transmited, received = [int(a.split(' ')[0]) for a
                            in lines[-2].split(', ')[:2]]
    stats, unit = lines[-1].split(' = ')[-1].split(' ')
    min_, avg, max_, stddev = [float(a) for a in stats.split('/')]
    return transmited, received, unit, min_, avg, max_, stddev

loop = asyncio.get_event_loop()
ping = loop.run_until_complete(ping(loop, 'free.fr'))
print(ping)

loop.close()

import redis
import os
from subprocess import Popen, PIPE, STDOUT

from pprint import pprint

r = redis.Redis(
    host='localhost',
    port=6379,
    password='')

# out = os.popen('cat `printf %s $HISTFILE`')
out = Popen("bash -i -c  'history -r;history' ", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
out = out.communicate()

print(type(out))
# print(out[0])
for line in out[0].decode("utf-8").splitlines():
    array = line.split()
    key = array[1] + ' ' + array[2]
    cmd_new =''
    for cmd in array[3:]:
        cmd_new += cmd + ' '

    joined_string = ' '.join([str(v) for v in array[3:]])
    # print(joined_string)
    r.hset("bash_history", key, joined_string)

#     break
# r.hset("bash_history", key, line)

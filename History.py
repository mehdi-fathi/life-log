import os
from subprocess import Popen, PIPE, STDOUT
from pprint import pprint
import AppClass


class history(AppClass.App):

    def __init__(self):
        AppClass.App.__init__(self)


    def save(self):

        out = Popen("bash -i -c  'history -r;history' ", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        out = out.communicate()

        for line in out[0].decode("utf-8").splitlines():
            array = line.split()
            key = array[1] + ' ' + array[2]
            cmd_new =''
            for cmd in array[3:]:
                cmd_new += cmd + ' '

            joined_string = ' '.join([str(v) for v in array[3:]])
            # print(joined_string)
            self.selfredis.hset("bash_history", key, joined_string)
        return ("Done it")



#     break
# r.hset("bash_history", key, line)

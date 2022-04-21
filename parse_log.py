#!/usr/bin/python3

import re

def parse1():
    with open("/home/feng/bug/1157238220.log.1", "r+") as f_log, open("/home/feng/bug/userid.txt", "r+") as f_user, open("/home/feng/bug/process1.log", "a") as f_process1:
        log_lines = f_log.readlines()
        for line in f_user.readlines():
            user_id = line.strip('\n')

            exit = False
            for log_line in log_lines:
                ret_exit = re.search(r"2022-03-29 ([0-9]{2}:[0-9]{2}:[0-9]{2}).*BMS user exit conference success.*" + user_id, log_line)
                if ret_exit:
                    f_process1.writelines([user_id, " ", ret_exit.group(1), "\n"])
                    exit = True
                    break

            if not exit:
                last_offline = ""
                last_online = ""
                for log_line in log_lines:
                    ret_offline = re.search(r"2022-03-29 ([0-9]{2}:[0-9]{2}:[0-9]{2}).*userOffline_handle.*" + user_id + ".*serviceType=0x1,.*channelType=50c", log_line)
                    if ret_offline:
                        last_offline = ret_offline.group(1)

                if last_offline != "":
                    for log_line in log_lines:
                        ret_online = re.search(r"2022-03-29 ([0-9]{2}:[0-9]{2}:[0-9]{2}).*userOnline_handle.*" + user_id + ".*serviceType=0x1,.*channelType=50c", log_line)
                        if ret_online:
                            last_online = ret_online.group(1)

                    if last_online != "":
                        if last_offline >= last_online:
                            f_process1.writelines([user_id, " ", last_offline, "\n"])
                        else:
                            f_process1.writelines([user_id, " 11:44:35\n"])
                    else:
                        print("not found %d online" % user_id)
                else:
                    f_process1.writelines([user_id, " 11:44:35\n"])


if __name__ == "__main__":
    parse1()

# log = [
#     {"time": "2021-04-27 07:58:54,256", "level": "[INFO]",
#      "msg": "Dumping current MySQL Servers structures for hostgroup ALL"},
#     {"time": "2021-04-27 07:58:54,256", "level": "[DEBUG]",
#      "msg": "Loading to runtime MySQL Users from peer proxysql-cluster.proxysql.svc.cluster.local:6032"},
#     {"time": "2021-04-27 09:30:54,256", "level": "[ERROR]",
#      "msg": "Error after 1009ms on server 10.0.1.72:3306 : timeout during ping"},
#     {"time": "2021-04-28 10:30:54,256", "level": "[ERROR]",
#      "msg": "Duplicate entry '6058-4006' for key 'interlocutors'"},
#     {"time": "2021-04-29 10:30:54,256", "level": "[WARNING]",
#      "msg": "1205, Lock wait timeout exceeded; try restarting transaction"}
# ]
# level = "INFO"
# for item in log:
#     if level in str(item.values()):
#         print(item)

# filter_id = [2, 5]
# for k, v in enumerate(filter_id):
#     print(k, v)
#     # if i == 1:
#     #     filter_id[i] = "RangeFilter"
#     # elif i == 2:
#     #     filter_id[i] = "InfoFilter"
#     # elif i == 3:
#     #     filter_id[i] = "DebugFilter"
#     # elif i == 4:
#     #     filter_id[i] = "WarningFilter"
#     # elif i == 5:
#     #     filter_id[i] = "ErrorFilter"
#
# print(filter_id)
# a = {"time": "2021-04-27 07:58:54,256", "level": "[INFO]"}
# a.values()
# content = {"filter_type": "FilterInfo,FilterError"}
# if "filter_type" not in content:
#     print("Bad request, filter type not implemented")
# if content["filter_type"] not in "FilterRange,FilterInfo,FilterDebug,FilterWarning,FilterError":
#     print("Bad request, filter type not valid")
a = {"filter_type": "FilterInfo", "id": 1}
print(1 in a.values())
fil = [{"filter_type": "FilterInfo", "id": 1},
       {"filter_type": "FilterError", "id": 2},
       {"filter_type": "FilterWarning", "id": 3}
       ]
ids = {"filter_ids": [1, 2, 3]}
a = '5'
a.isn
for id in ids["filter_ids"]:
    print(id)
    for filter in fil:
        print(filter.values())
        if id not in filter.values():
            print("Bad request, filter id not valid")

filter_many = ''
temp = ''
for id in ids["filter_ids"]:
    print(id)
    for filter in fil:
        if id == filter["id"]:
            temp = temp + filter["filter_type"] + ","
filter_many = {"filter_type": temp[:-1]}
# log = {"filter_type": filter_many[:-1]}
print(filter_many)

# for f in fil:
#        print(f["id"])
#        print(ids["filter_ids"])
#        print(f["id"] in ids["filter_ids"])

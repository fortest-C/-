import json
with open('data.json', 'r') as jdata:
    data = json.load(jdata)
print("msg1: ", data['msg1'])
print("msg6: ", data['msg6'])
print("MSG1: ", data['MSG1'])
print("msg9: ", data['msg9'])
print("msg2: ", data['msg2'])
print("MSG2: ", data['MSG2'])
print("msg7: ", data['msg7'])
print("msg4: ", data['msg4'])
print("msg8: ", data['msg8'])
print("msg5: ", data['msg5'])
print("MSG3: ", data['MSG3'])
'''
msg1:  遊戲是否進行中
msg6:  正式進入遊戲與否
MSG1:  ===== 分配後角色 =====#
msg9:  [玩家, 可否施法]
msg2:  [玩家, 毒藥, 藥水, 可否施法]
MSG2:  #====== 輔助變數 =====#
msg7:  [被選擇的人的號碼, 選擇者]
msg4:  [死者, 殺害者)]
msg8:  [代號,人名]
msg5:  day, night
'''
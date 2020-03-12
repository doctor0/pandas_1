import pandas as pd

def get_info_from_xxzx():
    df = pd.read_excel("xxzx_all.xlsx")
    df2 = pd.read_excel("results.xlsx")
    dic_ip = {}
    lists = []
    for sip in list(df2["IP"]):
        count = 0
        for dip in list(df["ip"]):
            temp = check(sip,dip)
            if(temp):
                # dic_ip['ip'] = sip
                # dic_ip['使用单位'] = sydw
                # dic_ip['设备名'] = sbm
                sydw = df[df["ip"] == dip]["sydw"].values.tolist()[0]
                sbm = df[df["ip"] == dip]["sbm"].values.tolist()[0]
                temp_list = [sip,sydw,sbm]
                count = 1
                break
            else:
                continue
                # dic_ip['ip'] = sip
                # dic_ip['使用单位'] = "未找到"
                # dic_ip['设备名'] = "未找到"
        if(count):
            lists.append(temp_list)
        else:
            lists.append([sip,"未找到","未找到"])
            count = 0
        # print(lists)
        # print(dic_ip)
    list_to_dict(lists)

def list_to_dict(list_n):
    len_a = len(list_n)
    list_sip = []
    list_dw = []
    list_sb = []
    for i in range(len_a):
        list_sip.append(list_n[i][0])
        list_dw.append(list_n[i][1])
        list_sb.append(list_n[i][2])
    dict = {'ip':list_sip,'使用单位':list_dw,'设备名':list_sb}
    concat_df(dict)

def concat_df(ma):
        data = pd.DataFrame(ma)
        data.to_excel('data.xlsx', sheet_name='data')

def check(sip,yuan_ip):
    ip3 = sip.split('.')
    yuan_ip3 = yuan_ip.split('.')
    yuan_p3 = yuan_ip.split('.')[3]
    if(ip3[0:3] == yuan_ip3[0:3]):
        if(ip3[3] == yuan_p3):
            return 1
        elif("-" in yuan_p3):
            have_p3 = list(range(int(yuan_p3.split('-')[0]),int(yuan_p3.split('-')[1])+1,1))
            if(int(ip3[3]) in have_p3):
                return 1
        else:
            return 0

def split_results():
    fp = open("qqq.txt","r")
    fp1 = open("dw.txt","w")
    fp2 = open("sb.txt","w")
    lines = fp.readlines()
    for line in lines:
        list1 = line.split(":")
        list2 = list1[2].split(",")[0]
        fp1.write(list2.strip(" ''")+"\n")
        fp2.write(list1[3].strip(" '").replace("'}",""))


if __name__ == "__main__":
    get_info_from_xxzx()
    # split_results()

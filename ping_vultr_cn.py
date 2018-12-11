import os
vultr_ip = {
'日本东京':'108.61.201.151',
'新加坡':'45.32.100.168',
'荷兰阿姆斯特丹':'108.61.198.102',
'法国巴黎':'108.61.209.127',
'德国法兰克福':'108.61.210.117',
'英国伦敦':'108.61.196.101',
'美国达拉斯':'108.61.224.175',
'美国西雅图':'108.61.194.105',
'美国芝加哥':'107.191.51.12',
'美国亚特兰大':'108.61.193.166',
'美国洛杉矶':'108.61.219.200',
'美国迈阿密':'104.156.244.232',
'美国纽约':'108.61.149.182',
'美国硅谷':'104.156.230.107',
'澳大利亚悉尼':'108.61.212.117',
}
for name,ip in vultr_ip.items():
    output = os.popen('ping -c 10 %s' % ip)
    info = output.readlines()
    for line in info:
        line = line.strip('\r\n')
        ping_result = str(line.encode('utf-8'))[34:-3]
        ping_result = ping_result.split('/')
    print(name)
    print('最小时延 '+ping_result[0]+' 最大时延 '+ping_result[2] \
            +' 时延标准差 '+ping_result[3] + ' 平均时延 '+ping_result[1])

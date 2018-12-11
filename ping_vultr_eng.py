import os
vultr_ip = {
'Tokyo, Japan':'108.61.201.151',
'Singapore':'45.32.100.168',
'Amsterdam, The Netherlands':'108.61.198.102',
'Paris, France':'108.61.209.127',
'frankfurt, Germany':'108.61.210.117',
'London, England':'108.61.196.101',
'Dallas, United States':'108.61.224.175',
'Seattle, USA':'108.61.194.105',
'Chicago, USA':'107.191.51.12',
'Atlanta, USA':'108.61.193.166',
'Los Angeles, USA':'108.61.219.200',
'Miami, USA':'104.156.244.232',
'New York, USA':'108.61.149.182',
'Silicon Valley, USA':'104.156.230.107',
'Sydney, Australia':'108.61.212.117',
}
for name,ip in vultr_ip.items():
    output = os.popen('ping -c 10 %s' % ip)
    info = output.readlines()
    for line in info:
        line = line.strip('\r\n')
        ping_result = str(line.encode('utf-8'))[34:-3]
        ping_result = ping_result.split('/')
    print(name)
    print('min delay '+ping_result[0]+' max delay '+ping_result[2] \
            +' delay stddev '+ping_result[3] + ' avg delay '+ping_result[1])

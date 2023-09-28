"""
컴퓨터 정보 확인 코드 만들기
cpu 속도, 물리 코어수, 메모리, 디스크, 네트워크 정보를 확인해 보자
"""

import psutil

# CPU의 속도를 출력
# Apple silicon 오류 https://github.com/giampaolo/psutil/issues/1892
# cpu = psutil.cpu_freq()
# print(cpu)

# CPU의 물리코어 수를 출력
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)
# -> 10

# 메모리 정보를 출력
memory = psutil.virtual_memory()
print(memory)
# -> svmem(total=34359738368, available=13272039424, percent=61.4, used=15905292288, free=362348544, active=12912377856, inactive=12777406464, wired=2992914432)

# 디스크 정보를 출력
disk = psutil.disk_partitions()
print(disk)
# -> 생략

# 네트워크를 통해 보내고 받은 데이터량을 출력
net = psutil.net_io_counters()
print(net)
# -> snetio(bytes_sent=266707968, bytes_recv=1350324224, packets_sent=1049032, packets_recv=4257772, errin=0, errout=0, dropin=0, dropout=0)
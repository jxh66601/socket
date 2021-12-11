import socket
import matplotlib.pyplot as plt
import numpy as np
import re
import matplotlib
from matplotlib.ticker import FuncFormatter
def main():
    # 1创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("",31500) # 必须绑定自己电脑IP和port
    udp_socket.bind(localaddr)
    # 3.接收数据
    while True:
        recv_data1 = udp_socket.recvfrom(10240) #cpu信息
        recv_data2 = udp_socket.recvfrom(10240) #内存信息
        recv_data3 = udp_socket.recvfrom(10240)  # swap信息
        recv_data4 = udp_socket.recvfrom(10240)  # 网速信息
        # recv_data存储元组（接收到的数据，（发送方的ip,port））
        #recv_msg = recv_data[0] # 信息内容
        #send_addr = recv_data[1] # 信息地址
        # 4.打印接收到的数据

        print('cpu信息')
        print(recv_data1)
        data1=str(recv_data1)
        data2=data1.split()
        #print(type(data1))
        list=[]  #cpu时间信息
        sum=0
        for i in range(1,10):
            list.append(data2[i])
            sum+=int(data2[i])
        cpuxl=round(int(data2[4])/sum,2) #cpu空闲
        #print(cpuxl)
        cpuxl1=round(1.00-cpuxl,1)
        #print(cpuxl1)
        #print('{:.2%}'.format(cpuxl1)) #cpu利用率
        a = str(cpuxl1 * 100) + '%'
        print(a)
        b = str(cpuxl * 100) + '%' #cpu空闲率
        print(b)

        print("内存信息")
        print(recv_data2)
        data3=str(recv_data2)
        data4=data3.split()
        #print(type(data4))
        #print(data4[1])
        #print(data4[3])
        mem=round((int(data4[1])-int(data4[3]))/(int(data4[1])),1)
        #print('{:.2%}'.format(mem))  # 内存利用率
        c = str(mem * 100) + '%'
        print(c)

        print('swap信息')
        print(recv_data3)
        data5=str(recv_data3)
        data6=data5.split()
        #print(type(data6))
        string=data6[1]

        list1=re.findall(r"\d+\.?\d*", string)
        swapus=round(int(list[1])/int(list1[0]),6)
        #print(swapus)
        d = str(swapus * 100) + '%'  # swap 闲置率
        print(d)
        swapus1=round(1-swapus,3)
        print(swapus1)
        e = str(swapus1 * 100) + '%'   #swap 闲置率
        print(e)
        #print(swapus)

        print("网速信息")
        print(recv_data4)
        data7=str(recv_data4)
        data8=data7.split()
        data8[46]=int(data8[46])
        wangsu1=round(int(data8[46]*1024)/int(data8[45]),2)
        wangsu2=str(wangsu1) + 'kb/s'     #传输速率，下
        print(wangsu2)
        g=wangsu2


        data8[38]=int(data8[38])
        wangsu2=round(int(data8[38]*1024)/int(data8[37]),2)
        wangsu3 = str(wangsu2) + 'kb/s'        #接受速录 上
        print(wangsu3)
        f=wangsu3


        matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文

        x=np.array(['cpu','cpu ideal','memory','swap','swap ideal','receive','transmit'])
        y=np.array([a,b,c,d,e,f,g])
        #print(y[0])
        plt.bar(x,y, label='百分比', color='steelblue', alpha=0.8)


        # 设置标题
        plt.title("虚拟机性能表")
        # 为两条坐标轴设置名称
        plt.xlabel("ubuntu")
        plt.ylabel("百分比")
        # 显示图例
        plt.legend()
        plt.savefig("a.jpg")
        plt.show()
        #print("信息来自:%s 内容是:%s" %(str(send_addr),recv_msg.decode("utf-8")))
    # 5.退出套接字
    udp_socket.close()
if __name__ == "__main__":
    main()

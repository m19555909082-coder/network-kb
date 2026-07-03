# 第6章 网络地址转换(NAT) — NAT负载均衡

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 33：1、建立内部地址池，其中的地址必须是各服务器的真实地址(加上rotary关键字)。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

1、建立内部地址池，其中的地址必须是各服务器的真实地址(加上rotary关键字)。
2、建立访问控制列表，定义转换的合法IP地址
3、用地址池和访问控制列表建立映射

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

1. Create an internal pool of addresses that must be the real addresses of each server (plus the rotary keyword).
R1(config)# ip nat pool p1 192.168.1.1 192.168.1.2 netmask 255.255.255.0 rotary
2. Establish the access control list and define the legal IP address of the transformation
R1(config)# access-list 1 permit host 200.1.1.1
3.Establish the mapping with an address pool and an access control list
R1(config)# ip nat inside source  list 1 pool p1

</div>

---

### 📄 Slide 34：4、指定NAT入口(E0口)和出口(S0口)

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

4、指定NAT入口(E0口)和出口(S0口)
配置了TCP负载均衡后，路由器会把对地址200.1.1.1的访问交替映射到192.168.1.1~192.168.1.2的各个地址上，使它们访问不同的服务器主机。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

4、指定NAT入口(E0口)和出口(S0口)
4. Specify NAT entry (E0 port) and exit (S0 port)
R1(config)# interface e0
R1(config-if)# ip nat inside
R1(config-if)# interface s0
R1(config-if)# ip nat outside
配置了TCP负载均衡后，路由器会把对地址200.1.1.1的访问交替映射到192.168.1.1~192.168.1.2的各个地址上，使它们访问不同的服务器主机。
With TCP load balancer configured, the router will map access to addresses 200.1.1.1 to addresses 192.168.1.1 through 192.168.1.2, making each visit to a different server host.

</div>
**💻 配置命令：**

```cisco
R1(config)# interface e0
R1(config-if)# ip nat inside
R1(config-if)# interface s0
R1(config-if)# ip nat outside
```


---

### 📄 Slide 35：4、指定NAT入口(E0口)和出口(S0口)

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

4、指定NAT入口(E0口)和出口(S0口)
对使用TCP负载均衡的各服务器必须建立为镜像服务器，它们可通过同步保持内容的一致性。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

4、指定NAT入口(E0口)和出口(S0口)
4. Specify NAT entry (E0 port) and exit (S0 port)
Each server using TCP load balancing must be set up as a mirror server, and they can maintain the consistency of content through synchronization.

</div>

---

### 📄 Slide 36：小型NAT设备和无线路由器

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

小型NAT设备和无线路由器
通常家庭或独立小型办公室，多台PC需要共享访问因特网时，不需要申请多个独立的DSL Modem，而只需要购置一个小型NAT设备，通常家庭无线路由器具有NAT功能。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Small NAT devices and wireless routers
Usually a family or an independent small office, multiple PCS need to share access to the Internet, do not need to apply for multiple independent DSL Modem, but only need to buy a small NAT equipment, usually the home wireless router has NAT function.

</div>

---

### 📄 Slide 37：NAT配置举例Example NAT configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1是局域网的边界路由器，R2是ISP的路由器。
局域网使用私有地址192.168.1.0/24进行编址。
ISP为局域网分配了一个合法地址块60.10.10.0/29。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT配置举例Example NAT configuration
192.168.1.0/24
E0: .1
200.1.1.0/24
S0: .2
S0: .1
R1
R2
DCE
PC1: .51
PC2: .52
E0:50.1.1.1/8
PC3:50.1.1.2/8
R1 is the border router of the LAN and R2 is the router of the ISP.
局域网使用私有地址192.168.1.0/24进行编址。
The LAN is addressed using the private address 192.168.1.0/24.
ISP为局域网分配了一个合法地址块60.10.10.0/29。
The ISP allocated a legal address block 60.10.10.0/29 for the LAN.

</div>

---

### 📄 Slide 38：分析：Analysis

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

地址范围为：60.10.10.0~60.10.10.7，共8个地址。
其中可用的地址是60.10.10.1~60.10.10.6，共6个地址。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

分析：Analysis
地址块(address block:) ：60.10.10.0/29
1111 1111  1111 1111  1111 1111  1111 1000
掩码为(The mask is) 255.255.255.248。
地址范围为：60.10.10.0~60.10.10.7，共8个地址。
The address range is 60.10.10.0 to 60.10.10.7, with 8 addresses in total.
其中可用的地址是60.10.10.1~60.10.10.6，共6个地址。
There are six addresses in the range 60.10.10.1 to 60.10.10.6.

</div>

---

### 📄 Slide 39：R1的配置：采用复用NAT池技术使用6个合法IP地址。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1的配置：采用复用NAT池技术使用6个合法IP地址。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Configuration of R1: six legitimate IP addresses are used by multiplexing NAT pool technology.
R1(config)# ip nat pool pool1 60.10.10.1 60.10.10.6 netmask 255.255.255.248
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R1(config)# ip nat inside source list 1 pool pool1 overload
R1(config)# interface e0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# ip nat inside
R1(config-if)# no shutdown

</div>
**💻 配置命令：**

```cisco
Configuration of R1: six legitimate IP addresses are used by multiplexing NAT pool technology.
R1(config)# ip nat pool pool1 60.10.10.1 60.10.10.6 netmask 255.255.255.248
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R1(config)# ip nat inside source list 1 pool pool1 overload
R1(config)# interface e0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# ip nat inside
R1(config-if)# no shutdown
```


---

### 📄 Slide 40：R1(config)# interface s0

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在R1上配置默认路由，把所有非本网络的请求都发往外网。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# interface s0
R1(config-if)# ip address 200.1.1.2 255.255.255.0
R1(config-if)# ip nat outside
R1(config-if)# no shutdown
R1(config-if)# exit
Configure the default route on R1 to route all requests that are not from the local network to the external network.
R1(config)# ip route 0.0.0.0 0.0.0.0 200.1.1.1

</div>
**💻 配置命令：**

```cisco
R1(config)# interface s0
R1(config-if)# ip address 200.1.1.2 255.255.255.0
R1(config-if)# ip nat outside
R1(config-if)# no shutdown
Configure the default route on R1 to route all requests that are not from the local network to the external network.
R1(config)# ip route 0.0.0.0 0.0.0.0 200.1.1.1
```

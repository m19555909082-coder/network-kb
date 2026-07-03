# 第6章 网络地址转换(NAT) — PAT端口地址转换

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 25：R1(config)# ip nat pool ippool 200.1.1.1 200.1.1.254 netmask 255.255.255.0

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1(config)# ip nat pool ippool 200.1.1.1 200.1.1.254 netmask 255.255.255.0
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 pool ippool
R1(config)# interface f0/0
R1(config-if)# ip nat inside
R1(config-if)# interface s0/0
R1(config-if)# ip nat outside

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# ip nat pool ippool 200.1.1.1 200.1.1.254 netmask 255.255.255.0
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 pool ippool
R1(config)# interface f0/0
R1(config-if)# ip nat inside
R1(config-if)# interface s0/0
R1(config-if)# ip nat outside

</div>
**💻 配置命令：**

```cisco
R1(config)# ip nat pool ippool 200.1.1.1 200.1.1.254 netmask 255.255.255.0
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 pool ippool
R1(config)# interface f0/0
R1(config-if)# ip nat inside
R1(config-if)# interface s0/0
R1(config-if)# ip nat outside
```


---

### 📄 Slide 26：复用NAT池  Reuse the NAT pool

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

当NAT池中的地址耗尽时，会导致后来的主机无法上网。所以当内网的主机数超过NAT池中的地址数时，通常应配置成复用NAT池，这样每个IP地址可对应多个会话，各个会话用端口号进行区分。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

复用NAT池  Reuse the NAT pool
When the addresses in the NAT pool are exhausted, it causes the subsequent hosts to be unable to access the Internet. When the number of hosts in the internal network exceeds the number of addresses in the NAT pool, it is common to configure the NAT pool to be multiplexed so that each IP address can be associated with multiple sessions, and each session is distinguished by a port number.

</div>

---

### 📄 Slide 27：复用NAT池  Reuse the NAT pool

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

理论上讲，一个IP地址可以映射约65000个会话，但实际的路由器往往只支持几千个会话（Cisco支持约4000个）。
在复用NAT池中，Cisco首先复用地址池中的第一个地址，达到能力极限后，再复用第二个地址，依此类推。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

复用NAT池  Reuse the NAT pool
In theory, an IP address can map to about 65,000 sessions, but in practice routers tend to support only a few thousand sessions (Cisco supports about 4,000).
In the multiplexed NAT pool, Cisco first reuses the first address in the address pool, and when it reaches its capacity limit, it reuses the second address, and so on.

</div>

---

### 📄 Slide 28：复用NAT池的配置方法与NAT池的配置方法基本相同，只是：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

复用NAT池的配置方法与NAT池的配置方法基本相同，只是：
在上面的命令中加上 overload 关键字表示使用端口复用技术。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

The configuration for a multiplexed NAT pool is basically the same as the NAT pool configuration, except:
Router(config)# ip nat inside source list ACL表号 pool 地址池名字  overload
在上面的命令中加上 overload 关键字表示使用端口复用技术。
Adding the overload keyword to the preceding command indicates port reuse.

</div>
**💻 配置命令：**

```cisco
Router(config)# ip nat inside source list ACL表号 pool 地址池名字  overload
```


---

### 📄 Slide 29：PAT

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

PAT是复用NAT池的特例，它是通过端口复用技术用于一个合法IP地址映射内网的所有私有IP地址，这个地址往往就是路由器出口的IP地址。
上例中，把内网的私有IP地址都映射为R1的S0/0口的IP地址就是PAT。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

PAT
PAT is a special case of multiplexing NAT pool, which uses port multiplexing technology to map a legitimate IP address to all private IP addresses in the internal network, which is often the IP address of the router exit.
10.0.0.0/8
R1
f0/0
s0/0: 195.4.10.2
上例中，把内网的私有IP地址都映射为R1的S0/0口的IP地址就是PAT。
In the above example, PAT is the IP address of R1's S0/0 port that maps all the private IP addresses of the internal network to R1.

</div>

---

### 📄 Slide 30：PAT的配置方法可以使用复用NAT池的配置方法，只要建立一个起始地址和结束地址相同的NAT池就行了。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

PAT的配置方法可以使用复用NAT池的配置方法，只要建立一个起始地址和结束地址相同的NAT池就行了。
也可以不建立NAT池，用以下命令进行配置：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

The PAT configuration method can use the multiplexed NAT pool configuration method, simply create a NAT pool with the same start address and end address.
It is also possible to configure the NAT pool without setting it up, using the following command:
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 interface s0/0 overload
R1(config)# interface f0/0
R1(config-if)# ip nat inside
R1(config-if)# interface s0/0
R1(config-if)# ip nat outside

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 interface s0/0 overload
R1(config)# interface f0/0
R1(config-if)# ip nat inside
R1(config-if)# interface s0/0
R1(config-if)# ip nat outside
```


---

### 📄 Slide 31：PAT可最大限度的节省IP地址用量，但由于它只能同时支持几千个会话，所以使用PAT易造成拥塞。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

PAT可最大限度的节省IP地址用量，但由于它只能同时支持几千个会话，所以使用PAT易造成拥塞。
为了避免PAT和复用NAT池的拥塞，一方面可以多申请一些IP地址，建立一个大些的NAT池，另一方面也应该限制用户使用那些占用会话数很多的应用（如BT）。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

PAT can save IP address usage to the greatest extent, but it can only support thousands of sessions at the same time, so using PAT is prone to congestion.
PAT can save IP address usage to the greatest extent, but it can only support thousands of sessions at the same time, so using PAT is prone to congestion.

</div>

---

### 📄 Slide 32：TCP负载均衡TCP Load Balancing

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

TCP负载均衡是为了把一个外部的合法地址交替映射到多个内部地址上，这样可以使多台服务器使用同一个外部地址进行访问。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

TCP负载均衡TCP Load Balancing
The purpose of TCP load balancing is to map an external valid address to multiple internal addresses alternately, so that multiple servers can use the same external address to access.
192.168.1.1
192.168.1.2
S0:200.1.1.1/24
E0

</div>
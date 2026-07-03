# 第6章 网络地址转换(NAT) — NAT与路由综合

> 7 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 41：R2的配置：R2 configuration:

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置到达网络 60.10.10.0/29 的静态路由：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R2的配置：R2 configuration:
R2(config)# interface s0
R2(config-if)# ip address 200.1.1.1 255.255.255.0
R2(config-if)# clock rate 64000
R2(config-if)# no shutdown
R2(config-if)# interface e0
R2(config-if)# ip address 50.1.1.1 255.0.0.0
R2(config-if)# no shutdown
配置到达网络 60.10.10.0/29 的静态路由：
Configure the static route to network 60.10.10.0/29:
R2(config)# ip route 60.10.10.0 255.255.255.248 200.1.1.2

</div>
**💻 配置命令：**

```cisco
R2(config)# interface s0
R2(config-if)# ip address 200.1.1.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# interface e0
R2(config-if)# ip address 50.1.1.1 255.0.0.0
R2(config-if)# no shutdown
Configure the static route to network 60.10.10.0/29:
R2(config)# ip route 60.10.10.0 255.255.255.248 200.1.1.2
```


---

### 📄 Slide 42：关于NAT边界的路由配置问题On the NAT boundary routing configuration issues

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

局域网和ISP的网络一般应看作为两个自治系统，所以两者之间不能通过RIP等协议学习路由。
在NAT路由器和与它相连的路由器间一般通过静态路由或默认路由实现两边网络的连通。
NAT路由器一般配置通往外网的默认路由。
ISP的路由器通过配置静态路由为局域网分配IP地址段。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

关于NAT边界的路由配置问题On the NAT boundary routing configuration issues
LAN and ISP should be regarded as two autonomous systems, so they can not learn routing through RIP.
The connection between NAT router and its connected router is usually realized by static route or default route.
NAT routers are typically configured with default routes to the public network.
The ISP's router assigns IP address segments to the LAN by configuring static routing.

</div>

---

### 📄 Slide 43：小结  Brief Summary

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

定义NAT入口和出口（任何一种NAT）：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

小结  Brief Summary
R1
E0
S0
192.168.*.*
192.168.1.1/24
200.1.1.1/24
Internet
定义NAT入口和出口（任何一种NAT）：
Define NAT entry and exit (any kind of NAT) :
R1(config)# interface 入口
R1(config-if)# ip nat inside
R1(config-if)# interface 出口
R1(config-if)# ip nat outside

</div>
**💻 配置命令：**

```cisco
R1(config)# interface 入口
R1(config-if)# ip nat inside
R1(config-if)# interface 出口
R1(config-if)# ip nat outside
```


---

### 📄 Slide 44：静态NAT：Static NAT

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

带有overload关键字时，为复用NAT池。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

静态NAT：Static NAT
R1(config)# ip nat inside source static 内部地址 外部地址
NAT池：NAT  pool
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 pool 池名 [overload]
带有overload关键字时，为复用NAT池。
The overload keyword is used to reuse the NAT pool.

</div>

---

### 📄 Slide 45：PAT：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

PAT：
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 interface 出口 overload
TCP负载均衡： TCP Load Balancing:
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码 rotary
R1(config)# access-list 表号 permit host 外部地址
R1(config)# ip nat inside source  list 表号 pool 池名

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

PAT：
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 interface 出口 overload
TCP负载均衡： TCP Load Balancing:
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码 rotary
R1(config)# access-list 表号 permit host 外部地址
R1(config)# ip nat inside source  list 表号 pool 池名

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 interface 出口 overload
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码 rotary
R1(config)# access-list 表号 permit host 外部地址
R1(config)# ip nat inside source  list 表号 pool 池名
```


---

### 📄 Slide 46：NAT网关的路由配置：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

NAT网关的路由配置：
通常情况下，NAT路由器不能配置路由协议，只能配置静态路由。
NAT网关
外部路由器
NAT网关：一般配置成默认路由。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT gateway routing configuration:
In general, NAT routers cannot configure routing protocols, only static routes.
R1
E0
S0
192.168.*.*
192.168.1.1/24
200.1.1.1/24
NAT网关
NAT gateway
exterior router
R2
NAT gateway: This is typically configured as the default route.
R1(config)# ip route 0.0.0.0 0.0.0.0  下一跳地址

</div>

---

### 📄 Slide 47：外部路由器：需要为局域网分配地址块。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

外部路由器：需要为局域网分配地址块。
R2(config)# ip route 地址块 地址块掩码 下一跳地址

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

External routers: Address blocks need to be allocated for the LAN.
R2(config)# ip route 地址块 地址块掩码 下一跳地址
R2(config)# ip route   Address block    Address block mask
Next hop address

</div>
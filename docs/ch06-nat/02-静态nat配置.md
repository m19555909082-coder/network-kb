# 第6章 网络地址转换(NAT) — 静态NAT配置

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 9：2、NAT池（动态NAT）：2. NAT Pool (dynamic NAT) :

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

将多个合法IP地址统一的组织起来，构成一个IP地址池，当有主机需要访问外网时，就分配一个合法IP地址与内部地址进行转换，当主机用完后，就归还该地址。
对于NAT池，如果同时联网用户太多，可能出现地址耗尽的问题。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

2、NAT池（动态NAT）：2. NAT Pool (dynamic NAT) :
A number of legal IP address unified organization, constitute an IP address pool, when a host needs to access the external network, the allocation of a legal IP address and internal address conversion, when the host is used up, the return of the address.
With NAT pools, we can run out of addresses if too many users are connected at the same time.
192.168.1.1
192.168.1.2
NAT池

</div>

---

### 📄 Slide 10：3、PAT（端口NAT）：3, PAT (port NAT) :

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

使用端口多路复用技术，将多个内部地址映射为一个合法地址，用不同的端口号区分各个内部地址。这种方法只需要一个合法IP地址。
路由器支持的PAT会话数是有限制的，所以使用PAT的局域网，其网络的规模不应该太大。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

3、PAT（端口NAT）：3, PAT (port NAT) :
Multiple internal addresses are mapped to a legal address by using port multiplexing technology, and each internal address is distinguished by different port numbers. This method requires only one legitimate IP address.
The number of PAT sessions supported by a router is limited, so the size of the LAN using PAT should not be too large.
192.168.1.1
192.168.1.2
S0:200.1.1.1/24

</div>

---

### 📄 Slide 11：4、复用NAT池（复用动态NAT）：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

4、复用NAT池（复用动态NAT）：
将多个合法IP地址构成一个NAT池，使用复用技术映射其中的地址，每个地址有可以对应多台主机，各主机用端口进行区分。
复用NAT池是NAT池和PAT技术的结合，可用于大规模的局域网。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

4、复用NAT池（复用动态NAT）：
4. Reuse NAT pool (reuse dynamic NAT) :
Several legal IP addresses are used to form a NAT pool, and the addresses in the pool are mapped by multiplexing technology. Each address can correspond to multiple hosts, and each host is distinguished by port.
NAT pool multiplexing is the combination of NAT pool and PAT technology, which can be used in large scale LAN.

</div>

---

### 📄 Slide 12：4、复用NAT池（复用动态NAT）：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

4、复用NAT池（复用动态NAT）：
说明：在端口复用技术中，用端口区分的不是一台主机，而是一个网络连接（会话），当一台主机同时建立了多个会话时，它的每个会话会占用一个端口映射。假如一台路由器支持4000个会话，那么它支持的主机数量会远少于4000台。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

4、复用NAT池（复用动态NAT）：
4. Reuse NAT pool (reuse dynamic NAT) :
Note: In port reuse technology, a port is not used to distinguish a host, but a network connection (session), when a host simultaneously establishes more than one session, its each session will occupy a port map. If a router supports 4,000 sessions, it will support far fewer hosts.

</div>

---

### 📄 Slide 13：5、TCP负载均衡：5. TCP load balancing:

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

如果一个服务器的访问量非常大，我们通常会建立多台映像服务器对访问进行分流。从外部来看，这些服务器的IP地址相同，NAT设备会把多个对服务器的访问映射到不同的服务器上，实现负载均衡。
TCP负载均衡与其它NAT的主要区别在于，它是把来自外网的同一合法IP地址翻译成不同的内网IP地址。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5、TCP负载均衡：5. TCP load balancing:
If the traffic to a server is very high, we usually set up multiple image servers to spread the traffic. From the outside, these servers have the same IP address, and the NAT device maps multiple accesses to different servers to achieve load balancing.
192.168.1.1
192.168.1.2
S0:200.1.1.1/24
The main difference between TCP load balancer and other Nats is that it translates the same legitimate IP address from the external network into a different internal IP address.

</div>

---

### 📄 Slide 14：常用NAT设备Common NAT Devices

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

实现NAT可以使用不同的设备，它们的基本功能相同，但功能强弱有别，应根据需要进行选用。常用的设备有：
1、路由器：功能强，支持多种NAT设置；
2、防火墙：除NAT转换外，还提供多种保护功能；
3、代理服务器：提供局域网接入功能；
4、双网卡计算机：功能较弱，多用于小型网络。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

常用NAT设备Common NAT Devices
NAT can be implemented using different devices, their basic functions are the same, but the strength of the function is different, should be selected according to the need. Commonly used devices are:
1, router: powerful, support a variety of NAT Settings;
2, firewall: in addition to NAT conversion, but also provide a variety of protection functions;
3, proxy server: provide LAN access function;
4, dual network card computer: weak function, mostly used for small networks.

</div>

---

### 📄 Slide 15：6.2 NAT的配置  NAT configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

6.2 NAT的配置  NAT configuration
静态NAT   Static  NAT
NAT池      NAT  pool
PAT
复用NAT池     Reuse the NAT pool
TCP负载均衡    TCP Load Balancing

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

6.2 NAT的配置  NAT configuration
静态NAT   Static  NAT
NAT池      NAT  pool
PAT
复用NAT池     Reuse the NAT pool
TCP负载均衡    TCP Load Balancing

</div>

---

### 📄 Slide 16：静态NAT   Static NAT

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

把私有地址和合法地址作一对一地转换。
另外，还需要把E0口指定为NAT内部接口，S0口指定为NAT外部接口。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

静态NAT   Static NAT
Translate private addresses to legitimate addresses one-to-one.
192.168.1.1
192.168.1.2
200.10.1.5
200.10.1.6
E0
S0
配置命令：   The configuration command:
Router(config)# ip nat inside source static 内部地址 外部地址
It is also necessary to specify E0 as the internal NAT interface and S0 as the external NAT interface.

</div>
**💻 配置命令：**

```cisco
Router(config)# ip nat inside source static 内部地址 外部地址
It is also necessary to specify E0 as the internal NAT interface and S0 as the external NAT interface.
```

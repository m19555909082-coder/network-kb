# 第6章 网络地址转换(NAT) — NAT概述与地址类型

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 1：第6章 网络地址转换NATChapter 6, Network Address Translation  NAT

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

第6章 网络地址转换NATChapter 6, Network Address Translation  NAT

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

第6章 网络地址转换NATChapter 6, Network Address Translation  NAT

</div>

---

### 📄 Slide 2：6.1 NAT概述  6.1 NAT Overview

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

NAT是将一个IP地址转换为另一个IP地址的功能。
通常，一个局域网由于申请不到足够多的IP地址，或者只是为了编址方便，在局域网内部采用私有IP地址为设备编址，当设备访问外网时，再通过NAT将私有地址翻译为合法地址。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

6.1 NAT概述  6.1 NAT Overview
NAT is a function that translates one IP address into another.
Usually, a LAN can not apply for enough IP addresses, or just for the convenience of addressing, the private IP address is used to address the device in the LAN. When the device accesses the external network, the private address is translated into the legal address through NAT.

</div>

---

### 📄 Slide 3：局域网专用IP地址LAN dedicated IP address

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

局域网专用IP地址是Internet特别划分出来的，它们不会注册给任何组织。
实际上，用户可以使用任意IP作为私有地址，但有可能导致某些外网的站点无法访问。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

局域网专用IP地址LAN dedicated IP address
LAN IP addresses are specially designated by the Internet and are not registered with any organization.
In fact, users can use any IP as a private address, but it may cause some external sites to be inaccessible.

</div>

---

### 📄 Slide 4：使用私有地址的注意事项：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

使用私有地址的注意事项：
私有地址不需要经过注册就可以使用，这导致这些地址是不唯一的。所以私有地址只能限制在局域网内部使用，不能把它们路由到外网中去。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Some notes on using private addresses:
Private addresses do not need to be registered to be used, which causes these addresses to be non-unique. Therefore, private addresses can only be used within the local area network, and they cannot be routed to the outside network.

</div>

---

### 📄 Slide 5：R1

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1是局域网和外网的边界路由器。局域网中使用私有IP地址进行编址。如果在R1上启用RIP协议，则：
×
这里不应该在私有地址上启用路由，它会导致私有地址被外网路由器学习到，扩大了它的有效范围。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1
E0
S0
192.168.*.*
192.168.1.1/24
200.1.1.1/24
Internet
R1 is the border router between the LAN and the extranet. Private IP addresses are used for addressing in local area networks. If RIP is enabled on R1, then:
R1(config)# router rip
R1(config-router)# network 200.1.1.0
R1(config-router)# network 192.168.1.0
Here routing should not be enabled on the private address, it will cause the private address to be learned by the external network router, expanding its effective range.

</div>

---

### 📄 Slide 6：NAT基本原理NAT Basic Principle

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

当一个使用私有地址的数据包到达NAT设备时，NAT设备负责把私有IP地址翻译成外部合法IP地址，然后再转发数据包，反之亦然。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT基本原理NAT Basic Principle
When a packet arrives at a NAT device using a private address, the NAT device is responsible for translating the private IP address into an external legal IP address before forwarding the packet, and vice versa.

</div>

---

### 📄 Slide 7：NAT基本原理NAT Basic Principle

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

端口多路复用技术：NAT支持把多个私有IP地址映射为一个合法IP地址的技术，这时各个主机通过端口进行区分，这就是端口多路复用技术。
利用端口多路复用技术可节省合法IP地址的使用量，但会加大NAT设备的负担，影响其转发速度。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT基本原理NAT Basic Principle
Port Multiplexing technology: NAT supports multiple private IP address mapping to a legal IP address technology, then each host by the port to distinguish, this is the port multiplexing technology.
The use of port multiplexing technology can save the amount of legal IP address, but it will increase the burden of NAT devices and affect their forwarding speed.

</div>

---

### 📄 Slide 8：NAT类型   NAT type

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

将内部地址和外部地址进行一对一的转换。这种方法要求申请到的合法IP地址足够多，可以与内部IP地址一一对应。
静态NAT一般用于那些需要固定的合法IP地址的主机，比如Web服务器、FTP服务器、E-mail服务器等。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT类型   NAT type
1、静态NAT：1. Static NAT:
One-to-one conversion of internal and external addresses is performed. This method requires that enough legitimate IP addresses can be applied to correspond to internal IP addresses.
静态NAT一般用于那些需要固定的合法IP地址的主机，比如Web服务器、FTP服务器、E-mail服务器等。
Static Nats are typically used for Web servers, FTP servers, E-mail servers, and so on, which require a fixed legal IP address.
192.168.1.1
192.168.1.2
200.10.1.5
200.10.1.6

</div>
# 第2章 扩展办公网络 — 生成树协议STP

> 10 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 23：办公网络优化之----生成树技术Spanning tree technology for office network optimization

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在目前常用的技术中，以生成树技术（STP）和链路聚合（Link Aggregation）技术应用最为广泛。链路聚合技术提供了传输线路内部的冗余机制，链路聚合成员彼此互为冗余和动态备份。而生成树协议提供了链路间的冗余方案，允许交换机间存在多条链路作为主链路的备份。
使用备份连接，可以提高网络的健全性、稳定性。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

办公网络优化之----生成树技术Spanning tree technology for office network optimization
Among the commonly used technologies, spanning tree technology (STP) and Link Aggregation technology are the most widely used. Link aggregation technology provides a redundancy mechanism in the transmission line, and link aggregation members are redundant and dynamic backup of each other. The spanning tree protocol provides an inter-link redundancy scheme, allowing multiple links between switches as backups of the primary link.
Using backup connection can improve the soundness and stability of the network.

</div>

---

### 📄 Slide 24：办公网络优化之----生成树技术Spanning tree technology for office network optimization

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

办公网络优化之----生成树技术Spanning tree technology for office network optimization

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

办公网络优化之----生成树技术Spanning tree technology for office network optimization

</div>

---

### 📄 Slide 25：交换网络中的冗余链路

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

交换网络中的冗余链路
故障
在网络中提供冗余链路解决单点故障问题

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Redundant links in the switching network
fault
Redundant links are provided in the network to solve the problem of single point of failure

</div>

---

### 📄 Slide 26：冗余链路出现的问题(1):广播风暴

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

冗余链路出现的问题(1):广播风暴
发送一个广播帧
广播风暴

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Problem with redundant links (1): broadcast storm
Send a broadcast frame
broadcast storm

</div>

---

### 📄 Slide 27：冗余链路出现的问题(2):地址表不稳定

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

冗余链路出现的问题(2):地址表不稳定

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Redundant link problem (2): address table instability

</div>

---

### 📄 Slide 28：冗余链路出现的问题(3):多帧复制

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

冗余链路出现的问题(3):多帧复制

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Problem of redundant links (3): multiple frame replication

</div>

---

### 📄 Slide 29：产生环路

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

产生环路
环路问题将会导致：广播风暴、多帧复制，MAC地址表的不稳定等问题。

</div>

---

### 📄 Slide 30：解决方法：环临时生成树思想Solution: Ring temporary spanning tree idea

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

临时关闭网络中冗余的链路

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

解决方法：环临时生成树思想Solution: Ring temporary spanning tree idea
Temporarily shut down redundant links in the network

</div>

---

### 📄 Slide 31：生成树协议STP 的基本概念Basic concept of spanning Tree Protocol STP

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

生成树协议（STP）   ：   IEEE802.1d标准
主要思想是:网络中存在备份链路时，只允许主链路激活，如果主链路因故障而被断开后，备用链路才会被打开。
主要作用：避免回路，冗余备份。
生成树协议实现交换网络中，生成没有环路的网络，主链路出现故障，自动切换到备份链路，保证网络的正常通信。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

生成树协议STP 的基本概念Basic concept of spanning Tree Protocol STP
生成树协议（STP）   ：   IEEE802.1d标准
Spanning Tree Protocol (STP) : IEEE802.1d standard
The main idea is that when there is a backup link in the network, only the primary link is allowed to be active. If the primary link is disconnected due to failure, the backup link will be opened.
Main function: avoid loop, redundant backup.
In the switching network, the spanning tree protocol generates a network without loop. When the main link fails, it automatically switches to the backup link to ensure the normal communication of the network.

</div>

---

### 📄 Slide 32：RSTP基本配置

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

RSTP基本配置
略

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

RSTP基本配置

</div>
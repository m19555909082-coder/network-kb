# 第4章 构建园区网络 — RIP路由协议

> 7 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 34：配置RIP协议 Configuring RIP Protocol

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置RIP协议 Configuring RIP Protocol
1、开启RIP路由协议进程(Start RIP routing protocol process)
Router(config)#router rip
2、申请本路由器参与RIP协议的直连网段信息(Request the information of direct network segment of this router to participate in RIP protocol)
Router(config-router)#network 192.168.1.0
3、指定RIP协议的版本2(默认是version1)(Specifies version 2 of the RIP protocol (default version1).)
Router(config-router)#version  2
4、在RIPv2版本中关闭自动汇总(Turn off automatic summarization in RIPv2 versions)
Router(config-router)#no auto-summary

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

配置RIP协议 Configuring RIP Protocol
1、开启RIP路由协议进程(Start RIP routing protocol process)
Router(config)#router rip
2、申请本路由器参与RIP协议的直连网段信息(Request the information of direct network segment of this router to participate in RIP protocol)
Router(config-router)#network 192.168.1.0
3、指定RIP协议的版本2(默认是version1)(Specifies version 2 of the RIP protocol (default version1).)
Router(config-router)#version  2
4、在RIPv2版本中关闭自动汇总(Turn off automatic summarization in RIPv2 versions)
Router(config-router)#no auto-summary

</div>
**💻 配置命令：**

```cisco
Router(config)#router rip
2、申请本路由器参与RIP协议的直连网段信息(Request the information of direct network segment of this router to participate in RIP protocol)
Router(config-router)#network 192.168.1.0
Router(config-router)#version  2
Router(config-router)#no auto-summary
```


---

### 📄 Slide 35：RIP路由协议的版本

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

RIP路由协议的版本
有类路由协议，不支持VLSM
以广播的形式发送更新报文
不支持认证
无类路由协议，支持VLSM
以组播的形式发送更新报文
支持明文和MD5的认证

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

RIP路由协议的版本
RIPv1
RIPv2
无类路由协议，支持VLSM

</div>

---

### 📄 Slide 36：OSPF协议

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

OSPF协议

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

OSPF协议
OSPF protocol

</div>

---

### 📄 Slide 37：OSPF简介 Introduction to OSPF

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

链路状态路由协议，克服了RIP的两个致命弱点
骨干区域Area 0，非骨干区域Area N
骨干区域保持连续性，非骨干区域一定要与骨干区域连接

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

OSPF简介 Introduction to OSPF
Link-state routing protocol overcomes the two fatal weaknesses of RIP
收敛速度慢（240秒以上）（Slow convergence (> 240 seconds)）
规模限制，只有15跳（Size limit, only 15 hops）
分区域概念：Subregional concepts:
骨干区域Area 0，非骨干区域Area N
The backbone Area is Area 0 and the non-backbone area is Area N
The backbone region is continuous, and the non-backbone region must be connected to the backbone region
RFC 2328定义（Defined in RFC 2328）

</div>

---

### 📄 Slide 38：交换Hello信息包，组播方式224.0.0.5 （Exchange Hello packets, multicast mode 224.0.0.5）

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

交换Hello信息包，组播方式224.0.0.5 （Exchange Hello packets, multicast mode 224.0.0.5）
DR指定路由器，BDR备份指定路由器（The DR Specifies the router and the BDR backup specifies the router）
具有最高OSPF优先权的路由器为DR，次者为BDR（The router with the highest OSPF priority is DR And the second is BDR）
除非DR或BDR宕机，否则不会进行新的竞选（No new campaign will be run unless DR Or BDR is down）
P=1
P=0
P=1
DR &BDR的竞选The campaign for DR &BDR
P=3
P=2
DR
BDR

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

交换Hello信息包，组播方式224.0.0.5 （Exchange Hello packets, multicast mode 224.0.0.5）
DR指定路由器，BDR备份指定路由器（The DR Specifies the router and the BDR backup specifies the router）
具有最高OSPF优先权的路由器为DR，次者为BDR（The router with the highest OSPF priority is DR And the second is BDR）
除非DR或BDR宕机，否则不会进行新的竞选（No new campaign will be run unless DR Or BDR is down）
P=1
P=0
P=1
DR &BDR的竞选The campaign for DR &BDR
P=3
P=2
DR
BDR

</div>

---

### 📄 Slide 39：DR & BDR

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

通过Hello信息包，竞选DR&BDR
每个路由器只与DR&BDR形成邻接关系

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

DR & BDR
DR
BDR
通过Hello信息包，竞选DR&BDR
每个路由器只与DR&BDR形成邻接关系
Run for DR&BDR through Hello packetsEach router only forms an adjacency relationship with DR&BDR

</div>

---

### 📄 Slide 40：OSPF 术语（OSPF Terminology）

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

区域边界路由器
区域边界路由器
自治域边界路由器
区域内部路由器

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

OSPF 术语（OSPF Terminology）
ABR
ABR
ASBR
Area 1
Area 2
Backbone Area 0
Internal Router

</div>
# 第4章 构建园区网络 — OSPF路由协议

> 6 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 41：创建OSPF进程Create the OSPF process

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

创建一个OSPF路由进程
定义关联的IP地址范围

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

创建OSPF进程Create the OSPF process
创建一个OSPF路由进程
Create an OSPF routing process
Router(config)#router ospf  1
Defines the associated IP address range
Router(config-router)#network 192.168.0.0 0.0.255.255  area 0

</div>
**💻 配置命令：**

```cisco
Router(config)#router ospf  1
Defines the associated IP address range
Router(config-router)#network 192.168.0.0 0.0.255.255  area 0
```


---

### 📄 Slide 42：172.16.2.2

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

172.16.2.2
S0
172.16.2.1
A
B
S0
192.168.10.1
202.99.8.1
F0
F0
192.168.10.5
202.99.8.3

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

172.16.2.2
S0
172.16.2.1
A
B
S0
192.168.10.1
202.99.8.1
F0
F0
192.168.10.5
202.99.8.3

</div>

---

### 📄 Slide 43：组建园区网，实现园区网互通

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

组建园区网，实现园区网互通
（项目实施）

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Set up the park network to realize the interconnection of the park network
project implementation

</div>

---

### 📄 Slide 44：任务一：使用静态路由实现园区网互通Task 1: Use static routing to achieve campus network interoper...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【任务描述】
王先生的孩子就读的学校，是一所职业技术学院。随着国家对于职业教育的扶持，学校的招生规模日益扩大。学校原有的空间已经无法容纳更多的人员，学校决定扩展校区范围。经过友好协商，学校把附近一墙之隔职业中专学校合并到学院中。
为实现统一管理，共享信息资源，网络中心决定把二个校区网络连接为一个整体。由于新并入学校建有自己独立网络，使用和学院不同的子网规划地址。网络中心希望在不改变并入中专学校网络现状情况下，通过静态路由实现两个校园网络连通。
【知识准备】：静态路由
【网络拓扑】
【任务目标】：
掌握静态路由技术。
【设备清单】：路由器（2台） 、
计算机（>=2台）、双绞线（若干根）。
【工作过程】

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务一：使用静态路由实现园区网互通Task 1: Use static routing to achieve campus network interoperability

</div>

---

### 📄 Slide 45：任务二：使用动态路由实现园区网互通Task two: Implement campus network interworking using dynamic ...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【任务描述】
王先生的孩子就读的学校，是一所职业技术学院。随着国家对于职业教育的扶持，学校的招生规模日益扩大。学校原有的空间已经无法容纳更多的人员，学校决定扩展校区范围。经过友好协商，学校把附近一墙之隔职业中专学校合并到学院中。
为实现统一管理，共享信息资源，网络中心决定把二个校区网络连接为一个整体。由于新并入学校建有自己独立网络，使用和学院不同的子网规划地址。网络中心希望在不改变并入中专学校网络现状情况下，通过动态路由实现两个校园网络连通。
【知识准备】：动态路由
【网络拓扑】
【任务目标】：
掌握动态路由技术。
【设备清单】：路由器（2台） 、
计算机（>=2台）、双绞线（若干根）。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务二：使用动态路由实现园区网互通Task two: Implement campus network interworking using dynamic routing

</div>

---

### 📄 Slide 46：项目三：实现园区网络与外网互连Project 3: Realize the interconnection between the campus networ...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【任务描述】
王先生的孩子就读的学校，是一所职业技术学院。随着国家对于职业教育的扶持，学校的招生规模日益扩大。学校原有的空间已经无法容纳更多的人员，学校决定扩展校区范围。经过友好协商，学校把附近一墙之隔的一所职业中专学校合并到学院中。
为实现统一管理，共享信息资源，网络中心决定把二个校区网络连接为一个整体。由于新并入学校建有自己独立网络，使用和学院不同的子网规划地址。为了实现校园整体信息化建设的需要，需要把两个分散的校园网连接为一体，并与外网连接，使用RIP动态路由技术可以实现子网之间、子网与外网之间的互联互通。
【知识准备】： RIPV2动态路由技术
【任务目标】：掌握RIPV2动态路由技术。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目三：实现园区网络与外网互连Project 3: Realize the interconnection between the campus network and the external network
【知识准备】： RIPV2动态路由技术

</div>
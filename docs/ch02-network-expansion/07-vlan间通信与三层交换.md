# 第2章 扩展办公网络 — VLAN间通信与三层交换

> 4 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 33：实现办公网互联互通：Realize the interconnection of office network

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

实现办公网互联互通：Realize the interconnection of office network
（项目实施）：Project implementation

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

实现办公网互联互通：Realize the interconnection of office network
（项目实施）：Project implementation

</div>

---

### 📄 Slide 34：任务：实现不同的VLAN之间通信Task: Implement communication between different VLans

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

学校的办公大楼中有多个不同部门办公，为避免广播干扰，划分有多个不同的VLAN,实现部门之间的安全隔离；
但为了实现资源的共享，学校希望通过技术能实现不同VLAN之间，在实现广播隔离基础上，又能实现安全通讯。
【任务目标】：Task object

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务：实现不同的VLAN之间通信Task: Implement communication between different VLans
【任务描述】Task description
There are many different departments working in the office building of the school. In order to avoid broadcast interference, there are many different VLAN to achieve security isolation between departments.
However, in order to realize the sharing of resources, the school hopes to realize safe communication between different VLans through technology, on the basis of achieving broadcast isolation.
【网络拓扑】 Network topology
【任务目标】：Task object
使用交换机组建办公网。Use switches to set up office networks.

</div>

---

### 📄 Slide 35：任务：实现不同的VLAN之间通信Task: Implement communication between different VLans

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

任务：实现不同的VLAN之间通信Task: Implement communication between different VLans

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务：实现不同的VLAN之间通信Task: Implement communication between different VLans

</div>

---

### 📄 Slide 36：任务：实现不同的VLAN之间通信Task: Implement communication between different VLans

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【工作过程】Course of work
第一步：分别在三层上创建每个VLAN对应虚拟网关SVI端口，
第二步:三层上为虚拟网关VLAN分配IP地址：
第三步：将二层VLAN内连接主机网关，指定虚拟网关接口地址

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务：实现不同的VLAN之间通信Task: Implement communication between different VLans
【工作过程】Course of work
二层设备操作（同项目任务一）2F Device Operation (Same project task 1)
三层设备操作：Three-layer equipment operation:
Step 1: Create a virtual gateway SVI port for each VLAN on the three layers,
Switch(config)#vlan 10
Switch(config)#vlan 20
第二步:三层上为虚拟网关VLAN分配IP地址：
Step 2: Assign an IP address to the virtual gateway VLAN on Layer 3:
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown
Step 3: Connect the host gateway within the layer 2 VLAN and specify the virtual gateway interface address

</div>
**💻 配置命令：**

```cisco
Step 1: Create a virtual gateway SVI port for each VLAN on the three layers,
Switch(config)#vlan 10
Switch(config)#vlan 20
Step 2: Assign an IP address to the virtual gateway VLAN on Layer 3:
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown
Step 3: Connect the host gateway within the layer 2 VLAN and specify the virtual gateway interface address
```

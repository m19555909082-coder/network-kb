# 第1章 VLAN技术 — VLAN Trunk与802.1Q

> 5 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 18：任务：实现办公楼中成员组之间通信Task: To realize the communication between the member groups in...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

王先生所在公司的销售部人员众多，销售部的人员办公场地分别有楼上和楼下二个办公区，其中楼上为销售部独立的办公区，楼下是销售部和客户服务部在一起的混合办公区。
为避免楼下混合办公区中客户服务部和销售部二个部门计算机之间互相干扰，在交换机上配置，实现了混合办公区两个部门PC机隔离。但同时需要实现位于楼上和楼下整个销售部门所有计算机互相连通。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务：实现办公楼中成员组之间通信Task: To realize the communication between the member groups in the office building
【任务描述】  ：Task description
The sales department of Mr. Wang's company has a large number of personnel. The office space of the sales department has two office areas: upstairs and downstairs. The upstairs is the independent office area of the sales department, and the downstairs is the mixed office area of the sales department and the customer service department.
In order to avoid the mutual interference between the computers of customer service department and sales department in the mixed office area downstairs, it is configured on the switch to realize the isolation of the PCS of the two departments in the mixed office area. But at the same time, all the computers in the entire sales department, located upstairs and downstairs, need to be connected to each other.

</div>

---

### 📄 Slide 19：任务：实现办公楼中成员组之间通信Task: To realize the communication between the member groups in...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【网络拓扑】
【任务目标】：使用交换机组建办公网。
【设备清单】：交换机（1台）、 计算机（>=2台）、双绞线（若干根）。
【工作过程】

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务：实现办公楼中成员组之间通信Task: To realize the communication between the member groups in the office building
network topology
[Task goal] : Use the switch to set up the office network.
[Equipment list] : switch (1), computer (>=2), twisted pair (several).
Course of work

</div>

---

### 📄 Slide 20：Switch# configure terminal

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown
Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown
Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown

</div>
**💻 配置命令：**

```cisco
Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown
Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown
```


---

### 📄 Slide 21：项目任务3：Project Task 3

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

项目任务3：Project Task 3
实现跨交换机同一VLAN之间通讯：Realize the communication between the same VLAN across switches
（理论知识）(Theoretical knowledge)

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目任务3：Project Task 3
实现跨交换机同一VLAN之间通讯：Realize the communication between the same VLAN across switches
（理论知识）(Theoretical knowledge)

</div>

---

### 📄 Slide 22：与未划分VLAN时一样，从一个端口发出数据帧，直接广播转发到同一vlan内部相应成员端口。由于VLAN划分，通常按逻辑功能而非物理位置进行，在没有技术处理的情况...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

与未划分VLAN时一样，从一个端口发出数据帧，直接广播转发到同一vlan内部相应成员端口。由于VLAN划分，通常按逻辑功能而非物理位置进行，在没有技术处理的情况下，一台交换机上VLAN中信号无法跨越交换机，传递到另一台交换机同一个VLAN成员中。
跨交换机虚拟局域网技术

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Same as when the VLAN is not divided, the data frame is issued from one port and directly broadcasted to the corresponding member port inside the same vlan. Because the VLAN division, usually according to the logical function rather than physical location, in the absence of technical processing, a switch in the VLAN signal can not cross the switch, passed to another switch in the same VLAN member.
Cross switch virtual LAN technology

</div>
**💻 配置命令：**

```cisco
Same as when the VLAN is not divided, the data frame is issued from one port and directly broadcasted to the corresponding member port inside the same vlan. Because the VLAN division, usually according to the logical function rather than physical location, in the absence of technical processing, a switch in the VLAN signal can not cross the switch, passed to another switch in the same VLAN member.
```

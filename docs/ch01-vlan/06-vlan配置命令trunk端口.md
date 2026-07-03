# 第1章 VLAN技术 — VLAN配置命令—Trunk端口

> 5 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 23：Switch B

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

跨交换机VLAN间通信
A交换机上VLAN10的端口范围中取一个端口，和交换机B上VLAN10范围中的某个端口，作级联连接。
如果交换机上划了10个VLAN，就需要分别连10条线作级联，端口效率就太低了。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch B
VLAN30
VLAN20
VLAN10
跨交换机VLAN间通信
Cross-switch inter-VLAN communication
Take A port from the port range of VLAN10 on switch A and a port from the port range of VLAN10 on switch B for cascading connection.
If you have 10 VLans on the switch, you need to concatenate 10 lines, and the port efficiency is too low.

</div>

---

### 📄 Slide 24：Switch B

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在交换机之间用一条级联线，并将对应的端口设置为Trunk，这条线路就可以承载交换机上所有VLAN的信息。
Trunk端口传输多个VLAN的信息，实现同一VLAN跨越不同的交换机
跨交换机VLAN之间的通信:Tag VLAN

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch B
VLAN30
VLAN20
VLAN10
Tag VLAN
With a cascaded line between the switches and the corresponding port set to Trunk, this line can carry all the VLans on the switch.
Trunk端口传输多个VLAN的信息，实现同一VLAN跨越不同的交换机
The Trunk port transfers the information of multiple VLans to realize the same VLAN across different switches
跨交换机VLAN之间的通信:Tag VLAN
Communication between cross-switch VLans :Tag VLan

</div>

---

### 📄 Slide 25：目的,源MAC地址

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

目的,源MAC地址
类型,数据
重新计算帧检测序列
2字节标记协议标识
Trunk端口技术处理：IEEE802.1Q数据帧
标记协议标识（TPID）:固定值0x8100,表示该帧载有802.1q标记信息
类型,数据
重新计算帧检测序列

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

目的,源MAC地址
Destination,
source MAC address
Type, data
The frame detection sequence is recalculated
2-byte marking
protocol identification2字节标记控制信息
2 bytes mark control information
Trunk端口技术处理：IEEE802.1Q数据帧
Trunk port technology processing: IEEE802.1Q data frames
标记协议标识（TPID）:固定值0x8100,表示该帧载有802.1q标记信息
Marking Protocol Identifier (TPID) : A fixed value of 0x8100 indicates that the frame contains 802.1q marking information
标记控制信息（TCI）:Tag control Information (TCI) :
Priority 3 bits：表示优先级  This indicates the priority
Canonical format indicator 1bit：区别以太网(Differential Ethernet)、FDDI
VlanID  12 bits：表示VID，范围1－4094.(Denotes VID, range 1-4094)
目的MAC地址,源MAC地址Destination
MAC address, source MAC address
Type, data
The frame detection sequence is recalculated
IEEE802.3  frame
IEEE802.1Q frame

</div>

---

### 📄 Slide 26：Switch #configure terminal

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

……

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch #configure terminal
Switch (config)# interface fastEthernet 0/1  ！进入F0/1接口配置模式(Enter F0/1 interface configuration mode)
Switch (config-if)# switchport mode trunk
！将F0/1设置为Trunk模式(Set F0/1 to Trunk mode)
Switch(config-if)#end
Switch# show vlan     ! 查看VLAN配置信息(View VLAN configuration information)

</div>
**💻 配置命令：**

```cisco
Switch (config)# interface fastEthernet 0/1  ！进入F0/1接口配置模式(Enter F0/1 interface configuration mode)
Switch (config-if)# switchport mode trunk
Switch(config-if)#end
Switch# show vlan     ! 查看VLAN配置信息(View VLAN configuration information)
```


---

### 📄 Slide 27：802.1Q帧只在交换机的trunk链路上传输，对用户透明的。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

802.1Q帧只在交换机的trunk链路上传输，对用户透明的。
默认Trunk端口，转发交换机上所有VLAN的数据。
交换机1
交换机2
802.1Q工作过程
数据帧
Tag标签

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

802.1Q帧只在交换机的trunk链路上传输，对用户透明的。
802.1Q frames are transmitted only on the trunk link of the switch and are transparent to the user.
默认Trunk端口，转发交换机上所有VLAN的数据。
The default Trunk port forwards data from all VLans on the switch.
A
802.1Q工作过程
802.1Q working process
B
data frame
Tag标签

</div>
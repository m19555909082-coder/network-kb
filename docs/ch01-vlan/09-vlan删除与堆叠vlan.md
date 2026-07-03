# 第1章 VLAN技术 — VLAN删除与堆叠VLAN

> 4 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 37：配置SVI示例Configuring the SVI example

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置SVI示例Configuring the SVI example
Switch#configure terminal
Switch(config)#vlan 10
Switch(config-vlan)exit
Switch(config)#vlan 20
Switch(config-vlan)#exit
Switch(config)#interface vlan 10
Switch(config-if)#ip address 192.168.10.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#interface vlan 20
Switch(config-if)#ip address 192.168.20.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#ip routing  (对于思科要启用路由功能) (Enable routing for Cisco)

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

配置SVI示例Configuring the SVI example
Switch#configure terminal
Switch(config)#vlan 10
Switch(config-vlan)exit
Switch(config)#vlan 20
Switch(config-vlan)#exit
Switch(config)#interface vlan 10
Switch(config-if)#ip address 192.168.10.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#interface vlan 20
Switch(config-if)#ip address 192.168.20.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#ip routing  (对于思科要启用路由功能) (Enable routing for Cisco)

</div>
**💻 配置命令：**

```cisco
Switch#configure terminal
Switch(config)#vlan 10
Switch(config-vlan)exit
Switch(config)#vlan 20
Switch(config-vlan)#exit
Switch(config)#interface vlan 10
Switch(config-if)#ip address 192.168.10.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#interface vlan 20
Switch(config-if)#ip address 192.168.20.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#ip routing  (对于思科要启用路由功能) (Enable routing for Cisco)
```


---

### 📄 Slide 38：任务2：实现不同的VLAN之间通信Task2: Implement communication between different VLans

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

学校的办公大楼中有多个不同部门办公，为避免广播干扰，划分有多个不同的VLAN,实现部门之间的安全隔离；
但为了实现资源的共享，学校希望通过技术能实现不同VLAN之间，在实现广播隔离基础上，又能实现安全通讯。
【网络拓扑】上课口述案例二实现需要怎样配置？

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务2：实现不同的VLAN之间通信Task2: Implement communication between different VLans
【任务描述】Task Description
There are many different departments working in the office building of the school. In order to avoid broadcast interference, there are many different VLAN to achieve security isolation between departments.
However, in order to realize the sharing of resources, the school hopes to realize safe communication between different VLans through technology, on the basis of achieving broadcast isolation.
[Network topology] How to configure the implementation of Case 2 in class?

</div>

---

### 📄 Slide 39：任务2：实现不同的VLAN之间通信Task2: Implement communication between different VLans

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

任务2：实现不同的VLAN之间通信Task2: Implement communication between different VLans

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

任务2：实现不同的VLAN之间通信Task2: Implement communication between different VLans

</div>

---

### 📄 Slide 40：谢 谢!

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

谢 谢!

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

谢 谢!
THANKS!

</div>
# 第1章 VLAN技术 — VLAN特点与划分方式

> 5 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 13：虚拟局域网特点

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

虚拟局域网特点
控制网络的广播风暴
确保网络安全
简化网络管理，提高组网灵活性

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Virtual LAN features
Control the broadcast storm of the network
Ensure network security
Simplify network management and improve network flexibility

</div>

---

### 📄 Slide 14：在局域网中划分虚拟局域网的方法很多，但基于端口的VLAN划分技术，是划分虚拟局域网最简单也是最有效的方法。这种划分VLAN的方法是根据以太网交换机的端口来划分。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在局域网中划分虚拟局域网的方法很多，但基于端口的VLAN划分技术，是划分虚拟局域网最简单也是最有效的方法。这种划分VLAN的方法是根据以太网交换机的端口来划分。
！把VLAN 10命名为test
配置虚拟局域网

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

There are many ways to divide the virtual LAN in the local area network, but the VLAN partition technology based on port is the simplest and most effective way to divide the virtual LAN. This method of dividing the VLAN is based on the port of the Ethernet switch.
Switch#configure terminal
Switch(config)#vlan 10
！启用VLAN 10（ Enable VLAN 10）
Switch(config-vlan)#name test
！把VLAN 10命名为test
（Name VLAN 10 test）
Switch(config-vlan)#
Configure a virtual LAN

</div>
**💻 配置命令：**

```cisco
There are many ways to divide the virtual LAN in the local area network, but the VLAN partition technology based on port is the simplest and most effective way to divide the virtual LAN. This method of dividing the VLAN is based on the port of the Ethernet switch.
Switch#configure terminal
Switch(config)#vlan 10
！启用VLAN 10（ Enable VLAN 10）
Switch(config-vlan)#name test
！把VLAN 10命名为test
（Name VLAN 10 test）
Switch(config-vlan)#
```


---

### 📄 Slide 15：指定端口到划分好VLAN中，如将交换机F0/5端口指定到VLAN 10配置

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

指定端口到划分好VLAN中，如将交换机F0/5端口指定到VLAN 10配置

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

指定端口到划分好VLAN中，如将交换机F0/5端口指定到VLAN 10配置
Specify the port to the divided VLAN, such as switch F0/5 port to VLAN 10 configuration
Switch(config)# interface fastEthernet 0/5     ！打开交换机的接口5    Open interface 5 of the switch
Switch(config-if)# switchport access vlan 10   ！把该接口分配到VLAN 10中  Assign the interface to VLAN 10
Switch(config-if)#no shutdown
Switch# show vlan  ! 查看VLAN配置信息
View VLAN configuration information

</div>
**💻 配置命令：**

```cisco
指定端口到划分好VLAN中，如将交换机F0/5端口指定到VLAN 10配置
Specify the port to the divided VLAN, such as switch F0/5 port to VLAN 10 configuration
Switch(config)# interface fastEthernet 0/5     ！打开交换机的接口5    Open interface 5 of the switch
Switch(config-if)# switchport access vlan 10   ！把该接口分配到VLAN 10中  Assign the interface to VLAN 10
Switch(config-if)#no shutdown
Switch# show vlan  ! 查看VLAN配置信息
View VLAN configuration information
```


---

### 📄 Slide 16：Port-vlan原理

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

Port-vlan原理
Principle of Port-vlan
F0/1
F0/2
F0/3
A
B
C
Vlan 10
Vlan 20
Vlan 10

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Port-vlan原理
Principle of Port-vlan
F0/1
F0/2
F0/3
A
B
C
Vlan 10
Vlan 20
Vlan 10

</div>
**💻 配置命令：**

```cisco
Vlan 10
Vlan 20
Vlan 10
```


---

### 📄 Slide 17：项目任务2：Project Task 2

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

项目任务2：Project Task 2
实现跨交换机同一VLAN之间通讯：Realize the communication between the same VLAN across switches
（项目实施）(Project implementation)

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目任务2：Project Task 2
实现跨交换机同一VLAN之间通讯：Realize the communication between the same VLAN across switches
（项目实施）(Project implementation)

</div>
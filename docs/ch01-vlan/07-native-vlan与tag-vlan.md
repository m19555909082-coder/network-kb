# 第1章 VLAN技术 — Native VLAN与Tag VLAN

> 4 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 28：配置VLAN-Trunk技术Configure the VLAN-Trunk technology

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置VLAN-Trunk技术Configure the VLAN-Trunk technology
把Fa 0/1配成Trunk口
Match Fa 0/1 to the Trunk mouth
Switch# configure terminal
Switch(config)# interface fastethernet0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)#no shutdown

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

配置VLAN-Trunk技术Configure the VLAN-Trunk technology
把Fa 0/1配成Trunk口
Match Fa 0/1 to the Trunk mouth
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
```


---

### 📄 Slide 29：VLAN相关配置

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

VLAN相关配置
当交换机与交换机相联系时，常将交换机之间连接的链路设置为TRUNK链路，用来确保连接不同交换机之间的链路可以传递多个VLAN的信息。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

VLAN相关配置
VLAN related configuration
f0/1
f0/1
switch1
switch2
Switch1#config
Switch1(config) #interface fastethernet 0/1
Switch(config-if)#switchport mode trunk (将二层接口的属性设置为trunk) (Set the layer 2 property to trunk)
Switch2#config
Switch2(config) #interface fastethernet 0/1
Switch(config-if)#switchport mode trunk
When the switch is connected with the switch, the link between the switch is often set as the TRUNK link, which is used to ensure that the link between different switches can transfer the information of multiple VLans.

</div>
**💻 配置命令：**

```cisco
VLAN related configuration
Switch1(config) #interface fastethernet 0/1
Switch(config-if)#switchport mode trunk (将二层接口的属性设置为trunk) (Set the layer 2 property to trunk)
Switch2(config) #interface fastethernet 0/1
Switch(config-if)#switchport mode trunk
```


---

### 📄 Slide 30：本帧VLAN：Native VLAN

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

每个Trunk口，都属于一个native VLAN ；
在配置Trunk链路时，确保Trunk口链路两端属于相同的native VLAN；

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

本帧VLAN：Native VLAN
Switch(config)# interface fastethernet0/1
Switch(config)# switchport  mode  trunk
Switch(config-if)# switchport  trunk native vlan 20
Switch(config-if)# no shutdown
Switch(config-if)# end
每个Trunk口，都属于一个native VLAN ；
Each Trunk port belongs to a native VLAN.
每个Trunk口，缺省native VLAN是VLAN 1；
For each Trunk port, the default native VLAN is VLAN 1;
在配置Trunk链路时，确保Trunk口链路两端属于相同的native VLAN；
When configuring the Trunk link, ensure that both ends of the Trunk port link belong to the same native VLAN
Native VLAN:本帧vlan。不需要打4个字节的标签就可以直接传输，但其它的必须要带TAG过trunk端口。(You don't need to TAG four bytes to transfer them directly, but everything else must be tagged through your trunk port.)

</div>
**💻 配置命令：**

```cisco
Switch(config)# interface fastethernet0/1
Switch(config)# switchport  mode  trunk
Switch(config-if)# switchport  trunk native vlan 20
Switch(config-if)# no shutdown
Switch(config-if)# end
每个Trunk口，都属于一个native VLAN ；
每个Trunk口，缺省native VLAN是VLAN 1；
For each Trunk port, the default native VLAN is VLAN 1;
```


---

### 📄 Slide 31：Switch B

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

VLAN10为本帧VLAN，VLAN10中数据过trunk口不带TAG直接传输，
VLAN20 、 VLAN30 数据跨Trunk端口传输需要到TAG标识

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch B
VLAN30
VLAN20
VLAN10
Tag VLAN
VLAN10为本帧VLAN，VLAN10中数据过trunk口不带TAG直接传输，
VLAN10 is the VLAN of this frame. Data in VLAN10 is directly transmitted through the trunk port without TAG.
VLAN20 、 VLAN30 数据跨Trunk端口传输需要到TAG标识
VLAN20, VLAN30 data transmission across the Trunk port needs to TAG identification
本帧：Native VLAN传输(transmission）
设为Native VLAN （Set to Native VLAN）
设为Native VLAN（Set to Native VLAN)
Native VLAN

</div>
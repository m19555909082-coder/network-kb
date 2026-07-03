# 第1章 VLAN技术 — SVI三层交换与VLAN间通信

> 5 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 32：Switch# show vlan

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

下面是一个把端口0/15 配置为TRUNK端口，但是不包含VLAN 2的例子：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Switch# show vlan
VLAN Name         Status    Ports
---- ------------------ --------- ---------------
1        default       active      Fa0/1, Fa0/2, Fa0/3, Fa0/4
Fa0/6, Fa0/7, Fa0/8, Fa0/9
Fa0/10, Fa0/11, Fa0/12, Fa0/13
Fa0/18, Fa0/19, Fa0/20, Fa0/21
2      VLAN0002 active     Fa0/5, Gi0/2
4      VLAN0004 active     Fa0/14, Fa0/15, Fa0/16, Fa0/17
5      VLAN0005 active     Fa0/22, Fa0/23, Fa0/24, Gi0/1
下面是一个把端口0/15 配置为TRUNK端口，但是不包含VLAN 2的例子：
Here is an example of configuring port 0/15 as TRUNK port, but without VLAN 2:
Switch(config)# interface fastethernet0/15
Switch(config)#switchport  mode trunk
Switch(config-if)# switchport trunk allowed vlan remove 2
Switch(config-if)# end
Switch# show interfaces fastethernet0/15 switchport
Interface Switchport Mode Access Native Protected VLAN lists
--------- ---------- --------- --------- --------- --------- -----------
Fa0/15      Enabled   Trunk   1          1         Enabled     1,3-4094
配置(Configure)Tag VLAN-Trunk

</div>
**💻 配置命令：**

```cisco
Switch# show vlan
VLAN Name         Status    Ports
下面是一个把端口0/15 配置为TRUNK端口，但是不包含VLAN 2的例子：
Here is an example of configuring port 0/15 as TRUNK port, but without VLAN 2:
Switch(config)# interface fastethernet0/15
Switch(config)#switchport  mode trunk
Switch(config-if)# switchport trunk allowed vlan remove 2
Switch(config-if)# end
Switch# show interfaces fastethernet0/15 switchport
Interface Switchport Mode Access Native Protected VLAN lists
```


---

### 📄 Slide 33：在堆叠管理下如何配置VLAN：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在堆叠管理下如何配置VLAN：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

How to configure VLAN under stack management:
Switch(config)# interface fastethernet1/0/10
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 100
Switch(config-if)# exit
Switch(config)# interface fastethernet1/0/15
Switch(config-if)# switchport mode trunk
Switch(config-if)# end
Switch(config)#member 1
Switch@1(config)# interface fastethernet1/0/10
Switch@1(config-if)# switchport mode access
Switch@1(config-if)# switchport access vlan 100
Switch@1(config-if)# exit
配置堆叠管理下的VLANConfigure VLAN under stack management

</div>
**💻 配置命令：**

```cisco
How to configure VLAN under stack management:
Switch(config)# interface fastethernet1/0/10
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 100
Switch(config-if)# exit
Switch(config)# interface fastethernet1/0/15
Switch(config-if)# switchport mode trunk
Switch(config-if)# end
Switch(config)#member 1
Switch@1(config)# interface fastethernet1/0/10
Switch@1(config-if)# switchport mode access
Switch@1(config-if)# switchport access vlan 100
配置堆叠管理下的VLANConfigure VLAN under stack management
```


---

### 📄 Slide 34：删除VLAN(Deleting a VLAN)

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

删除VLAN,需要先删除VLAN下接口:

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

删除VLAN(Deleting a VLAN)
删除VLAN,需要先删除VLAN下接口:
To delete the VLAN, you need to delete the interface under the VLAN first:
Switch(config)# interface fastethernet0/10
Switch(config-if)# no switchport
Switch(config-if)# exit
再删除VLAN(Then delete the VLAN)
Switch(config)# no vlan 10

</div>
**💻 配置命令：**

```cisco
To delete the VLAN, you need to delete the interface under the VLAN first:
Switch(config)# interface fastethernet0/10
Switch(config-if)# no switchport
Switch(config-if)# exit
Switch(config)# no vlan 10
```


---

### 📄 Slide 35：项目任务4：Project Task 4

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

项目任务4：Project Task 4
实现不同VLAN之间通讯:Realize the communication between different VLans
（项目实施）:(Project implementation)

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目任务4：Project Task 4
实现不同VLAN之间通讯:Realize the communication between different VLans
（项目实施）:(Project implementation)

</div>

---

### 📄 Slide 36：三层交换机上配置SVI接口地址

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

三层交换机上配置SVI接口地址
各VLAN中主机将三层交换机上相应VLAN的SVI接口地址作为本VLAN网关
数据到达三层交换机后利用路由功能转发到其他VLAN

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

The SVI interface address is configured on the layer 3 switch
各VLAN中主机将三层交换机上相应VLAN的SVI接口地址作为本VLAN网关
The host in each VLAN takes the SVI interface address of the corresponding VLAN on the layer 3 switch as the VLAN gateway
After arriving at the layer 3 switch, the data is forwarded to other VLans by using the routing function
任务1：实现不同的VLAN之间通信Task 1: Implement communication between different VLans

</div>
**💻 配置命令：**

```cisco
The SVI interface address is configured on the layer 3 switch
The host in each VLAN takes the SVI interface address of the corresponding VLAN on the layer 3 switch as the VLAN gateway
```

# 复习大纲 — 简答题答案

> **说明**：答案优先从PPT原文提取并整理；PPT中缺失的内容已通过补充知识完善。

---

## Q1：什么是动态路由？

**答案来源**：`4-构建园区网络双语...`

路由概念：略；路由发生在网络层,包含两个基本动作：确定最佳路径和通过网络转发数据。
网络中的数据包通过路由器转发到目的网络，必须依据于路由表，路由表中包含有目的网络地址以及到达这些网络的最佳路径，如某个接口或下一跳地址。正是由于路由表的存在，路由器可以依据它进行数据转发。
典型的路由表产生方式有三种：；直连路由；静态路由 Static routing；动态路由 Dynamic routing
园区网路由

---

## Q2：什么设备可以产生路由表？

**答案来源**：PPT原文 + 整理补充

- **路由器**是产生和维护路由表的主要设备
- 路由器保存着各种传输路径的地址信息表，俗称**路由表（Routing Table）**，供数据包路由时选择
- 路由表中保存着到达各子网的标志信息：路由标识、获得路由方式、目标网络、转发路由器地址和经过路由器的个数等内容
- 路由表中包含有该路由器知道的目的网络地址以及通过此路由器到达这些网络的最佳路径，如某个接口或下一跳的地址
- **三层交换机**开启路由功能（`ip routing`）后也可产生路由表
- 典型的路由表产生方式有三种：直连路由、静态路由、动态路由

---

## Q3：最早开发以太网的公司是哪个？

**答案来源**：PPT原文 + 补充知识

- 以太网最早由**施乐公司（Xerox）**在20世纪70年代开发
- 1980年，DEC、Intel、Xerox三家公司联合提出了以太网标准（DIX标准）
- 1983年，IEEE 802.3标准正式发布，成为以太网的国际标准

---

## Q4：本征帧的概念，一般本征帧在哪个VLAN，本征帧的协议标准是哪个？

**答案来源**：PPT原文 + 整理补充

- **本征帧（Native VLAN）**：在Trunk链路上，不需要打4字节802.1Q标签就可以直接传输的帧
- **默认Native VLAN**：每个Trunk口的缺省Native VLAN是**VLAN 1**
- **协议标准**：**IEEE 802.1Q**
- 配置命令：`Switch(config-if)# switchport trunk native vlan [VLAN号]`
- 注意事项：Trunk链路两端必须配置相同的Native VLAN

---

## Q5：配置静态路由的一般步骤是什么？

**答案来源**：`4-构建园区网络双语...`

静态路由配置命令；配置静态路由用命令ip route
router(config)#ip route [网络编号] [子网掩码] [转发路由器的IP地址/本地接口]
静态路由描述转发路径的方式有两种；指向本地接口（即从本地某接口发出）；指向下一跳路由器直连接口的

---

## Q6：什么是RIP协议，收敛时间是多少，跳数限制是多少？

**答案来源**：`4-构建园区网络双语...`

路由信息协议RIP；RIP（
RIP协议假定如果从网络的一个终端到另一个终端的路由跳数超过15个，那么一定牵涉到了循环，因此当一个路径达到16跳，将被认为是达不到的。

> **补充**：RIP收敛速度较慢（240秒以上），路由更新周期30秒，180秒未收到更新即标记不可达，240秒后删除路由。

---

## Q7：理解SVI、TAGVLAN、RIP、OSPF的含义

**答案来源**：PPT原文 + 整理补充

- **SVI（Switch Virtual Interface，交换机虚拟接口）**：为交换机中VLAN创建的虚拟三层接口，可配置IP地址作为该VLAN的网关，实现VLAN间路由
- **TAG VLAN（标签VLAN）**：基于IEEE 802.1Q标准，在以太网帧中插入4字节VLAN标签（Tag），包含12位VLAN ID（支持4096个VLAN）、3位优先级、1位格式指示符。Trunk端口传输多VLAN数据时给帧打标签
- **RIP（Routing Information Protocol，路由信息协议）**：距离矢量路由协议，以跳数作为度量值，最大15跳（16跳不可达），每隔30秒更新，适用于小型网络
- **OSPF（Open Shortest Path First，开放最短路径优先）**：链路状态路由协议，克服了RIP收敛慢（240秒以上）和15跳规模限制的弱点，采用区域概念（骨干区域Area 0），由RFC 2328定义

---

## Q8：记住所有的私有地址

**答案来源**：PPT原文 + 补充知识（RFC 1918）

私有IP地址范围（RFC 1918定义）：
- **A类**：10.0.0.0 ~ 10.255.255.255（10.0.0.0/8）
- **B类**：172.16.0.0 ~ 172.31.255.255（172.16.0.0/12）
- **C类**：192.168.0.0 ~ 192.168.255.255（192.168.0.0/16）

这些地址只能在局域网内部使用，不能直接在Internet上路由。

---

## Q9：交换机和路由器的各种操作模式及提示符号

**答案来源**：`3-使用子网技术，实现网络连通双语...`

路由器配置命令模式；一般说前四种就可以：；用户模式 user mode Router>
特权模式 privileged mode Router #；全局模式 global mode Router(config)#
端口模式 interface mode Router(config-if)#；线程配置模式
Router(config-line)#；路由协议配置模式；Router(config-router)#

---

## Q10：综合理解RIP和OSPF

**答案来源**：PPT原文 + 整理补充

**RIP（路由信息协议）**：
- 距离矢量路由协议，Xerox在70年代开发
- 以跳数为度量，最大15跳，16跳不可达
- 每30秒发送更新报文，180秒未收到→标记不可达，240秒→删除路由
- 适用于小型同类网络，配置简单但收敛慢

**OSPF（开放最短路径优先）**：
- 链路状态路由协议，克服了RIP收敛慢和规模限制
- 采用分区域概念：骨干区域Area 0 + 非骨干区域
- 基于SPF算法计算最短路径，收敛速度快
- RFC 2328定义，适用于中大型网络

---

## Q11：RIP v1和RIP v2的区别

**答案来源**：`4-构建园区网络双语...`

RIP路由协议的版本；有类路由协议，不支持VLSM；以广播的形式发送更新报文；不支持认证
无类路由协议，支持VLSM；以组播的形式发送更新报文；支持明文和MD5的认证

---

## Q12：RIP路由信息的更新过程

**答案来源**：`4-构建园区网络双语...`

RIP路由信息的更新
2、如果路由器经过180秒没有收到来自某一路由器的路由更新报文，则将所有来自此路由器的路由信息标志为不可达。
3、若在其后240秒内仍未收到更新报文，就将这些路由从路由表中删除

> **补充**：第1步 — RIP协议每隔30秒定期向外发送一次更新报文。

---

## Q13：不同VLAN之间通过什么技术通信？三层交换机/路由器的工作模式有几种？

**答案来源**：`2-扩展办公网络，提供网络带宽双语...`

路由器实现；利用路由器的路由功能，实现不同子接口数据的转发；缺点是：部署不灵活，形成网络瓶颈。
在路由器上为每个VLAN划分一个子接口；每个子接口配置

---

## Q14：内部连通性测试命令有哪些，怎么用？

**答案来源**：PPT原文 + 补充知识

常用连通性测试命令：
- **ping**：使用ICMP协议发送回显请求，测试网络连通性和延迟
  - 用法：`ping 目标IP地址`（Windows默认4次，Cisco持续发送）
- **tracert/traceroute**：追踪数据包从源到目的地经过的路径（每一跳）
  - Windows：`tracert 目标IP地址`
  - Cisco路由器：`traceroute 目标IP地址`

说明：ping命令使用的是ICMP协议，除网络探查外还用于传输错误信息，路由器上不应禁止该协议。

---

## Q15：掌握静态路由，什么是默认路由，默认路由是特殊的静态路由

**答案来源**：`4-构建园区网络双语...`

缺省路由 Ult routing；缺省路由一般使用在
stub网络是只有1条出口路径的网络。使用默认路由来发送那些目标网络没有包含在路由表中的数据包。
缺省路由可以看作是静态路由的一种特殊情况。；配置缺省路由用如下命令：
router(config)#ip route 0.0.0.0 0.0.0.0 [转发路由器的IP地址/本地接口]

---

## Q16：启用RIP和OSPF的命令

**答案来源**：`4-构建园区网络双语...`

1、开启；Router(config)#router rip；2、申请本路由器参与
Router(config-router)#network 192.168.1.0
3、指定；Router(config-router)#version  2；Router(config-router)#no auto-summary

> **补充（OSPF命令）**：Router(config)#router ospf 1 → Router(config-router)#network 网段 反掩码 area 区域号

---

## Q17：掌握直连路由概念，会写直连路由，知道默认网关

**答案来源**：`4-构建园区网络双语...`

园区网直连路由；直连路由 directly connected routing；直连路由是在配置完路由器网络接口的
一般把在路由器接口所连接的子网，直接配置地址的路由方式称为直连路由，直连路由基本功能就是实现邻居的互通。

---

## Q18：掌握跨交换机VLAN通信配置方法，直连路由和静态路由实验

**答案来源**：`1-优化办公网络，降低网络干扰双语...`

在交换机之间用一条级联线，并将对应的端口设置为；Trunk端口传输多个；跨交换机

---

## Q19：每个实验的命令配置过程必须会写

**答案来源**：`1-优化办公网络，降低网络干扰双语...`

将一组接口加入某一个VLAN
Switch(config)#interface range fastethernet 0/1-10，0/15，0/20
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#no shutdown；注：连续接口 0/1-10，中间使用空格分离;
不连续多个接口，中间用逗号隔开；；如果使用模块，一定要写明模块编号。

---

## Q20：配置TAGVLAN时对端口的要求

**答案来源**：`1-优化办公网络，降低网络干扰双语...`

Switch# show vlan；下面是一个把端口0/15 配置为
Switch(config)# interface fastethernet0/15
Switch(config)#switchport  mode trunk
Switch(config-if)# switchport trunk allowed vlan remove 2
Switch(config-if)# end
Switch# show interfaces fastethernet0/15 switchport
配置(Configure)Tag VLAN-Trunk

---

## Q21：路由器端口地址的配置原则是什么？

**答案来源**：`3-使用子网技术，实现网络连通双语...`

配置接口
Red-Giant(config-if)#ip address 192.168.1.1                       255.255.255.0
Red-Giant(config-if)#no shutdown；将接口关闭；路由器接口配置命令

---

## Q22：创建VLAN、分配端口到VLAN、配置端口IP地址、启用RIP和OSPF路由

**答案来源**：`2-扩展办公网络，提供网络带宽双语...`

二层设备操作（同项目任务一）2F Device Operation (Same project task 1)
三层设备操作：；第一步：分别在三层上创建每个；Switch(config)#vlan 10
Switch(config)#vlan 20；第二步:三层上为虚拟网关VLAN分配IP地址：
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown；Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown；第三步：将二层

---

## Q23：NAT的端口应用原理

**答案来源**：PPT原文 + 整理补充

**PAT（Port Address Translation，端口地址转换/端口复用）**：
- PAT是复用NAT池的特例，通过**端口复用技术**用一个合法IP地址映射内网所有私有IP地址
- 这个合法地址往往就是路由器出口的IP地址（如S0/0口IP）
- 工作原理：将内网多个私有IP地址和端口号映射到同一个公网IP地址的不同端口号上
- 理论上一个IP地址可映射约**65000个会话**，实际路由器通常支持约**4000个**（Cisco）

**PAT配置方法一**（建立NAT池，起始=结束）：
```
R1(config)# ip nat pool 池名 起始地址 结束地址 netmask 子网掩码
R1(config)# access-list 表号 permit 内部地址条件
R1(config)# ip nat inside source list 表号 pool 池名 overload
```

**PAT配置方法二**（不建立NAT池，直接使用出口接口）：
```
R1(config)# access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)# ip nat inside source list 30 interface s0/0 overload
```

- 优点：最大限度节省IP地址
- 缺点：只能同时支持几千个会话，易造成拥塞；缓解方法：多申请IP地址建大NAT池、限制占用会话数多的应用（如BT）

---

## Q24：NAT边界路由配置应注意什么？

**答案来源**：`6网络地址转换NAT讲课...`

局域网和；NAT路由器一般配置通往外网的默认路由。；ISP的路由器通过配置静态路由为局域网分配IP地址段。

---

## Q25：网络系统集成的特点是什么？

**答案来源**：`网络工程设计CH1...`

网络系统集成的特点；接口规范；关注系统整体性能；重视工程规范和质量管理；建立良好的用户关系
解放军理工大学计算机系；陈鸣：网络工程设计

---

## Q26：IP地址/子网地址/园区网的层次结构

**答案来源**：`2-扩展办公网络，提供网络带宽双语...`

在组建大中型以太网络之前，需要连接很多的交换机、路由器等网络互联设备。大中型以太网络在规划和设计中，普遍采用三层结构模型，以明确每一台设备在以太网中所承担的基本功能，以太网络在规划和设计中三层结构模型，按照网络的功能，将网络首先从逻辑结构上，划分为三个层次，即核心层、汇聚层和接入层。
层次化网络规划设计

---

## Q27：私有地址/广播地址

**答案来源**：PPT原文 + 补充知识

**私有地址**（RFC 1918定义，只能在局域网内部使用，不能直接在Internet上路由）：
- **A类**：10.0.0.0 ~ 10.255.255.255（10.0.0.0/8）
- **B类**：172.16.0.0 ~ 172.31.255.255（172.16.0.0/12）
- **C类**：192.168.0.0 ~ 192.168.255.255（192.168.0.0/16）

**广播地址**：
- **子网广播地址（直接广播）**：子网中主机位全为1的地址，用于向该子网内所有主机发送数据。如192.168.1.0/24的广播地址为192.168.1.255
- **有限广播地址**：255.255.255.255，用于本地网络广播，路由器默认不会转发（隔离广播域）
- **广播域**：网络中能接收同一广播帧的所有节点的集合。VLAN技术可分割广播域，控制广播风暴
- NAT边界路由器需处理私有地址与公网地址的转换，私有地址在公网上不可路由

---

## Q28：路由器和交换机的模式符号，路由表缩写C S R O的含义

**答案来源**：`4-构建园区网络双语...`

【配置直连路由】；Red-Giant#configure terminal ! 进入全局配置模式
Red-Giant(config)#
Red-Giant(config)#interface fastethernet 1/0 ! 进入路由器F1/0接口模式
Red-Giant(config-if) #ip address 192.168.1.1 255.255.255.0 ! 配置接口地址
Red-Giant(config-if) #no shutdown
Red-Giant(config)#interface fastethernet 1/1 ! 进入路由器F1/1接口模式
Red-Giant(config-if) #ip address 192.168.3.1 255.255.255.0 ! 配置接口地址
Red-Giant(config-if) #no shutdown
Red-Giant(config)#interface Serial 1/2 ! 进入路由器
Red-Giant(config-if) #ip address 192.168.2.1 255.255.255.0
Red-Giant(config-if) #no shutdown；Router# show ip route ！ 查看路由器设备的路由表信息

> **补充**：路由表中 C=直连路由(Connected)、S=静态路由(Static)、R=RIP、O=OSPF。

---

## Q29：三层交换机默认工作在第几层？

**答案来源**：PPT原文 + 补充知识

- 三层交换机**默认工作在第二层（数据链路层）**
- 三层交换机本质是"二层交换机 + 路由模块"，数据转发优先使用硬件交换（二层）
- 只有开启路由功能（`ip routing`）后，才能进行三层路由转发
- 三层交换机用于核心层/汇聚层，连接所有区域的核心设备

---

## Q30：三层交换机上创建VLAN40/VLAN80，配置地址

**答案来源**：`2-扩展办公网络，提供网络带宽双语...`

二层设备操作（同项目任务一）2F Device Operation (Same project task 1)
三层设备操作：；第一步：分别在三层上创建每个；Switch(config)#vlan 10
Switch(config)#vlan 20；第二步:三层上为虚拟网关VLAN分配IP地址：
Switch(config)# interface vlan 10
Switch(config-if)# ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown；Switch(config)# interface vlan 20
Switch(config-if)# ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown；第三步：将二层

---

## Q31：直连路由及默认路由

**答案来源**：`4-构建园区网络双语...`

缺省路由 Ult routing；缺省路由一般使用在
stub网络是只有1条出口路径的网络。使用默认路由来发送那些目标网络没有包含在路由表中的数据包。
缺省路由可以看作是静态路由的一种特殊情况。；配置缺省路由用如下命令：
router(config)#ip route 0.0.0.0 0.0.0.0 [转发路由器的IP地址/本地接口]

---

## Q32：两台交换机VLAN互通配置

**答案来源**：`1-优化办公网络，降低网络干扰双语...`

在堆叠管理下如何配置VLAN：
Switch(config)# interface fastethernet1/0/10
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 100
Switch(config-if)# exit
Switch(config)# interface fastethernet1/0/15
Switch(config-if)# switchport mode trunk
Switch(config-if)# end；Switch(config)#member 1
配置堆叠管理下的

---

## Q33：配置静态路由连通网络

**答案来源**：`4-构建园区网络双语...`

静态路由配置命令；配置静态路由用命令ip route
router(config)#ip route [网络编号] [子网掩码] [转发路由器的IP地址/本地接口]
静态路由描述转发路径的方式有两种；指向本地接口（即从本地某接口发出）；指向下一跳路由器直连接口的

---

## Q34：综合实验（实验15）

**答案来源**：PPT原文 + 整理补充

综合实验（实验15）目标是**组建园区网，实现园区网互通**，涵盖网络工程全流程。

**实验场景**：学校合并两个校区，需要在两个不同子网规划的校园网之间实现互联互通，并与外网连接。

**实验内容与步骤**：

1. **使用静态路由实现园区网互通**：
   - 配置路由器各接口IP地址
   - 为每个非直连网段添加静态路由（`ip route 目标网络 子网掩码 下一跳`）
   - 验证两个校区网络连通性

2. **使用动态路由（RIP）实现园区网互通**：
   - 配置RIP协议：`router rip` → `network 网段` → `version 2` → `no auto-summary`
   - 实现自动路由学习和更新

3. **实现园区网络与外网互连**：
   - 配置NAT边界路由器
   - 使用RIPv2动态路由实现子网之间、子网与外网之间的互联互通
   - 配置默认路由指向外网

**涉及的全部技术**：VLAN划分与Trunk配置、SVI接口地址配置、直连路由与静态路由、默认路由、RIP动态路由协议、RIPv1与RIPv2、NAT/PAT地址转换、ACL访问控制列表

---


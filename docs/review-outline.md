# 复习大纲 — 简答题答案 / Review Outline — Short Answer Questions

> **说明**：答案基于PPT原文、课堂图片及实验报告整理。每题提供中英双语对照。
> **Note**：Answers compiled from PPT slides, lecture images, and lab reports. Bilingual (Chinese/English) for each question.

---

## Q1：什么是动态路由？ / What is Dynamic Routing?

**答案 / Answer**：

路由发生在网络层（OSI第三层），包含两个基本动作：**确定最佳路径**和**通过网络转发数据**。网络中的数据包通过路由器转发到目的网络，必须依据路由表。路由表中包含目的网络地址以及到达这些网络的最佳路径（如某个接口或下一跳地址）。正是由于路由表的存在，路由器可以依据它进行数据转发。

典型的路由表产生方式有三种：**直连路由**（Directly Connected Routing）、**静态路由**（Static Routing）、**动态路由**（Dynamic Routing）。

**动态路由**是路由器通过路由协议（如RIP、OSPF）自动学习、更新和维护路由表的方式。路由器之间相互通信，利用收到的路由信息更新路由器表，动态寻找网络最佳路径。动态路由协议能够自动适应网络拓扑变化，适用于中大型网络。

---

Routing occurs at the network layer (Layer 3 of OSI model), consisting of two basic actions: **determining the best path** and **forwarding data through the network**. Packets are forwarded by routers according to the routing table, which contains destination network addresses and the best paths to reach them (e.g., an interface or next-hop address).

There are three ways to generate a routing table: **Directly Connected Routing**, **Static Routing**, and **Dynamic Routing**.

**Dynamic Routing** enables routers to automatically learn, update, and maintain routing tables through routing protocols (e.g., RIP, OSPF). Routers communicate with each other, exchange routing information, and dynamically find the best path. Dynamic routing protocols adapt to network topology changes automatically and are suitable for medium to large networks.

---

## Q2：什么设备可以产生路由表？ / What Devices Can Generate a Routing Table?

**答案 / Answer**：

- **路由器（Router）**是产生和维护路由表的主要设备。路由器保存着各种传输路径的地址信息表，俗称路由表（Routing Table），供数据包路由时选择。路由表中保存着到达各子网的标志信息：路由标识、获得路由方式、目标网络、转发路由器地址和经过路由器的个数等内容。
- **三层交换机（Layer 3 Switch）**开启路由功能（`ip routing`）后也可产生路由表。
- 典型的路由表产生方式有三种：**直连路由**（配置接口IP后自动生成）、**静态路由**（管理员手工配置）、**动态路由**（路由协议自动学习）。

---

- **Routers** are the primary devices that generate and maintain routing tables. A router stores address information for various transmission paths — known as the **Routing Table** — for packet forwarding decisions. The routing table contains: route identifier, route source, destination network, forwarding router address, and hop count.
- **Layer 3 switches** can also generate routing tables after enabling the routing function (`ip routing`).
- Three methods of routing table generation: **Directly Connected** (auto-generated after interface IP configuration), **Static Routing** (manually configured by administrator), and **Dynamic Routing** (automatically learned via routing protocols).

---

## Q3：最早开发以太网的公司是哪个？ / Which Company First Developed Ethernet?

**答案 / Answer**：

以太网最早由**施乐公司（Xerox）**在20世纪70年代开发。1980年，**DEC、Intel、Xerox**三家公司联合提出了以太网标准（DIX标准）。1983年，**IEEE 802.3**标准正式发布，成为以太网的国际标准。

---

Ethernet was first developed by **Xerox** in the 1970s. In 1980, **DEC, Intel, and Xerox** jointly proposed the Ethernet standard (DIX standard). In 1983, the **IEEE 802.3** standard was officially released, becoming the international standard for Ethernet.

---

## Q4：本征帧的概念，一般本征帧在哪个VLAN，本征帧的协议标准是哪个？ / What is the Concept of Native VLAN? Which VLAN is the Default Native VLAN? Which Protocol Standard?

**答案 / Answer**：

- **本征帧（Native VLAN）**：在Trunk链路上，不需要打4字节802.1Q标签就可以直接传输的帧。Trunk端口收到未打标签的帧时，自动将其归入Native VLAN。
- **默认Native VLAN**：每个Trunk口的缺省Native VLAN是**VLAN 1**。
- **协议标准**：**IEEE 802.1Q**。
- 配置命令：`Switch(config-if)# switchport trunk native vlan [VLAN号]`
- ⚠️ 注意事项：Trunk链路两端必须配置相同的Native VLAN，否则会导致VLAN跳转。

---

- **Native VLAN**：Frames transmitted over a Trunk link without the 4-byte 802.1Q tag. When a Trunk port receives an untagged frame, it automatically assigns it to the Native VLAN.
- **Default Native VLAN**：The default Native VLAN for each Trunk port is **VLAN 1**.
- **Protocol Standard**：**IEEE 802.1Q**.
- Configuration command: `Switch(config-if)# switchport trunk native vlan [VLAN-ID]`
- ⚠️ Both ends of a Trunk link must have the same Native VLAN configured.

---

## Q5：配置静态路由的一般步骤是什么？ / What are the General Steps for Configuring Static Routing?

**答案 / Answer**：

静态路由是由网络管理员手工配置的固定路由。配置静态路由用命令 `ip route`：
```
router(config)#ip route [网络编号] [子网掩码] [转发路由器的IP地址/本地接口]
```

静态路由描述转发路径的方式有两种：指向本地接口（即从本地某接口发出）；指向下一跳路由器直连接口的IP地址。

**静态路由的一般配置步骤**：
1. 为路由器每个接口配置IP地址
2. 确定本路由器有哪些直连网段的路由信息
3. 确定网络中有哪些属于本路由器的非直连网段
4. 添加本路由器的非直连网段相关的路由信息

静态路由的优点：简单、高效、可靠、网络安全保密性高。在所有路由中，静态路由优先级最高（管理距离为0或1）。

---

Static routing is a fixed routing table manually configured by the network administrator. Use the `ip route` command:
```
router(config)#ip route [network] [subnet-mask] [next-hop-IP/local-interface]
```

Two ways to describe the forwarding path: point to a local interface, or point to the next-hop router's directly connected interface IP address.

**General configuration steps**:
1. Configure IP addresses for each router interface
2. Determine which directly connected network segments the router has
3. Identify which non-direct network segments belong to this router
4. Add routing information for non-direct network segments

Advantages of static routing: simple, efficient, reliable, and high security. Static routes have the highest priority among all routes (administrative distance 0 or 1).

---

## Q6：什么是RIP协议，收敛时间是多少，跳数限制是多少？ / What is the RIP Protocol? What is its Convergence Time and Hop Count Limit?

**答案 / Answer**：

**RIP（Routing Information Protocol，路由信息协议）**由施乐（Xerox）在70年代开发，是应用较早、使用较普遍的内部网关协议（IGP），适用于小型同类网络，是典型的**距离矢量（Distance-Vector）**协议。

- **跳数限制**：最大**15跳**，16跳视为不可达。RIP以跳数来衡量到达目的网络的度量值（metric）。
- **更新周期**：每隔**30秒**定期向外发送一次更新报文。
- **收敛时间**：如果路由器经过**180秒**未收到来自某路由器的路由更新报文，则将该路由标记为不可达；若其后**240秒**内仍未收到更新报文，将该路由从路由表中删除。
- RIP收敛速度较慢（240秒以上）。

---

**RIP (Routing Information Protocol)** was developed by Xerox in the 1970s. It is an early and widely used Interior Gateway Protocol (IGP), suitable for small homogeneous networks, and is a typical **Distance-Vector** protocol.

- **Hop Count Limit**: Maximum **15 hops**; 16 hops is considered unreachable. RIP uses hop count as the metric to measure distance to the destination network.
- **Update Interval**: Sends update packets every **30 seconds**.
- **Convergence Time**: If a router receives no update from another router for **180 seconds**, the route is marked as unreachable. If still no update after **240 seconds**, the route is deleted from the routing table.
- RIP convergence is slow (240+ seconds).

---

## Q7：理解SVI、TAG VLAN、RIP、OSPF的含义 / Explain the Meanings of SVI, TAG VLAN, RIP, and OSPF

**答案 / Answer**：

- **SVI（Switch Virtual Interface，交换机虚拟接口）**：为交换机中的VLAN创建的虚拟三层接口，可配置IP地址作为该VLAN的网关，实现VLAN间路由。各VLAN中主机将相应VLAN的SVI接口地址作为本VLAN网关，数据到达三层交换机后利用路由功能转发到其他VLAN。
- **TAG VLAN（标签VLAN）**：基于**IEEE 802.1Q**标准，在以太网帧中插入4字节VLAN标签（Tag），包含12位VLAN ID（范围1-4094，支持4096个VLAN）、3位优先级（Priority）、1位格式指示符（CFI）。Trunk端口传输多VLAN数据时给帧打标签，802.1Q帧只在Trunk链路上传输，对用户透明。
- **RIP（Routing Information Protocol，路由信息协议）**：距离矢量路由协议，以跳数作为度量值，最大15跳（16跳不可达），每隔30秒更新，适用于小型网络。
- **OSPF（Open Shortest Path First，开放最短路径优先）**：链路状态路由协议，克服了RIP收敛慢（240秒以上）和15跳规模限制的弱点。采用分区域概念：骨干区域Area 0 + 非骨干区域Area N，骨干区域保持连续性，非骨干区域必须与骨干区域连接。由RFC 2328定义，适用于中大型网络。

---

- **SVI (Switch Virtual Interface)**：A virtual Layer 3 interface created for a VLAN on a switch. An IP address can be configured as the gateway for that VLAN, enabling inter-VLAN routing. Hosts in each VLAN use the SVI interface address as their VLAN gateway.
- **TAG VLAN**：Based on the **IEEE 802.1Q** standard. A 4-byte VLAN tag is inserted into Ethernet frames, containing a 12-bit VLAN ID (range 1-4094), 3-bit priority, and 1-bit CFI. Trunk ports tag frames when transmitting multi-VLAN data. 802.1Q frames are transmitted only on Trunk links and are transparent to users.
- **RIP (Routing Information Protocol)**：A distance-vector routing protocol using hop count as metric. Maximum 15 hops (16 = unreachable). Updates every 30 seconds. Suitable for small networks.
- **OSPF (Open Shortest Path First)**：A link-state routing protocol that overcomes RIP's slow convergence (240+ seconds) and 15-hop limit. Uses a hierarchical area structure: backbone Area 0 + non-backbone areas. Defined by RFC 2328. Suitable for medium to large networks.

---

## Q8：记住所有的私有地址 / Memorize All Private IP Address Ranges

**答案 / Answer**：

私有IP地址是Internet特别划分出来的，不会注册给任何组织。私有地址不需要经过注册就可以使用，但这些地址是不唯一的，只能在局域网内部使用，不能直接路由到外网（Internet）中。

**私有IP地址范围（RFC 1918定义）**：

| 类别 | 地址范围 | CIDR表示 |
|------|---------|---------|
| **A类** | 10.0.0.0 ~ 10.255.255.255 | 10.0.0.0/8 |
| **B类** | 172.16.0.0 ~ 172.31.255.255 | 172.16.0.0/12 |
| **C类** | 192.168.0.0 ~ 192.168.255.255 | 192.168.0.0/16 |

---

Private IP addresses are specially designated by the Internet and are not registered with any organization. They can be used without registration but are non-unique. They can only be used within a LAN and cannot be directly routed to the Internet.

**Private IP Address Ranges (RFC 1918)**：

| Class | Address Range | CIDR Notation |
|-------|--------------|---------------|
| **Class A** | 10.0.0.0 ~ 10.255.255.255 | 10.0.0.0/8 |
| **Class B** | 172.16.0.0 ~ 172.31.255.255 | 172.16.0.0/12 |
| **Class C** | 192.168.0.0 ~ 192.168.255.255 | 192.168.0.0/16 |

---

## Q9：交换机和路由器的各种操作模式及提示符号 / Operation Modes and Prompt Symbols for Switches and Routers

**答案 / Answer**：

一般说前四种即可：

| 模式 | 提示符 | 说明 |
|------|--------|------|
| **用户模式** User Mode | `Router>` / `Switch>` | 查看路由器信息，简单测试命令 |
| **特权模式** Privileged Mode | `Router#` / `Switch#` | 查看、管理路由器配置信息，测试、调试 |
| **全局配置模式** Global Configuration Mode | `Router(config)#` / `Switch(config)#` | 全局参数配置 |
| **端口/接口配置模式** Interface Configuration Mode | `Router(config-if)#` / `Switch(config-if)#` | 接口参数配置 |
| 线路配置模式 Line Configuration Mode | `Router(config-line)#` | 线路参数配置 |
| 路由协议配置模式 Router Protocol Configuration Mode | `Router(config-router)#` | 路由协议参数配置 |

进入方式：`Router> enable` → `Router# configure terminal` → `Router(config)#` → `Router(config)# interface fa0/1` → `Router(config-if)#`

---

Generally, the first four modes suffice:

| Mode | Prompt | Purpose |
|------|--------|---------|
| **User Mode** | `Router>` / `Switch>` | View info, simple test commands |
| **Privileged Mode** | `Router#` / `Switch#` | View/manage config, test, debug |
| **Global Configuration Mode** | `Router(config)#` / `Switch(config)#` | Global parameter configuration |
| **Interface Configuration Mode** | `Router(config-if)#` / `Switch(config-if)#` | Interface parameter configuration |
| Line Configuration Mode | `Router(config-line)#` | Line parameter configuration |
| Router Protocol Config Mode | `Router(config-router)#` | Routing protocol parameter configuration |

Entry sequence: `Router> enable` → `Router# configure terminal` → `Router(config)#` → `Router(config)# interface fa0/1` → `Router(config-if)#`

---

## Q10：综合理解RIP和OSPF / Comprehensive Understanding of RIP and OSPF

**答案 / Answer**：

| 对比项 | RIP | OSPF |
|--------|-----|------|
| **协议类型** | 距离矢量（Distance-Vector） | 链路状态（Link-State） |
| **开发者/标准** | Xerox 70年代开发 | RFC 2328定义 |
| **度量值** | 跳数（Hop Count） | 链路成本（Cost，基于带宽） |
| **最大跳数** | 15跳（16跳不可达） | 无跳数限制 |
| **更新方式** | 每30秒广播/组播更新 | 触发更新，组播224.0.0.5 |
| **收敛速度** | 慢（240秒以上） | 快 |
| **区域概念** | 无 | 骨干区域Area 0 + 非骨干区域 |
| **DR/BDR** | 无 | 有（DR指定路由器、BDR备份指定路由器） |
| **适用网络** | 小型同类网络 | 中大型网络 |
| **管理距离** | 120 | 110 |
| **VLSM支持** | RIPv1不支持，RIPv2支持 | 支持 |

---

| Comparison | RIP | OSPF |
|------------|-----|------|
| **Protocol Type** | Distance-Vector | Link-State |
| **Origin/Standard** | Xerox, 1970s | RFC 2328 |
| **Metric** | Hop Count | Cost (based on bandwidth) |
| **Max Hops** | 15 (16 = unreachable) | No limit |
| **Update Method** | Every 30s broadcast/multicast | Triggered updates, multicast 224.0.0.5 |
| **Convergence Speed** | Slow (240+ seconds) | Fast |
| **Area Concept** | None | Backbone Area 0 + non-backbone areas |
| **DR/BDR** | None | Yes (Designated Router, Backup DR) |
| **Suitable For** | Small homogeneous networks | Medium to large networks |
| **Administrative Distance** | 120 | 110 |
| **VLSM Support** | RIPv1: No, RIPv2: Yes | Yes |

---

## Q11：RIP v1和RIP v2的区别 / Differences Between RIPv1 and RIPv2

**答案 / Answer**：

| 对比项 | RIPv1 | RIPv2 |
|--------|-------|-------|
| **路由类型** | 有类路由协议（Classful） | 无类路由协议（Classless） |
| **VLSM支持** | 不支持VLSM | 支持VLSM |
| **更新报文发送形式** | 以**广播**的形式发送更新报文 | 以**组播**的形式发送更新报文 |
| **认证** | 不支持认证 | 支持明文和MD5的认证 |
| **自动汇总** | 默认开启，不可关闭 | 默认开启，可手动关闭（`no auto-summary`） |

---

| Comparison | RIPv1 | RIPv2 |
|------------|-------|-------|
| **Routing Type** | Classful routing protocol | Classless routing protocol |
| **VLSM Support** | Does NOT support VLSM | Supports VLSM |
| **Update Transmission** | **Broadcast** | **Multicast** |
| **Authentication** | No authentication | Supports plaintext and MD5 authentication |
| **Auto-Summary** | On by default, cannot disable | On by default, can disable (`no auto-summary`) |

---

## Q12：RIP路由信息的更新过程 / The RIP Route Update Process

**答案 / Answer**：

RIP协议通过以下三步过程维护路由信息：

1. **第1步**：RIP协议每隔**30秒**定期向外发送一次更新报文。
2. **第2步**：如果路由器经过**180秒**没有收到来自某一路由器的路由更新报文，则将所有来自此路由器的路由信息标志为**不可达**。
3. **第3步**：若在其后**240秒**内仍未收到更新报文，就将这些路由从路由表中**删除**。

---

RIP maintains routing information through a three-step process:

1. **Step 1**：RIP periodically sends update packets every **30 seconds**.
2. **Step 2**：If a router does not receive a route update from another router for **180 seconds**, all routes from that router are marked as **unreachable**.
3. **Step 3**：If no update is received within the subsequent **240 seconds**, those routes are **deleted** from the routing table.

---

## Q13：不同VLAN之间通过什么技术通信？三层交换机/路由器的工作模式有几种？ / What Technologies Enable Inter-VLAN Communication? How Many Working Modes for L3 Switches/Routers?

**答案 / Answer**：

**不同VLAN之间通信的三种方式**：

1. **三层交换机 + SVI（交换机虚拟接口）**：在三层交换机上为每个VLAN创建SVI虚拟接口，配置IP地址作为各VLAN的网关，利用三层交换机的路由功能实现VLAN间数据转发。数据到达三层交换机后利用路由功能转发到其他VLAN。这是最常用的方式，部署灵活，不会形成网络瓶颈。

2. **单臂路由（Router-on-a-Stick）**：利用路由器的路由功能，在路由器上为每个VLAN划分一个子接口（Subinterface），每个子接口配置IP地址作为相应VLAN的网关。缺点是部署不灵活，形成网络瓶颈（所有VLAN间流量都经过一条物理链路）。

3. **直连路由方式**：不同VLAN的主机分别连接路由器的不同物理接口。

**单臂路由配置步骤**：
```
Router(config)#interface f0/0.1
Router(config-subif)#encapsulation dot1q 10
Router(config-subif)#ip address 192.168.1.1 255.255.255.0
Router(config-subif)#no shutdown
```

---

**Three methods for Inter-VLAN Communication**:

1. **Layer 3 Switch + SVI**：Create SVI virtual interfaces for each VLAN on a Layer 3 switch, configure IP addresses as VLAN gateways, and use the switch's routing function to forward data between VLANs. This is the most common method — flexible deployment without bottlenecks.

2. **Router-on-a-Stick**：Use a router's routing function. Create a subinterface for each VLAN on the router, and configure an IP address on each subinterface as the VLAN gateway. Disadvantage: inflexible deployment and potential network bottleneck (all inter-VLAN traffic passes through a single physical link).

3. **Direct Routing**：Connect hosts from different VLANs to different physical router interfaces.

**Router-on-a-Stick Configuration Steps**：
```
Router(config)#interface f0/0.1
Router(config-subif)#encapsulation dot1q 10
Router(config-subif)#ip address 192.168.1.1 255.255.255.0
Router(config-subif)#no shutdown
```

---

## Q14：内部连通性测试命令有哪些，怎么用？ / What are the Internal Connectivity Test Commands and How to Use Them?

**答案 / Answer**：

- **ping**：使用**ICMP协议**（Internet Control Message Protocol）发送回显请求，测试网络连通性和延迟。
  - Windows：`ping 目标IP地址`（默认发送4个包）
  - Cisco路由器：`ping 目标IP地址`（持续发送，Ctrl+C停止）
  - 说明：ping命令除网络探查外还用于传输各种错误信息，路由器上不应禁止ICMP协议。

- **tracert / traceroute**：追踪数据包从源到目的地经过的每一跳路径。
  - Windows：`tracert 目标IP地址`
  - Cisco路由器：`traceroute 目标IP地址`

- **show ip route**：查看路由器的路由表信息。

---

- **ping**：Uses **ICMP protocol** to send echo request packets and test network connectivity and latency.
  - Windows: `ping <destination-IP>` (4 packets by default)
  - Cisco router: `ping <destination-IP>` (continuous, Ctrl+C to stop)
  - Note: ICMP is also used for error reporting; it should not be disabled on routers.

- **tracert / traceroute**：Traces the path (each hop) from source to destination.
  - Windows: `tracert <destination-IP>`
  - Cisco router: `traceroute <destination-IP>`

- **show ip route**：View the router's routing table.

---

## Q15：掌握静态路由，什么是默认路由，默认路由是特殊的静态路由 / Understand Static Routing and Default Routing (Default Route is a Special Static Route)

**答案 / Answer**：

**静态路由（Static Routing）**是在路由器中设置的固定路由表，除非网络管理员干预，否则不会发生变化。静态路由的优点是简单、高效、可靠，在所有路由中优先级最高（管理距离为0或1）。

**默认路由（Default Route / 缺省路由）**是一种特殊的静态路由，一般使用在**stub网络**（末端/存根网络）中。Stub网络是只有1条出口路径的网络。使用默认路由来发送那些目标网络没有包含在路由表中的数据包。Internet上大约99.99%的路由器上都存在一条默认路由。

配置命令：
```
router(config)#ip route 0.0.0.0 0.0.0.0 [转发路由器的IP地址/本地接口]
```

---

**Static Routing** is a fixed routing table configured in the router that does not change unless the network administrator intervenes. Advantages: simple, efficient, reliable, and highest priority (administrative distance 0 or 1).

**Default Route** is a special type of static route, typically used in **stub networks** (networks with only one exit path). It is used to forward packets whose destination networks are not in the routing table. Approximately 99.99% of routers on the Internet have a default route.

Configuration command:
```
router(config)#ip route 0.0.0.0 0.0.0.0 [next-hop-IP/local-interface]
```

---

## Q16：启用RIP和OSPF的命令 / Commands to Enable RIP and OSPF

**答案 / Answer**：

**RIP配置步骤**：
```
Router(config)#router rip                           ! 开启RIP路由协议进程
Router(config-router)#network 192.168.1.0           ! 申请本路由器参与RIP协议的直连网段
Router(config-router)#version 2                     ! 指定RIP协议版本2（默认version 1）
Router(config-router)#no auto-summary                ! 关闭自动汇总（RIPv2）
```

**OSPF配置步骤**：
```
Router(config)#router ospf 1                        ! 创建OSPF路由进程（进程号1）
Router(config-router)#network 192.168.0.0 0.0.255.255 area 0  ! 定义关联IP地址范围，指定区域
```

---

**RIP Configuration Steps**:
```
Router(config)#router rip                           ! Start RIP routing process
Router(config-router)#network 192.168.1.0           ! Advertise directly connected network
Router(config-router)#version 2                     ! Set RIP version 2
Router(config-router)#no auto-summary                ! Disable auto-summarization
```

**OSPF Configuration Steps**:
```
Router(config)#router ospf 1                        ! Create OSPF routing process (ID 1)
Router(config-router)#network 192.168.0.0 0.0.255.255 area 0  ! Define network range and area
```

---

## Q17：掌握直连路由概念，会写直连路由，知道默认网关 / Understand Directly Connected Routing, Write Routing Entries, and Know Default Gateway

**答案 / Answer**：

**直连路由（Directly Connected Routing）**是在配置完路由器网络接口的IP地址后**自动生成**的。如果没有对这些接口进行特殊的限制，这些接口所直连的网络之间就可以直接通信。直连路由的基本功能就是实现邻居的互通。

**路由表示例**（参考图片-园区网直连路由拓扑）：
- `C  192.168.1.0/24  F1/0` — 直连路由，目的网络192.168.1.0/24，从F1/0口出去
- `C  192.168.3.0/24  F1/1` — 直连路由，目的网络192.168.3.0/24，从F1/1口出去

**默认网关（Default Gateway）**：当主机需要发送数据到不同IP子网时，数据分组将被转发至发送主机的默认网关。如PC1的IP为192.168.1.5，默认网关为192.168.1.1（路由器F1/0口IP）。

---

**Directly Connected Routing** is **automatically generated** after configuring IP addresses on router interfaces. Networks directly connected to these interfaces can communicate with each other if no special restrictions are in place. The basic function of directly connected routing is neighbor-to-neighbor communication.

**Example Routing Table Entries**:
- `C  192.168.1.0/24  F1/0` — Direct route to network 192.168.1.0/24 via interface F1/0
- `C  192.168.3.0/24  F1/1` — Direct route to network 192.168.3.0/24 via interface F1/1

**Default Gateway**: When a host needs to send data to a different IP subnet, the packet is forwarded to the host's default gateway. Example: PC1 IP = 192.168.1.5, default gateway = 192.168.1.1 (Router's F1/0 interface IP).

---

## Q18：掌握跨交换机VLAN通信配置方法，直连路由和静态路由实验 / Master Cross-Switch VLAN Communication Configuration, Direct Routing and Static Routing Experiments

**答案 / Answer**：

**跨交换机VLAN通信 — Tag VLAN技术**：

在没有技术处理的情况下，一台交换机上VLAN中的信号无法跨越交换机传递到另一台交换机同一个VLAN成员中。如果交换机上划分了10个VLAN就需要分别连10条线做级联，端口效率太低。

解决方法：在交换机之间用一条级联线，并将对应的端口设置为**Trunk模式**，这条线路就可以承载交换机上所有VLAN的信息。Trunk端口传输多个VLAN的信息，实现同一VLAN跨越不同的交换机。

**配置步骤**（两台交换机互连）：
```
Switch1(config)#interface fastethernet 0/1
Switch1(config-if)#switchport mode trunk
Switch1(config-if)#no shutdown

Switch2(config)#interface fastethernet 0/1
Switch2(config-if)#switchport mode trunk
Switch2(config-if)#no shutdown
```

---

**Cross-Switch VLAN Communication — Tag VLAN Technology**:

Without technical processing, VLAN signals on one switch cannot cross to another switch to reach the same VLAN members. If a switch has 10 VLANs, you would need 10 separate cascade cables — this is very inefficient.

Solution: Use a single cascade cable between switches and configure the corresponding ports as **Trunk mode**. This single link can carry information for all VLANs on the switch. The Trunk port transmits data for multiple VLANs, enabling the same VLAN to span different switches.

**Configuration Steps** (connecting two switches):
```
Switch1(config)#interface fastethernet 0/1
Switch1(config-if)#switchport mode trunk
Switch1(config-if)#no shutdown

Switch2(config)#interface fastethernet 0/1
Switch2(config-if)#switchport mode trunk
Switch2(config-if)#no shutdown
```

---

## Q19：每个实验的命令配置过程必须会写 / Must be Able to Write Configuration Commands for Each Experiment

**答案 / Answer**：

**常用配置命令汇总**：

**VLAN创建与端口分配**：
```
Switch(config)#vlan 10                              ! 创建VLAN 10
Switch(config-vlan)#name test                        ! 命名VLAN
Switch(config)#interface fastethernet 0/5            ! 进入端口
Switch(config-if)#switchport access vlan 10          ! 将端口加入VLAN 10
Switch(config-if)#no shutdown
```

**批量端口加入VLAN**：
```
Switch(config)#interface range fastethernet 0/1-10   ! 连续端口，用空格分隔范围
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#no shutdown
```

**Trunk端口配置**：
```
Switch(config)#interface fastethernet 0/1
Switch(config-if)#switchport mode trunk
```

**三层交换机SVI配置（子网连通）**：
```
Switch(config)#interface fa0/1
Switch(config-if)#no switchport                      ! 将二层口转为三层口
Switch(config-if)#ip address 172.16.1.1 255.255.255.0
Switch(config-if)#no shutdown
```

---

**Common Configuration Command Summary**:

**VLAN Creation and Port Assignment**:
```
Switch(config)#vlan 10
Switch(config-vlan)#name test
Switch(config)#interface fastethernet 0/5
Switch(config-if)#switchport access vlan 10
Switch(config-if)#no shutdown
```

**Batch Port Assignment to VLAN**:
```
Switch(config)#interface range fastethernet 0/1-10   ! Continuous ports
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#no shutdown
```

**Trunk Port Configuration**:
```
Switch(config)#interface fastethernet 0/1
Switch(config-if)#switchport mode trunk
```

**L3 Switch SVI Configuration (Subnet Connectivity)**:
```
Switch(config)#interface fa0/1
Switch(config-if)#no switchport                      ! Convert L2 port to L3
Switch(config-if)#ip address 172.16.1.1 255.255.255.0
Switch(config-if)#no shutdown
```

---

## Q20：配置TAG VLAN时对端口的要求 / Port Requirements for Configuring TAG VLAN

**答案 / Answer**：

**TAG VLAN配置要点**：

1. 交换机之间互连的端口必须设置为**Trunk模式**。
2. Trunk端口默认转发交换机上**所有VLAN**的数据。
3. 802.1Q帧**只在Trunk链路上传输**，对用户透明。
4. 每个Trunk口都属于一个Native VLAN，缺省Native VLAN是**VLAN 1**。
5. Trunk链路两端必须配置**相同的Native VLAN**。
6. 可以限制Trunk端口允许通过的VLAN范围：
   ```
   Switch(config-if)# switchport trunk allowed vlan remove 2   ! 禁止VLAN 2通过该Trunk口
   ```
7. 查看Trunk端口信息：`Switch# show interfaces fastethernet0/15 switchport`

---

**TAG VLAN Configuration Requirements**:

1. Ports connecting switches MUST be set to **Trunk mode**.
2. Trunk ports forward data for **all VLANs** on the switch by default.
3. 802.1Q frames are transmitted **only on Trunk links** and are transparent to users.
4. Each Trunk port belongs to a Native VLAN; the default Native VLAN is **VLAN 1**.
5. Both ends of a Trunk link must have the **same Native VLAN** configured.
6. You can restrict VLANs allowed on a Trunk port:
   ```
   Switch(config-if)# switchport trunk allowed vlan remove 2
   ```
7. View Trunk port info: `Switch# show interfaces fastethernet0/15 switchport`

---

## Q21：路由器端口地址的配置原则是什么？ / What are the Principles for Configuring Router Port Addresses?

**答案 / Answer**：

**接口IP地址配置的基本原则**（三条）：

1. **路由器的物理网络端口需要有一个IP地址**。
2. **相邻路由器的相邻端口IP地址在同一网段**。
3. **同一路由器的不同端口在不同网段上**。

**配置命令**：
```
Router(config)#interface fa0/1
Router(config-if)#ip address 192.168.1.1 255.255.255.0
Router(config-if)#no shutdown
```

---

**Basic Principles for Interface IP Address Configuration** (Three Rules):

1. **Every physical network port on a router must have an IP address**.
2. **Adjacent ports of adjacent routers must be in the same network segment**.
3. **Different ports on the same router must be in different network segments**.

**Configuration Command**:
```
Router(config)#interface fa0/1
Router(config-if)#ip address 192.168.1.1 255.255.255.0
Router(config-if)#no shutdown
```

---

## Q22：创建VLAN、分配端口到VLAN、配置端口IP地址、启用RIP和OSPF路由 / Create VLANs, Assign Ports to VLANs, Configure Port IP Addresses, and Enable RIP and OSPF Routing

**答案 / Answer**：

这是一个综合配置流程，分为二层和三层操作：

**二层设备操作**：
```
Switch(config)#vlan 10                              ! 创建VLAN 10
Switch(config)#vlan 20                              ! 创建VLAN 20
Switch(config)#interface range fa0/1-5              ! 批量进入端口
Switch(config-if-range)#switchport access vlan 10   ! 分配到VLAN 10
Switch(config)#interface fa0/6
Switch(config-if)#switchport access vlan 20         ! 单端口分配到VLAN 20
```

**三层设备操作（SVI配置）**：
```
Switch(config)#interface vlan 10
Switch(config-if)#ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#interface vlan 20
Switch(config-if)#ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#ip routing                           ! 思科设备需启用路由功能
```

**启用RIP**：
```
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 192.168.2.0
Router(config-router)#version 2
Router(config-router)#no auto-summary
```

**启用OSPF**：
```
Router(config)#router ospf 1
Router(config-router)#network 192.168.1.0 0.0.0.255 area 0
Router(config-router)#network 192.168.2.0 0.0.0.255 area 0
```

---

This is a comprehensive configuration process with Layer 2 and Layer 3 operations:

**Layer 2 Switch Operations**:
```
Switch(config)#vlan 10
Switch(config)#vlan 20
Switch(config)#interface range fa0/1-5
Switch(config-if-range)#switchport access vlan 10
Switch(config)#interface fa0/6
Switch(config-if)#switchport access vlan 20
```

**Layer 3 Operations (SVI Configuration)**:
```
Switch(config)#interface vlan 10
Switch(config-if)#ip address 192.168.1.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#interface vlan 20
Switch(config-if)#ip address 192.168.2.1 255.255.255.0
Switch(config-if)#no shutdown
Switch(config)#ip routing                           ! Required for Cisco devices
```

**Enable RIP**:
```
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 192.168.2.0
Router(config-router)#version 2
Router(config-router)#no auto-summary
```

**Enable OSPF**:
```
Router(config)#router ospf 1
Router(config-router)#network 192.168.1.0 0.0.0.255 area 0
Router(config-router)#network 192.168.2.0 0.0.0.255 area 0
```

---

## Q23：NAT的端口应用原理 / The Port Application Principle of NAT (PAT)

**答案 / Answer**：

**PAT（Port Address Translation，端口地址转换/端口复用）**是复用NAT池的特例，通过**端口复用技术**用一个合法IP地址映射内网所有私有IP地址。这个合法地址往往就是路由器出口的IP地址（如S0/0口IP）。

**工作原理**：将内网多个私有IP地址和端口号映射到同一个公网IP地址的不同端口号上。利用端口号区分不同主机的不同会话（连接），而不是区分主机。同一主机同时建立多个会话时会占用多个端口映射。

- 理论上一个IP地址可映射约**65000个会话**，实际路由器通常支持约**4000个**（Cisco）。
- 优点：最大限度节省IP地址。
- 缺点：只能同时支持几千个会话，易造成拥塞。缓解方法：多申请IP地址建大NAT池、限制占用会话数多的应用（如BT）。

**PAT配置方法一**（建立NAT池，起始=结束）：
```
R1(config)#ip nat pool 池名 起始地址 结束地址 netmask 子网掩码
R1(config)#access-list 表号 permit 内部地址条件
R1(config)#ip nat inside source list 表号 pool 池名 overload
```

**PAT配置方法二**（不建立NAT池，直接使用出口接口）：
```
R1(config)#access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)#ip nat inside source list 30 interface s0/0 overload
```

---

**PAT (Port Address Translation / Port Multiplexing)** is a special case of multiplexed NAT pool. It uses port multiplexing technology to map all private IP addresses in the internal network to a single legal IP address (often the router's exit interface IP, e.g., S0/0).

**Working Principle**: Maps multiple internal private IP addresses and port numbers to different port numbers on a single public IP address. Port numbers distinguish different sessions (connections), not hosts. A single host with multiple simultaneous sessions occupies multiple port mappings.

- Theoretically, one IP can map ~65,000 sessions; Cisco routers typically support ~4,000.
- Advantage: Maximizes IP address savings.
- Disadvantage: Only supports a few thousand simultaneous sessions, prone to congestion. Mitigation: apply for more IP addresses for larger NAT pools, limit high-session applications (e.g., BitTorrent).

**PAT Method 1** (with NAT pool, start IP = end IP):
```
R1(config)#ip nat pool <pool-name> <start-IP> <end-IP> netmask <mask>
R1(config)#access-list <num> permit <internal-address-range>
R1(config)#ip nat inside source list <num> pool <pool-name> overload
```

**PAT Method 2** (without NAT pool, directly use exit interface):
```
R1(config)#access-list 30 permit 10.0.0.0 0.255.255.255
R1(config)#ip nat inside source list 30 interface s0/0 overload
```

---

## Q24：NAT边界路由配置应注意什么？ / What Should be Noted for NAT Border Router Configuration?

**答案 / Answer**：

**NAT边界路由配置注意事项**：

1. 局域网和ISP的网络一般应看作为**两个自治系统（AS）**，两者之间**不能通过RIP等动态路由协议学习路由**。
2. NAT路由器和与它相连的路由器之间一般通过**静态路由或默认路由**实现两边网络的连通。
3. **NAT路由器一般配置通往外网的默认路由**：
   ```
   R1(config)#ip route 0.0.0.0 0.0.0.0 [下一跳地址]
   ```
4. **ISP的路由器通过配置静态路由为局域网分配IP地址段**：
   ```
   R2(config)#ip route [地址块] [地址块掩码] [下一跳地址]
   ```
5. 不能在私有地址上启用路由协议，否则会导致私有地址被外网路由器学习到，扩大了有效范围。

**常用NAT设备**：路由器（功能强，支持多种NAT设置）、防火墙（除NAT外还提供多种保护）、代理服务器（提供局域网接入）、双网卡计算机（功能较弱，多用于小型网络）。

---

**NAT Border Router Configuration Considerations**:

1. The LAN and ISP networks should generally be treated as **two Autonomous Systems (AS)**. **Dynamic routing protocols (like RIP) should NOT be used** between them to exchange routes.
2. Connectivity between NAT routers and adjacent routers is typically achieved through **static routes or default routes**.
3. **NAT routers are typically configured with a default route to the external network**:
   ```
   R1(config)#ip route 0.0.0.0 0.0.0.0 [next-hop-IP]
   ```
4. **The ISP router configures static routes to assign IP address blocks to the LAN**:
   ```
   R2(config)#ip route [address-block] [mask] [next-hop-IP]
   ```
5. Do NOT enable routing protocols on private addresses — this would cause private addresses to be learned by external routers, expanding their effective range.

**Common NAT Devices**: Router (powerful, supports multiple NAT settings), Firewall (NAT + protection), Proxy Server (LAN access), Dual-NIC Computer (weaker, mostly for small networks).

---

## Q25：网络系统集成的特点是什么？ / What are the Characteristics of Network System Integration?

**答案 / Answer**：

**网络系统集成的四个特点**：

1. **接口规范**：选用具有最合适工作机制的设备，只关注各种设备或部件的外部特性即接口，而忽略内部技术细节。
2. **关注系统整体性能**：根据网络应用需求，关注系统的总体功能和特性，选用各种合适的部件来构造或定制所需要的网络信息系统。
3. **重视工程规范和质量管理**：任何工程方法必须以有组织的质量保证为基础。全面的质量管理和类似的理念刺激了过程的不断改进，正是这种改进导致了更加成熟的网络工程方法的不断出现。
4. **建立良好的用户关系**：系统集成商需要与用户充分交流、现场勘察、进行需求分析。

**网络工程的核心就是对于网络质量的关注**。

---

**Four Characteristics of Network System Integration**:

1. **Interface Standardization**: Select devices with the most suitable working mechanisms, focusing only on external characteristics (interfaces) while ignoring internal technical details.
2. **Focus on Overall System Performance**: Based on network application requirements, focus on overall system functionality and features, and select appropriate components to build the required network information system.
3. **Emphasis on Engineering Standards and Quality Management**: Any engineering approach must be based on organized quality assurance. Total quality management stimulates continuous process improvement, leading to more mature network engineering methods.
4. **Establish Good User Relationships**: System integrators must fully communicate with users, conduct site surveys, and perform needs analysis.

**The core of network engineering is the concern for network quality**.

---

## Q26：IP地址/子网地址/园区网的层次结构 / IP Addresses, Subnet Addressing, and Campus Network Hierarchical Structure

**答案 / Answer**：

**IP地址与子网划分**：
有时为了方便网络管理，需要将网络划分为若干个网段，打破传统8位界限，从主机地址空间中"借位"作为网络地址。建立子网掩码需要两步：确定运行IP的网段数、确定子网掩码。

**园区网三层层次结构**：
大中型以太网络在规划和设计中，普遍采用三层结构模型，按照网络的功能将网络从逻辑结构上划分为三个层次：

| 层次 | 英文 | 功能 | 设备 |
|------|------|------|------|
| **核心层** | Core Layer | 高速数据转发，网络骨干 | 高带宽千兆以上交换机，双机冗余热备份 |
| **汇聚层** | Distribution Layer | 路由聚合、流量收敛、VLAN路由、安全控制 | 支持三层交换和VLAN的交换机 |
| **接入层** | Access Layer | 工作组接入、访问控制 | 普通二层交换机（可无VLAN和三层功能） |

**流量收敛**：南向带宽和北向带宽的比例。收敛比 = 南向带宽 ÷ 北向带宽。流量收敛原因：交换机不支持线速转发、网络架构设计原因。

**线速转发**：端口在满负载的情况下，对帧进行无差错的转发。

---

**IP Addresses and Subnetting**:
For network management convenience, networks are divided into segments by "borrowing" bits from the host address space as network address bits. Creating a subnet mask requires two steps: determine the number of network segments running IP, and determine the subnet mask.

**Campus Network Three-Layer Hierarchical Structure**:
In planning and designing large/medium Ethernet networks, a three-layer structure model is commonly used, dividing the network logically by function:

| Layer | Function | Equipment |
|-------|----------|-----------|
| **Core Layer** | High-speed data forwarding, network backbone | Gigabit+ switches, dual redundant hot backup |
| **Distribution Layer** | Route aggregation, traffic convergence, VLAN routing, security control | Switches supporting L3 switching and VLAN |
| **Access Layer** | Workgroup access, access control | Standard L2 switches (VLAN/L3 not required) |

**Traffic Convergence**: The ratio of southbound to northbound bandwidth. Convergence ratio = Southbound ÷ Northbound.
**Wire-Speed Forwarding**: Error-free forwarding of frames when a port is under full load.

---

## Q27：私有地址/广播地址 / Private Addresses and Broadcast Addresses

**答案 / Answer**：

**私有地址（RFC 1918定义）**：

| 类别 | 地址范围 | CIDR |
|------|---------|------|
| A类 | 10.0.0.0 ~ 10.255.255.255 | 10.0.0.0/8 |
| B类 | 172.16.0.0 ~ 172.31.255.255 | 172.16.0.0/12 |
| C类 | 192.168.0.0 ~ 192.168.255.255 | 192.168.0.0/16 |

私有地址只能在局域网内部使用，不能直接在Internet上路由。

**广播地址**：
- **子网广播地址（直接广播）**：子网中主机位全为1的地址，用于向该子网内所有主机发送数据。如192.168.1.0/24的广播地址为192.168.1.255。
- **有限广播地址**：255.255.255.255，用于本地网络广播，路由器默认不会转发（隔离广播域）。
- **广播域**：网络中能接收同一广播帧的所有节点的集合。VLAN技术可分割广播域，控制广播风暴。
- NAT边界路由器需处理私有地址与公网地址的转换，私有地址在公网上不可路由。

---

**Private Addresses (RFC 1918)**:

| Class | Address Range | CIDR |
|-------|--------------|------|
| Class A | 10.0.0.0 ~ 10.255.255.255 | 10.0.0.0/8 |
| Class B | 172.16.0.0 ~ 172.31.255.255 | 172.16.0.0/12 |
| Class C | 192.168.0.0 ~ 192.168.255.255 | 192.168.0.0/16 |

Private addresses can only be used within a LAN and cannot be directly routed on the Internet.

**Broadcast Addresses**:
- **Subnet Broadcast (Directed Broadcast)**: The address with all host bits set to 1 in a subnet, used to send data to all hosts within that subnet. E.g., for 192.168.1.0/24, the broadcast address is 192.168.1.255.
- **Limited Broadcast**: 255.255.255.255, used for local network broadcast. Routers do not forward this by default (isolate broadcast domains).
- **Broadcast Domain**: The set of all nodes that can receive the same broadcast frame. VLAN technology can segment broadcast domains and control broadcast storms.

---

## Q28：路由器和交换机的模式符号，路由表缩写C S R O的含义 / Router and Switch Mode Symbols, and Meanings of C, S, R, O in Routing Tables

**答案 / Answer**：

**操作模式及提示符号**：

| 模式 | 路由器提示符 | 交换机提示符 |
|------|------------|------------|
| 用户模式 | `Router>` | `Switch>` |
| 特权模式 | `Router#` | `Switch#` |
| 全局配置模式 | `Router(config)#` | `Switch(config)#` |
| 接口配置模式 | `Router(config-if)#` | `Switch(config-if)#` |

**路由表缩写含义**（通过 `show ip route` 查看）：

| 缩写 | 全称 | 含义 | 管理距离 |
|------|------|------|---------|
| **C** | Connected | 直连路由 | 0 |
| **S** | Static | 静态路由 | 0（出接口）/ 1（下一跳） |
| **R** | RIP | RIP动态路由 | 120 |
| **O** | OSPF | OSPF动态路由 | 110 |

管理距离值越低，学到的路由越可信。静态配置路由优先于动态协议学到的路由。

---

**Operation Modes and Prompt Symbols**:

| Mode | Router Prompt | Switch Prompt |
|------|-------------|---------------|
| User Mode | `Router>` | `Switch>` |
| Privileged Mode | `Router#` | `Switch#` |
| Global Config Mode | `Router(config)#` | `Switch(config)#` |
| Interface Config Mode | `Router(config-if)#` | `Switch(config-if)#` |

**Routing Table Abbreviation Meanings** (via `show ip route`):

| Abbreviation | Full Name | Meaning | Admin Distance |
|-------------|-----------|---------|----------------|
| **C** | Connected | Directly connected route | 0 |
| **S** | Static | Static route | 0 (interface) / 1 (next-hop) |
| **R** | RIP | RIP dynamic route | 120 |
| **O** | OSPF | OSPF dynamic route | 110 |

Lower administrative distance = more trustworthy route. Static routes take precedence over dynamically learned routes.

---

## Q29：三层交换机默认工作在第几层？ / Which Layer Does a Layer 3 Switch Operate at by Default?

**答案 / Answer**：

- 三层交换机**默认工作在第二层（数据链路层）**。
- 三层交换机本质是"二层交换机 + 路由模块"，数据转发优先使用硬件交换（二层）。
- 只有开启路由功能（`ip routing`，思科设备需要）后，才能进行三层路由转发。
- 三层交换机用于核心层/汇聚层，作为连接所有区域的核心设备。
- 在组建中型网络时，把交换速度更快、网络管理功能更先进的三层交换机作为连接所有区域的核心设备。

---

- A Layer 3 switch **operates at Layer 2 (Data Link Layer) by default**.
- A Layer 3 switch is essentially a "Layer 2 switch + routing module." Data forwarding prioritizes hardware switching (Layer 2).
- Layer 3 routing only occurs after enabling the routing function (`ip routing`, required for Cisco devices).
- Layer 3 switches are used in the core/distribution layers as core devices connecting all areas.
- In medium-sized networks, Layer 3 switches with faster switching speeds and more advanced management serve as core devices connecting all areas.

---

## Q30：三层交换机上创建VLAN40/VLAN80，配置地址 / Create VLAN40 and VLAN80 on a Layer 3 Switch and Configure Addresses

**答案 / Answer**：

在三层交换机上创建VLAN 40和VLAN 80并配置SVI地址：

```
Switch#configure terminal
Switch(config)#vlan 40                              ! 创建VLAN 40
Switch(config-vlan)#exit
Switch(config)#vlan 80                              ! 创建VLAN 80
Switch(config-vlan)#exit

Switch(config)#interface vlan 40                    ! 进入VLAN 40的SVI接口
Switch(config-if)#ip address 172.16.40.1 255.255.255.0
Switch(config-if)#no shutdown

Switch(config)#interface vlan 80                    ! 进入VLAN 80的SVI接口
Switch(config-if)#ip address 172.16.80.1 255.255.255.0
Switch(config-if)#no shutdown

Switch(config)#ip routing                           ! 启用路由功能（思科设备必须）
```

各VLAN中主机将三层交换机上相应VLAN的SVI接口地址作为本VLAN网关。

---

Create VLAN 40 and VLAN 80 on a Layer 3 switch and configure SVI addresses:

```
Switch#configure terminal
Switch(config)#vlan 40
Switch(config-vlan)#exit
Switch(config)#vlan 80
Switch(config-vlan)#exit

Switch(config)#interface vlan 40
Switch(config-if)#ip address 172.16.40.1 255.255.255.0
Switch(config-if)#no shutdown

Switch(config)#interface vlan 80
Switch(config-if)#ip address 172.16.80.1 255.255.255.0
Switch(config-if)#no shutdown

Switch(config)#ip routing                           ! Enable routing (required for Cisco)
```

Hosts in each VLAN use the corresponding SVI interface address as their VLAN gateway.

---

## Q31：直连路由及默认路由 / Directly Connected Routing and Default Routing

**答案 / Answer**：

**直连路由（Directly Connected Routing）**：
- 配置完路由器网络接口IP地址后**自动生成**。
- 直连路由基本功能是**实现邻居的互通**。
- 在路由表中显示为 `C`，管理距离为0。

**默认路由（Default Route）**：
- 默认路由是静态路由的一种**特殊情况**，使用 `0.0.0.0 0.0.0.0` 匹配所有未知目标网络。
- 一般使用在**stub网络**（只有1条出口路径的网络）中。
- 配置命令：
  ```
  router(config)#ip route 0.0.0.0 0.0.0.0 [下一跳地址/本地接口]
  ```
- Internet上大约99.99%的路由器上都存在一条默认路由。

**两者的关系**：直连路由自动生成，默认路由手动配置。在边界路由器上，内部网段使用直连路由，外网流量通过默认路由转发。

---

**Directly Connected Routing**:
- **Automatically generated** after configuring IP addresses on router interfaces.
- Basic function: **enable neighbor-to-neighbor communication**.
- Displayed in routing table as `C`, administrative distance 0.

**Default Route**:
- A **special case** of static routing, using `0.0.0.0 0.0.0.0` to match all unknown destination networks.
- Typically used in **stub networks** (networks with only one exit path).
- Configuration:
  ```
  router(config)#ip route 0.0.0.0 0.0.0.0 [next-hop-IP/local-interface]
  ```
- Approximately 99.99% of routers on the Internet have a default route.

**Relationship**: Direct routes are generated automatically; default routes are manually configured. On border routers, internal segments use direct routes while external traffic is forwarded via the default route.

---

## Q32：两台交换机VLAN互通配置 / VLAN Intercommunication Configuration Between Two Switches

**答案 / Answer**：

两台交换机通过Trunk链路实现跨交换机同一VLAN通信：

**交换机1配置**：
```
Switch1(config)#vlan 10
Switch1(config)#vlan 20
Switch1(config)#interface fastethernet 0/10
Switch1(config-if)#switchport mode access
Switch1(config-if)#switchport access vlan 10
Switch1(config-if)#exit
Switch1(config)#interface fastethernet 0/24
Switch1(config-if)#switchport mode trunk            ! 级联口设置为Trunk
Switch1(config-if)#no shutdown
```

**交换机2配置**：
```
Switch2(config)#vlan 10
Switch2(config)#vlan 20
Switch2(config)#interface fastethernet 0/10
Switch2(config-if)#switchport mode access
Switch2(config-if)#switchport access vlan 10
Switch2(config-if)#exit
Switch2(config)#interface fastethernet 0/24
Switch2(config-if)#switchport mode trunk            ! 级联口设置为Trunk
Switch2(config-if)#no shutdown
```

**关键点**：级联链路两端都必须设置Trunk模式，Trunk端口承载所有VLAN信息，实现同一VLAN跨越不同交换机。

---

Two switches communicate across switches within the same VLAN via Trunk links:

**Switch 1 Configuration**:
```
Switch1(config)#vlan 10
Switch1(config)#vlan 20
Switch1(config)#interface fastethernet 0/10
Switch1(config-if)#switchport mode access
Switch1(config-if)#switchport access vlan 10
Switch1(config-if)#exit
Switch1(config)#interface fastethernet 0/24
Switch1(config-if)#switchport mode trunk            ! Set cascade port to Trunk
Switch1(config-if)#no shutdown
```

**Switch 2 Configuration** (same structure as Switch 1):
```
Switch2(config)#vlan 10
Switch2(config)#vlan 20
Switch2(config)#interface fastethernet 0/10
Switch2(config-if)#switchport mode access
Switch2(config-if)#switchport access vlan 10
Switch2(config-if)#exit
Switch2(config)#interface fastethernet 0/24
Switch2(config-if)#switchport mode trunk
Switch2(config-if)#no shutdown
```

**Key Point**: Both ends of the cascade link must be set to Trunk mode. Trunk ports carry information for all VLANs, enabling the same VLAN to span different switches.

---

## Q33：配置静态路由连通网络 / Configure Static Routing for Network Connectivity

**答案 / Answer**：

静态路由配置用于连通非直连网段，使用 `ip route` 命令：

**配置命令格式**：
```
router(config)#ip route [目标网络] [子网掩码] [下一跳IP地址/本地出接口]
```

**示例**（路由器RA去往202.99.8.0网络）：
```
RA(config)#ip route 202.99.8.0 255.255.255.0 s0    ! 指向本地接口
或
RA(config)#ip route 202.99.8.0 255.255.255.0 172.16.2.2  ! 指向下一跳IP
```

**静态路由描述转发路径的两种方式**：
1. 指向本地接口（即从本地某接口发出）
2. 指向下一跳路由器直连接口的IP地址

**配置步骤回顾**：
1. 为路由器每个接口配置IP地址
2. 确定本路由器有哪些直连网段
3. 确定哪些是非直连网段
4. 添加非直连网段的路由信息

---

Static routing is used to connect non-direct network segments using the `ip route` command:

**Configuration Command Format**:
```
router(config)#ip route [destination-network] [subnet-mask] [next-hop-IP/local-interface]
```

**Example** (Router RA to reach 202.99.8.0 network):
```
RA(config)#ip route 202.99.8.0 255.255.255.0 s0              ! Point to local interface
or
RA(config)#ip route 202.99.8.0 255.255.255.0 172.16.2.2      ! Point to next-hop IP
```

**Two ways to describe the forwarding path**:
1. Point to a local interface (send from this interface)
2. Point to the next-hop router's directly connected interface IP

**Configuration Steps Review**:
1. Configure IP addresses for each router interface
2. Determine which segments are directly connected
3. Identify non-direct network segments
4. Add routing information for non-direct segments

---

## Q34：综合实验（实验15） / Comprehensive Experiment (Experiment 15)

**答案 / Answer**：

综合实验（实验15）目标是**组建园区网，实现园区网互通**，涵盖网络工程全流程。

**实验场景**：学校合并两个校区，需要在两个不同子网规划的校园网之间实现互联互通，并与外网连接。

**实验拓扑与初始配置**：
- SWITCH1（二层）：划分VLAN10、VLAN20，F0/1-5属于VLAN10，F0/6-10属于VLAN20
- SWITCH2（二层）：划分VLAN10、VLAN30，F0/1-5属于VLAN10，F0/6-10属于VLAN30
- SWITCH1利用两条链路接入核心交换机，采用**802.3ad链路聚合**提高链路带宽，提供冗余链路
- SWITCH3（三层核心交换机）和出口路由器R0相连，采用**SVI方式**配置
- R0和电信端路由器R1利用V.35直连
- 局域网内部三层交换机和路由器间利用**RIPv2**实现全网互通
- 路由器连外网配置**默认路由**
- 配置**动态NAPT**实现局域网访问互联网

**安全策略（ACL）**：
1. VLAN10主机可以访问VLAN20主机，VLAN30主机不可以访问VLAN20主机
2. VLAN30主机不可以访问WWW Server

**涉及的全部技术**：VLAN划分与Trunk配置、SVI接口地址配置、链路聚合（802.3ad）、直连路由与静态路由、默认路由、RIP动态路由协议（RIPv2）、NAT/PAT地址转换、ACL访问控制列表。

**实验设备**：5台PC、二层交换机2台、三层交换机1台、路由器2台、跳线10条以上。

---

The Comprehensive Experiment (Experiment 15) aims to **build a campus network and achieve campus-wide connectivity**, covering the entire network engineering process.

**Scenario**: A school merges two campuses and needs to achieve connectivity between two campus networks with different subnet plans, and connect them to the external network.

**Topology and Initial Configuration**:
- SWITCH1 (L2): VLAN10, VLAN20. F0/1-5 → VLAN10, F0/6-10 → VLAN20
- SWITCH2 (L2): VLAN10, VLAN30. F0/1-5 → VLAN10, F0/6-10 → VLAN30
- SWITCH1 uses two links to connect to the core switch via **802.3ad Link Aggregation** for increased bandwidth and redundancy
- SWITCH3 (L3 Core Switch) connects to border router R0 via **SVI configuration**
- R0 and ISP router R1 connected via V.35 serial link
- **RIPv2** enables full connectivity between internal L3 switch and routers
- **Default route** configured on the router toward the external network
- **Dynamic NAPT** enables LAN-to-Internet access

**Security Policies (ACL)**:
1. VLAN10 hosts can access VLAN20 hosts; VLAN30 hosts CANNOT access VLAN20 hosts
2. VLAN30 hosts CANNOT access the WWW Server

**Technologies Covered**: VLAN creation & Trunk configuration, SVI interface addressing, Link Aggregation (802.3ad), Direct & Static routing, Default routing, RIP dynamic routing (RIPv2), NAT/PAT address translation, ACL access control lists.

**Equipment**: 5 PCs, 2 L2 switches, 1 L3 switch, 2 routers, 10+ patch cables.

---

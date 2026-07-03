# 第5章 访问控制列表(ACL) — ACL概述与工作原理

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 1：第5章 访问控制列表(ACL)Chapter 5, Access Control Lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

第5章 访问控制列表(ACL)Chapter 5, Access Control Lists

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

第5章 访问控制列表(ACL)Chapter 5, Access Control Lists

</div>

---

### 📄 Slide 2：5.1 ACL概述5.1Overview of ACL

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

利用ACL可以对经过路由器的数据包按照设定的规则进行过滤，使数据包有选择的通过路由器，起到防火墙的作用。
访问控制列表(ACL)由一组规则组成，在规则中定义允许或拒绝通过路由器的条件。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.1 ACL概述5.1Overview of ACL
ACL can filter the data packets through the router according to the set rules, so that the data packets can be selected through the router, and play the role of firewall.
An access control list (ACL) consists of a set of rules that define conditions for allowing or denying access to a router.

</div>

---

### 📄 Slide 3：5.1 ACL概述5.1Overview of ACL

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

ACL过滤的依据主要包括源地址、目的地址、上层协议等。
ACL有两种：标准访问控制列表、扩展访问控制列表。
ACL的基本用途是限制访问网络的用户，保护网络的安全。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.1 ACL概述5.1Overview of ACL
ACL filtering is based on source address, destination address, upper protocol and so on.
There are two kinds of ACLs: standard access control lists and extended access control lists.
The basic purpose of ACL is to restrict the users accessing the network and protect the security of the network.

</div>

---

### 📄 Slide 4：ACL一般只在以下路由器上配置：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

ACL一般只在以下路由器上配置：
1、内部网和外部网的边界路由器。
2、两个功能网络交界的路由器。
1、允许那些用户访问网络。（根据用户的IP地址进行限制）
2、允许用户访问的类型，如允许http和ftp的访问，但拒绝Telnet的访问。（根据用户使用的上层协议进行限制）

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Acls are typically configured only on the following routers:
1.Internal network and external network border routers.
2. Routers at the interface of two functional networks.
限制的内容通常包括：The restrictions usually include:
1. Allow those users to access the network. (Limit based on the user's IP address)
2.The type of user access is allowed, such as http and ftp access is allowed, but Telnet access is denied. (Limited by the upper protocol you are using)

</div>
**💻 配置命令：**

```cisco
1.Internal network and external network border routers.
2. Routers at the interface of two functional networks.
1. Allow those users to access the network. (Limit based on the user's IP address)
```


---

### 📄 Slide 5：ACL的工作过程   How ACL works

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

访问控制列表(ACL) 由多条判断语句组成。每条语句给出一个条件和处理方式（通过或拒绝）。
路由器对收到的数据包按照判断语句的书写次序进行检查，当遇到相匹配的条件时，就按照指定的处理方式进行处理。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

ACL的工作过程   How ACL works
Access Control List (ACL) consists of a number of judgment statements. Each statement gives a condition and a response (pass or reject).
The router checks the received packets according to the order of the judgment statements, and when it meets the matching conditions, it processes the packets according to the specified processing mode.

</div>

---

### 📄 Slide 6：ACL的工作过程   How ACL works

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

ACL中各语句的书写次序非常重要，如果一个数据包和某判断语句的条件相匹配时，该数据包的匹配过程就结束了，剩下的条件语句被忽略。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

ACL的工作过程   How ACL works
The order of statements in an ACL is very important. If a packet matches the condition of a judgment statement, the matching process of the packet is over, and the remaining conditional statements are ignored.

</div>

---

### 📄 Slide 7：5.2 ACL语句  5.2 ACL statements

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一个访问控制列表(ACL)可由多条语句组成，每条ACL语句的形式为：
ACL表号：用于区分各访问控制列表。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.2 ACL语句  5.2 ACL statements
An Access control list (ACL) can consist of multiple statements.Each ACL statement is of the form:
Router(config)# access-list 表号 处理方式 条件
ACL table number: Used to distinguish between access control lists.

</div>
**💻 配置命令：**

```cisco
Router(config)# access-list 表号 处理方式 条件
```


---

### 📄 Slide 8：5.2 ACL语句 5.2 ACL statements

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一台路由器中可定义多个ACL，每个ACL使用一个表号。
其中针对IP数据报的ACL可使用的表号为：
标准访问控制列表：1~99。
扩展访问控制列表：100~199。
同一个ACL中各语句的表号相同。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.2 ACL语句 5.2 ACL statements
Multiple ACLs can be defined in a router, and each ACL uses a table number.
The table numbers that can be used for ACL of IP datagrams are:
Standard access control lists: 1-99
扩展访问控制列表：100~199。
Extended Access control lists: 100 to 199.
Statements in the same ACL have the same table number.

</div>
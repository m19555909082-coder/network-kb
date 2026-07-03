# 第5章 访问控制列表(ACL) — 标准ACL配置

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 15：any条件：any Condition:

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

当条件为所有地址时，如果使用通配符掩码应写为：
这时可以用“any”表示这个条件。
上面两个语句是等价的。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

any条件：any Condition:
0.0.0.0 255.255.255.255
When the condition is all addresses, the wildcard mask should be written as follows:0.0.0.0  255.255.255.255
You can use "any" for this condition.
如：For example:
Router(config)# access-list 1 permit 0.0.0.0 255.255.255.255
Router(config)# access-list 1 permit any
The above two statements are equivalent.

</div>
**💻 配置命令：**

```cisco
Router(config)# access-list 1 permit 0.0.0.0 255.255.255.255
Router(config)# access-list 1 permit any
```


---

### 📄 Slide 16：host关键字：The “host”  keyword:

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

当条件为单一IP地址时，如果使用通配符掩码应写为：
这时可以用“host”关键字定义这个条件。
上面两个语句是等价的。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

host关键字：The “host”  keyword:
IP地址 0.0.0.0
When the condition is a single IP address, the wildcard mask should be written as follows:IP address  0.0.0.0
This condition can be defined using the "host" keyword.
如：For example:
Router(config)# access-list 1 permit 200.1.1.5  0.0.0.0
Router(config)# access-list 1 permit host 200.1.1.5
The above two statements are equivalent.

</div>
**💻 配置命令：**

```cisco
When the condition is a single IP address, the wildcard mask should be written as follows:IP address  0.0.0.0
Router(config)# access-list 1 permit 200.1.1.5  0.0.0.0
Router(config)# access-list 1 permit host 200.1.1.5
```


---

### 📄 Slide 17：5.3 标准访问控制列表5.3 Standard access control lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

标准ACL只能使用地址作为条件。
标准ACL使用数据包的源地址匹配ACL语句中的条件。
定义标准ACL时，可使用的表号为1~99。（针对IP数据报）

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.3 标准访问控制列表5.3 Standard access control lists
Standard ACL can only use addresses as conditions.
Standard ACLs use the source address of a packet to match a condition in an ACL statement.
定义标准ACL时，可使用的表号为1~99。（针对IP数据报）
Standard ACLs can be defined with table numbers 1 to 99. (For IP datagrams)

</div>

---

### 📄 Slide 18：标准ACL配置举例1Example 1 of a standard ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一个局域网连接在路由器R1的E0口，这个局域网要求只有来自10.0.0.0/8、192.168.0.0/24、192.168.1.0/24的用户能够访问。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

标准ACL配置举例1Example 1 of a standard ACL configuration
R1
E0
一个局域网连接在路由器R1的E0口，这个局域网要求只有来自10.0.0.0/8、192.168.0.0/24、192.168.1.0/24的用户能够访问。
A local area network is connected to the E0 port of router R1. This LAN requires that only users from 10.0.0.0/8, 192.168.0.0/24, 192.168.1.0/24 can access it.

</div>

---

### 📄 Slide 19：R1(config)# access-list 1 permit 10.0.0.0 0.255.255.255

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置完成后，可以用命令查看ACL：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 1 permit 10.0.0.0 0.255.255.255
R1(config)# access-list 1 permit 192.168.0.0 0.0.0.255
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R1(config)# interface e0
R1(config-if)# ip access-group 1 out
Once configured, you can view the ACL with the command:
R1# show access-lists

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 1 permit 10.0.0.0 0.255.255.255
R1(config)# access-list 1 permit 192.168.0.0 0.0.0.255
R1(config)# access-list 1 permit 192.168.1.0 0.0.0.255
R1(config)# interface e0
R1# show access-lists
```


---

### 📄 Slide 20：说明：Explain

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：Explain
1、在每个ACL中都隐含着一个语句：
它位于ACL的最后，表示拒绝所有。所以任何一个与前面各语句都不匹配的数据包都会被拒绝。
2、在ip access-group语句中，用in或out表示入栈时匹配或出站时匹配，如果没有指定这个值，默认为out。
3、在每个接口、每个方向上只能应用一个ACL。
4、一个ACL可以应用到多个接口上。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

说明：Explain
1. Implicit in each ACL is a statement:
access-list list-num deny any
It is located at the end of the ACL to reject all. So any packet that doesn't match any of the preceding statements will be rejected.
2、在ip access-group语句中，用in或out表示入栈时匹配或出站时匹配，如果没有指定这个值，默认为out。
2. In the ip access-group statement, use in or out to indicate an inbound match or an outbound match; if this value is not specified, it defaults to out.
3, Only one ACL can be applied in each interface and in each direction.
An ACL can be applied to multiple interfaces.

</div>
**💻 配置命令：**

```cisco
access-list list-num deny any
3, Only one ACL can be applied in each interface and in each direction.
```


---

### 📄 Slide 21：R1

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

实例1的实验验证：

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1
R2
PC1: .2
PC2: .1.1.2
PC3: .1.1.2
E0: .1
E0: .1.1.1
E1: .1.1.1
S0: .1
S0: .2
192.168.0.0/24
192.168.1.0/24
10.0.0.0/8
20.0.0.0/8
Experimental verification of Example 1:

</div>

---

### 📄 Slide 22：标准ACL配置举例2Example 2 of a standard ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一个局域网连接在路由器R1的E0口，这个局域网要求拒绝来自192.168.10.0/24的用户访问，其它用户都可以访问。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

标准ACL配置举例2Example 2 of a standard ACL configuration
R1
E0
一个局域网连接在路由器R1的E0口，这个局域网要求拒绝来自192.168.10.0/24的用户访问，其它用户都可以访问。
A local area network is connected to the E0 port of router R1. This LAN requires to deny the user access from 192.168.10.0/24, and other users can access.

</div>
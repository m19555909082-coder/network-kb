# 第5章 访问控制列表(ACL) — 扩展ACL配置

> 10 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 23：R1(config)# access-list 1 deny 192.168.10.0 0.0.0.255

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

注意：access-list 1 permit any语句不能省略，如果省略该语句，则所有和语句1不匹配的数据包都会被隐含的access-list 1 deny any语句拒绝。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 1 deny 192.168.10.0 0.0.0.255
R1(config)# access-list 1 permit any
R1(config)# interface e0
R1(config-if)# ip access-group 1 out
注意：access-list 1 permit any语句不能省略，如果省略该语句，则所有和语句1不匹配的数据包都会被隐含的access-list 1 deny any语句拒绝。
Note: The access-list 1 permit any statement cannot be omitted. If this statement is omitted, all packets that do not match statement 1 will be rejected by the implicit access-list 1 deny any statement.

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 1 deny 192.168.10.0 0.0.0.255
R1(config)# access-list 1 permit any
R1(config)# interface e0
注意：access-list 1 permit any语句不能省略，如果省略该语句，则所有和语句1不匹配的数据包都会被隐含的access-list 1 deny any语句拒绝。
Note: The access-list 1 permit any statement cannot be omitted. If this statement is omitted, all packets that do not match statement 1 will be rejected by the implicit access-list 1 deny any statement.
```


---

### 📄 Slide 24：标准ACL配置举例3Example 3 of a standard ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一个局域网连接在路由器R1的E0口，这个局域网只允许来自192.168.20.0/24的用户访问，但其中192.168.20.1和192.168.20.5两台主机除外。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

标准ACL配置举例3Example 3 of a standard ACL configuration
R1
E0
一个局域网连接在路由器R1的E0口，这个局域网只允许来自192.168.20.0/24的用户访问，但其中192.168.20.1和192.168.20.5两台主机除外。
A local area network is connected to the E0 port of router R1. This LAN only allows users from 192.168.20.0/24 to access, except for two hosts 192.168.20.1 and 192.168.20.5.

</div>

---

### 📄 Slide 25：R1(config)# access-list 1 deny host 192.168.20.1

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

注意：access-list 1 permit 192.168.20 0.0.0.255语句不能写在另两条语句的前面，如果把它写在第1句，则192.168.20.1和192.168.20.5因已经满足了条件，不会再进行后面的匹配。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 1 deny host 192.168.20.1
R1(config)# access-list 1 deny host 192.168.20.5
R1(config)# access-list 1 permit 192.168.20.0 0.0.0.255
R1(config)# interface e0
R1(config-if)# ip access-group 1 out
注意：access-list 1 permit 192.168.20 0.0.0.255语句不能写在另两条语句的前面，如果把它写在第1句，则192.168.20.1和192.168.20.5因已经满足了条件，不会再进行后面的匹配。
Note: The access-list 1 permit 192.168.20 0.0.0.255 statement cannot be written before the other two statements.If it is written in the first statement, 192.168.20.1 and 192.168.20.5 will not be matched because the condition is already met.

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 1 deny host 192.168.20.1
R1(config)# access-list 1 deny host 192.168.20.5
R1(config)# access-list 1 permit 192.168.20.0 0.0.0.255
R1(config)# interface e0
注意：access-list 1 permit 192.168.20 0.0.0.255语句不能写在另两条语句的前面，如果把它写在第1句，则192.168.20.1和192.168.20.5因已经满足了条件，不会再进行后面的匹配。
Note: The access-list 1 permit 192.168.20 0.0.0.255 statement cannot be written before the other two statements.If it is written in the first statement, 192.168.20.1 and 192.168.20.5 will not be matched because the condition is already met.
```


---

### 📄 Slide 26：说明：Explain

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：Explain
定义ACL时，每条语句都按输入的次序加入到ACL的末尾，如果想要更改某条语句，或者更改语句的顺序，只能先删除整个ACL，再重新输入。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

说明：Explain
When defining an ACL, each statement is appended to the end of the ACL in the order it was entered, so if you want to change a statement or the order of the statements, you have to delete the entire ACL and type it again.

</div>

---

### 📄 Slide 27：比如删除表号为1的ACL：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

比如删除表号为1的ACL：
在实际应用中，我们往往把路由器的配置文件导出到TFTP服务器中，用文本编辑工具修改ACL，然后再把配置文件装回到路由器中。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

比如删除表号为1的ACL：
For example, to delete an ACL with table number 1:
Router(config)# no access-list 1
In practice, we usually export the router configuration file to the TFTP server, modify the ACL with a text editor, and then install the configuration file back into the router.

</div>
**💻 配置命令：**

```cisco
Router(config)# no access-list 1
```


---

### 📄 Slide 28：5.4 扩展访问控制列表5.4 Extended access control lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

扩展ACL可以使用地址作为条件，也可以用上层协议作为条件。
扩展ACL既可以测试数据包的源地址，也可以测试数据包的目的地址。
定义扩展ACL时，可使用的表号为100~199。（针对IP数据报）

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.4 扩展访问控制列表5.4 Extended access control lists
Extended ACLs can use addresses as conditions or upper layer protocols as conditions.
Extended ACL can test both the source address and the destination address of a packet.
定义扩展ACL时，可使用的表号为100~199。（针对IP数据报）
When defining extended ACLs, table numbers from 100 to 199 can be used. (For IP datagrams)

</div>

---

### 📄 Slide 29：扩展ACL的语句：Extended ACL statements:

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

access-list  表号  处理方式   条件
处理方式：permit（允许）或deny（拒绝）。
条件： 协议  源地址  目的地址  [运算符 端口号]

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL的语句：Extended ACL statements:
access-list  表号  处理方式   条件
access-list table number   processing mode    condition
表号：取值100~199。Table number: Range from 100 to 199.
处理方式：permit（允许）或deny（拒绝）。
Processing: permit or deny.
条件： 协议  源地址  目的地址  [运算符 端口号]
Condition: Protocol     source address       Destination address [Operator port number]

</div>

---

### 📄 Slide 30：协议：用于匹配数据包使用的网络层或传输层协议，如IP、TCP、UDP、ICMP等。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

协议：用于匹配数据包使用的网络层或传输层协议，如IP、TCP、UDP、ICMP等。
源地址、目的地址：使用“地址 通配符掩码”的形式，也可以使用any、host关键字。
运算符 端口号：用于匹配TCP、UDP数据包中的端口号。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Protocol: This is used to match the network or transport layer protocol used by the packet, such as IP, TCP, UDP, ICMP, etc.
Source address, destination address: Use the form "address wildcard mask", or use the any, host keywords.
Operator    port  number: Used to match the port number in TCP and UDP packets.

</div>

---

### 📄 Slide 31：运算符包括lt(小于)、gt(大于)、eq(等于)、neq(不等于)。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

运算符包括lt(小于)、gt(大于)、eq(等于)、neq(不等于)。
端口号用于对应一种应用，如21—FTP、23—Telnet、25—SMTP、53—DNS、80—HTTP等。
“运算符  端口号”可匹配数据包的用途。如：“eq 80”可匹配那些访问Web网站的数据包。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

运算符包括lt(小于)、gt(大于)、eq(等于)、neq(不等于)。
The operators include lt(less than), gt(greater than), eq(equal to), and neq(not equal to).
端口号用于对应一种应用，如21—FTP、23—Telnet、25—SMTP、53—DNS、80—HTTP等。
Port numbers are used to correspond to one application, such as 21-FTP, 23-telnet, 25-SMTP, 53-DNS, 80-HTTP, and so on.
The operator port number matches the purpose of the packet. For example, "eq 80" matches packets that visit the Web site.

</div>

---

### 📄 Slide 32：在扩展ACL语句中， “运算符 端口号”可以没有。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

在扩展ACL语句中， “运算符 端口号”可以没有。
表示允许来自192.168.*.*的用户访问位于10.*.*.*的Web站点。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

In the extended ACL statement, "operator   port number" can be omitted.
例：For example
access-list 100 permit tcp 192.168.0.0 0.0.255.255 10.0.0.0 0.255.255.255 eq 80
表示允许来自192.168.*.*的用户访问位于10.*.*.*的Web站点。
Indicates that the user from 192.168.*.* is allowed to access the Web site at 10.*.*.*

</div>
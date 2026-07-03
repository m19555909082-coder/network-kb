# 第5章 访问控制列表(ACL) — ACL放置规则与综合应用

> 12 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 41：扩展ACL配置举例4Example 4 of an extended ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1是局域网和外网的边界路由器，禁止对S0口的ping操作。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL配置举例4Example 4 of an extended ACL configuration
R1
E0
R1 is the border router between the LAN and the external network, and the ping operation to the S0 port is prohibited.
S0
192.168.*.*
192.168.0.1/24
200.1.1.1/24

</div>

---

### 📄 Slide 42：R1(config)# access-list 100 deny icmp any host 200.1.1.1

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：ping命令使用的是ICMP协议，但ICMP除了具有网络探查功能外，还需要用它传输各种错误信息，所以在路由器上不应该禁止该协议。如果想要禁止ping，最好使用专用的防火墙。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 100 deny icmp any host 200.1.1.1
R1(config)# access-list 100 permit ip any any
R1(config)# interface s0
R1(config-if)# ip access-group 100 in
Note: The ping command uses the ICMP protocol, but ICMP is required to transmit various error messages in addition to network probing, so it should not be disabled on the router. If you want to disable ping, it's best to use a dedicated firewall.

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 100 deny icmp any host 200.1.1.1
R1(config)# access-list 100 permit ip any any
R1(config)# interface s0
Note: The ping command uses the ICMP protocol, but ICMP is required to transmit various error messages in addition to network probing, so it should not be disabled on the router. If you want to disable ping, it's best to use a dedicated firewall.
```


---

### 📄 Slide 43：5.5 命名访问控制列表5.5 Named access control lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

命名ACL是新版路由器操作系统(11.2以后的版本)增加的一种定义ACL的方法。
命名ACL使用一个符号串作为ACL的名字，不再使用表号。
命名ACL也有标准ACL和扩展ACL两种，一个命名ACL只能是其中的一种。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.5 命名访问控制列表5.5 Named access control lists
命名ACL是新版路由器操作系统(11.2以后的版本)增加的一种定义ACL的方法。
Named  ACLs is a way of defining ACLs that has been added to router operating systems since version 11.2.
Named ACLs use a symbol string as the name of the ACL, not the table number.
命名ACL也有标准ACL和扩展ACL两种，一个命名ACL只能是其中的一种。
There are also two types of named ACLs, standard ACLs and extended ACLs, and a named ACL can only be one of them.

</div>

---

### 📄 Slide 44：命名ACL配置方法Named  ACL configuration method

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

standard：定义标准命名ACL。
extended：定义扩展命名ACL。
name：ACL的名字，可自定义。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

命名ACL配置方法Named  ACL configuration method
Router(config)# ip access-list { standard | extended } name
standard：定义标准命名ACL。
standard：(Define standard named ACLs.)
extended：定义扩展命名ACL。
extended：(Define the extension named ACL.)
name：ACL的名字，可自定义。
name：(A customizable name for the ACL.)

</div>
**💻 配置命令：**

```cisco
Router(config)# ip access-list { standard | extended } name
```


---

### 📄 Slide 45：命名ACL配置方法Named  ACL configuration method

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

该命令执行后，提示符变为Router(config-std-nacl)#或Router(config-ext-nacl)#。在此提示符下可输入ACL语句。
命名ACL语句格式：处理方式 条件。
它只比以前的ACL少了前面的“access-list 表号”部分，其它都相同。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

命名ACL配置方法Named  ACL configuration method
该命令执行后，提示符变为Router(config-std-nacl)#或Router(config-ext-nacl)#。在此提示符下可输入ACL语句。
After this command is executed, the prompt changes to Router(config-std-nacl)# or Router(config-ext-nacl)#. You can enter ACL statements at this prompt.
Named ACL statement format: processing mode condition.
它只比以前的ACL少了前面的“access-list 表号”部分，其它都相同。
Only the access-list part is missing from the previous ACL-everything else is the same.

</div>

---

### 📄 Slide 46：例1 配置标准命名ACLExample 1 configures the standard named ACL

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

要求拒绝来自200.1.1.0/24的数据包通过S0口进入路由器，其它都允许。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

例1 配置标准命名ACLExample 1 configures the standard named ACL
R1
E0
要求拒绝来自200.1.1.0/24的数据包通过S0口进入路由器，其它都允许。
Request TO REJECT THE DATA PACKET from 200.1.1.0/24 entering ROUTER through S0 port, all others are allowed.
S0

</div>

---

### 📄 Slide 47：R1(config)# ip access-list standard list1

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

list1是访问控制列表的名字。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# ip access-list standard list1
R1(config-std-nacl)# deny 200.1.1.0 0.0.0.255
R1(config-std-nacl)# permit any
R1(config-std-nacl)# exit
R1(config)# interface s0
R1(config-if)# ip access-group list1 in
list1是访问控制列表的名字。
list1 is the name of the access control list.

</div>
**💻 配置命令：**

```cisco
R1(config)# ip access-list standard list1
R1(config)# interface s0
```


---

### 📄 Slide 48：命名ACL在修改上略好于一般的ACL，进入一个ACL的模式后，我们可以使用“no”命令删除某一个表项。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

命名ACL在修改上略好于一般的ACL，进入一个ACL的模式后，我们可以使用“no”命令删除某一个表项。
但如果想要调整各表项的次序，还是需要删除整个ACL，再重新输入。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Named ACLs are slightly better at modifying than regular ACLs; once in an ACL mode, we can use the "no" command to delete an entry.
However, if we want to reorder the entries, we still need to delete the entire ACL and re-enter it.

</div>

---

### 📄 Slide 49：例2 配置扩展命名ACLExample 2 configures the standard named ACL

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

禁止内网用户访问地址为60.54.145.21的Web网站。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

例2 配置扩展命名ACLExample 2 configures the standard named ACL
R1
E0
S0
192.168.*.*
192.168.0.1/24
200.1.1.1/24
禁止内网用户访问地址为60.54.145.21的Web网站。
Intranet users are forbidden to access the Web site with address 60.54.145.21.

</div>

---

### 📄 Slide 50：R1(config)# ip access-list extended list2

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1(config)# ip access-list extended list2
R1(config-ext-nacl)# deny tcp 192.168.0.0 0.0.255.255 host 60.54.145.21 eq 80
R1(config-ext-nacl)# permit  ip  any  any
R1(config-ext-nacl)# exit
R1(config)# interface e0
R1(config-if)# ip access-group list2 in

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# ip access-list extended list2
R1(config-ext-nacl)# deny tcp 192.168.0.0 0.0.255.255 host 60.54.145.21 eq 80
R1(config-ext-nacl)# permit  ip  any  any
R1(config-ext-nacl)# exit
R1(config)# interface e0
R1(config-if)# ip access-group list2 in

</div>
**💻 配置命令：**

```cisco
R1(config)# ip access-list extended list2
R1(config)# interface e0
```


---

### 📄 Slide 51：5.6 正确放置访问控制列表5.6 Properly place access control lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

ACL应用在不同接口、不同方向上会有不同效果。
标准ACL不能指定目的地址，一般应放置在离目的地最近的接口上。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.6 正确放置访问控制列表5.6 Properly place access control lists
ACL has different effects in different interfaces and directions.
Standard ACLs cannot specify the destination address and should generally be placed on the interface closest to the destination.

</div>
**💻 配置命令：**

```cisco
Standard ACLs cannot specify the destination address and should generally be placed on the interface closest to the destination.
```


---

### 📄 Slide 52：5.6 正确放置访问控制列表5.6 Properly place access control lists

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

扩展ACL一般应放置在离被拒绝的流量来源最近的地方。
由于一般的通信都需要双向传输信号，所以使用入站检测和出站检测在效果上往往一样，通常使用出站检测时被检查的数据包数量要少一些。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

5.6 正确放置访问控制列表5.6 Properly place access control lists
Extended ACLs should generally be placed closest to the source of rejected traffic.
Due to the bidirectional transmission of signals in general communication, the effect of using inbound and outbound detection is often the same, and the number of examined packets is usually smaller when using outbound detection.

</div>
# 第5章 访问控制列表(ACL) — 命名ACL

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 33：扩展ACL定义后，也需要使用 ip access-group 命令应用在指定接口上才能起作用。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

扩展ACL定义后，也需要使用 ip access-group 命令应用在指定接口上才能起作用。
在每个扩展ACL末尾也有一条默认语句：
它会拒绝所有与前面语句不匹配的数据包。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL定义后，也需要使用 ip access-group 命令应用在指定接口上才能起作用。
Extending the ACL definition also requires the ip access-group command to be applied to the specified interface for it to work.
如：For example
Router(config)# interface e0
Router(config-if)# ip access-group 100 out
There is also a default statement at the end of each extended ACL:
access-list list-num deny ip any any
It rejects all packets that do not match the previous statement.

</div>
**💻 配置命令：**

```cisco
Extending the ACL definition also requires the ip access-group command to be applied to the specified interface for it to work.
Router(config)# interface e0
Router(config-if)# ip access-group 100 out
access-list list-num deny ip any any
```


---

### 📄 Slide 34：扩展ACL配置举例1Example 1 of an extended ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

一个局域网连接在路由器R1的E0口，这个局域网只允许Web通信流量和Ftp通信流量，其它都拒绝。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL配置举例1Example 1 of an extended ACL configuration
R1
E0
A local area network is connected to the E0 port of router R1. This LAN only allows Web traffic and Ftp traffic, and rejects everything else.

</div>

---

### 📄 Slide 35：R1(config)# access-list 100 permit tcp any any eq 80

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：标准FTP协议使用了两个端口，21用于建立FTP连接，20用于数据传输。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 100 permit tcp any any eq 80
R1(config)# access-list 100 permit tcp any any eq 20
R1(config)# access-list 100 permit tcp any any eq 21
R1(config)# interface e0
R1(config-if)# ip access-group 100 out
Note: The standard FTP protocol uses two ports, 21 for FTP connection establishment and 20 for data transfer.

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 100 permit tcp any any eq 80
R1(config)# access-list 100 permit tcp any any eq 20
R1(config)# access-list 100 permit tcp any any eq 21
R1(config)# interface e0
```


---

### 📄 Slide 36：说明：Notes

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：Notes
例1的配置将会极大限制局域网和外网间的应用，它会拒绝除Web和Ftp外的所有应用（包括ICMP、DNS、电子邮件等），也会拒绝那些没有使用标准端口的Web和Ftp应用。
在实际应用中，我们通常只对那些可能有害的访问作出拒绝限制，或者限制用户访问某些有害的站点或服务。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

说明：Notes
The configuration in Example 1 will severely restrict applications between the local and public network, rejecting all applications except Web and Ftp (ICMP, DNS, email, etc.) and rejecting Web and Ftp applications that do not use a standard port.
In practice, we usually restrict access to potentially harmful sites or services, or restrict access to harmful sites or services.

</div>

---

### 📄 Slide 37：扩展ACL配置举例2Example 2 of an extended ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1是局域网和外网的边界路由器，禁止外网用户用Telnet远程登录本路由器。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL配置举例2Example 2 of an extended ACL configuration
R1
E0
R1 is the border router between the LAN and the external network, and the external network users are forbidden to remotely login to this router with Telnet.
S0
192.168.*.*
192.168.0.1/24
200.1.1.1/24

</div>

---

### 📄 Slide 38：R1(config)# access-list 100 deny tcp any host 200.1.1.1 eq 23

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

说明：这里使用了禁止对两个接口进行Telnet的数据包进入S0口的方法阻断来自外网的Telnet请求。
由于对E0口没有限制，所以它不影响来自内网的Telnet请求。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 100 deny tcp any host 200.1.1.1 eq 23
R1(config)# access-list 100 deny tcp any host 192.168.0.1 eq 23
R1(config)# access-list 100 permit ip any any
R1(config)# interface s0
R1(config-if)# ip access-group 100 in
Note: This uses the method of blocking the Telnet request from the external network by forbidding the Telnet packets to the two interfaces to enter the S0 port.
Since there is no restriction on the E0 port, it does not affect Telnet requests from the internal network.

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 100 deny tcp any host 200.1.1.1 eq 23
R1(config)# access-list 100 deny tcp any host 192.168.0.1 eq 23
R1(config)# access-list 100 permit ip any any
R1(config)# interface s0
Note: This uses the method of blocking the Telnet request from the external network by forbidding the Telnet packets to the two interfaces to enter the S0 port.
```


---

### 📄 Slide 39：扩展ACL配置举例3Example 3 of an extended ACL configuration

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1是局域网和外网的边界路由器，60.54.145.21是一个有害的Web网站，禁止内网用户访问该网站。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

扩展ACL配置举例3Example 3 of an extended ACL configuration
R1
E0
R1是局域网和外网的边界路由器，60.54.145.21是一个有害的Web网站，禁止内网用户访问该网站。
R1 is the border router between local area network and external network, 60.54.145.21 is a harmful Web site, and internal network users are forbidden to access the site.
S0
192.168.*.*
192.168.0.1/24
200.1.1.1/24

</div>

---

### 📄 Slide 40：R1(config)# access-list 100 deny tcp 192.168.0.0 0.0.0.255 host 60.54.145.21 eq ...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

R1(config)# access-list 100 deny tcp 192.168.0.0 0.0.0.255 host 60.54.145.21 eq 80
R1(config)# access-list 100 permit ip any any
R1(config)# interface e0
R1(config-if)# ip access-group 100 in

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

R1(config)# access-list 100 deny tcp 192.168.0.0 0.0.0.255 host 60.54.145.21 eq 80
R1(config)# access-list 100 permit ip any any
R1(config)# interface e0
R1(config-if)# ip access-group 100 in

</div>
**💻 配置命令：**

```cisco
R1(config)# access-list 100 deny tcp 192.168.0.0 0.0.0.255 host 60.54.145.21 eq 80
R1(config)# access-list 100 permit ip any any
R1(config)# interface e0
```

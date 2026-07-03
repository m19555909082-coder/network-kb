# 第6章 网络地址转换(NAT) — 动态NAT配置

> 8 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 17：例：For example

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

例：For example
Router(config)# ip nat inside source static 192.168.1.1 200.10.1.5
Router(config)# ip nat inside source static 192.168.1.2 200.10.1.6
Router(config)# interface e0
Router(config-if)# ip nat inside
Router(config-if)# interface s0
Router(config-if)# ip nat outside

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

例：For example
Router(config)# ip nat inside source static 192.168.1.1 200.10.1.5
Router(config)# ip nat inside source static 192.168.1.2 200.10.1.6
Router(config)# interface e0
Router(config-if)# ip nat inside
Router(config-if)# interface s0
Router(config-if)# ip nat outside

</div>
**💻 配置命令：**

```cisco
Router(config)# ip nat inside source static 192.168.1.1 200.10.1.5
Router(config)# ip nat inside source static 192.168.1.2 200.10.1.6
Router(config)# interface e0
Router(config-if)# ip nat inside
Router(config-if)# interface s0
Router(config-if)# ip nat outside
```


---

### 📄 Slide 18：配置完成后，从外网来看，PC1的IP地址是200.10.1.5，PC2的IP地址是200.10.1.6，各计算机都可用此IP地址访问PC1和PC2。

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置完成后，从外网来看，PC1的IP地址是200.10.1.5，PC2的IP地址是200.10.1.6，各计算机都可用此IP地址访问PC1和PC2。
用show ip nat translation命令可查看活跃的转换。（静态NAT始终是活跃的）
用show ip nat statistics命令可查看转换的统计信息。
静态NAT是一直存在的，管理员可以用“no”命令删除静态NAT条目。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

配置完成后，从外网来看，PC1的IP地址是200.10.1.5，PC2的IP地址是200.10.1.6，各计算机都可用此IP地址访问PC1和PC2。
After the configuration is completed, the IP address of PC1 is 200.10.1.5, and the IP address of PC2 is 200.10.1.6. Each computer can use this IP address to access PC1 and PC2.
用show ip nat translation命令可查看活跃的转换。（静态NAT始终是活跃的）
Use the show ip nat translation command to see the active translation. (Static Nats are always active)
用show ip nat statistics命令可查看转换的统计信息。
Use the show ip nat statistics command to see the statistics of the transformations.
Static Nats are always present, and administrators can delete static NAT entries with the "no" command.

</div>

---

### 📄 Slide 19：NAT池（动态NAT）

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

NAT池（动态NAT）
主要工作：建立一个IP地址池。设定被转换的IP地址范围。建立转换关系。设定转换的入口和出口。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT池（动态NAT）
192.168.1.1
192.168.1.2
NAT池
Main work: Establish a pool of IP addresses. Specifies the range of IP addresses to be translated. Establish the transition relationship. Specifies the entry and exit points for the transformation.

</div>

---

### 📄 Slide 20：1、建立IP地址池   1. Establish a pool of IP addresses

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

例：建立一个地址范围为200.1.1.1~200.1.1.10/24的IP地址池。
P1是地址池的名字。
说明：地址池中的地址应该是经过注册的合法IP地址。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

1、建立IP地址池   1. Establish a pool of IP addresses
Router(config)# ip nat pool 地址池名字 起始IP 结束IP netmask 子网掩码
例：建立一个地址范围为200.1.1.1~200.1.1.10/24的IP地址池。
Example: Create a pool of IP addresses in the range 200.1.1.1 to 200.1.1.10/24.
Router(config)# ip nat pool P1 200.1.1.1 200.1.1.10 netmask 255.255.255.0
P1 is the name of the address pool.
Note: The address in the address pool should be a registered legal IP address.

</div>
**💻 配置命令：**

```cisco
1、建立IP地址池   1. Establish a pool of IP addresses
Router(config)# ip nat pool 地址池名字 起始IP 结束IP netmask 子网掩码
Example: Create a pool of IP addresses in the range 200.1.1.1 to 200.1.1.10/24.
Router(config)# ip nat pool P1 200.1.1.1 200.1.1.10 netmask 255.255.255.0
Note: The address in the address pool should be a registered legal IP address.
```


---

### 📄 Slide 21：2、设定被转换的地址范围：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

2、设定被转换的地址范围：
被转换的地址范围使用标准访问控制列表进行定义。
比如：被转换的地址是形如192.168.*.*/24的地址，则可定义：
说明：这里定义的ACL不是用于数据过滤的，它只是用于指定参与NAT转换的私有地址范围的。所以，我们不必把它用在一个接口上。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

2. Set the range of addresses to be converted:
The range of addresses to be translated is defined using standard access control lists.
比如：被转换的地址是形如192.168.*.*/24的地址，则可定义：
For example, if the translated address is an address of the form 192.168.*.*/24, you can define:
Router(config)# access-list 1 permit 192.168.0.0 0.0.255.255
Note: The ACL defined here is not used for data filtering, it is only used to specify the private address range participating in the NAT translation. So, we don't have to use it for an interface.

</div>
**💻 配置命令：**

```cisco
Router(config)# access-list 1 permit 192.168.0.0 0.0.255.255
```


---

### 📄 Slide 22：3、建立被转换的地址和地址池间的关系：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

3、建立被转换的地址和地址池间的关系：
例：把1号ACL定义的地址与名为P1的地址池建立NAT转换关系。
说明：经此定义后，每当路由器收到一个数据包，就检测它的源地址，如果和1号ACL相匹配，就使用P1中的地址进行NAT转换。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

3. Establish the relationship between the translated address and the address pool:
Router(config)# ip nat inside source list ACL表号 pool 地址池名字
Example: Establish a NAT translation relationship between the address defined by ACL # 1 and the address pool named P1.
Router(config)# ip nat inside source list 1 pool P1
Note: With this definition, each time a router receives a packet, it checks its source address, and if it matches the ACL number 1, it uses the address in P1 for NAT translation.

</div>
**💻 配置命令：**

```cisco
Router(config)# ip nat inside source list ACL表号 pool 地址池名字
Router(config)# ip nat inside source list 1 pool P1
```


---

### 📄 Slide 23：4、指定NAT转换的入口和出口：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

4、指定NAT转换的入口和出口：
说明：每种NAT都需要指定内部接口和外部接口。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

4. Specify the ingress and egress of the NAT translation:
Router(config)# interface 内部接口
Router(config-if)# ip nat inside
Router(config)# interface 外部接口
Router(config-if)# ip nat outside
Note: Each NAT needs to specify internal and external interfaces.

</div>
**💻 配置命令：**

```cisco
Router(config)# interface 内部接口
Router(config-if)# ip nat inside
Router(config)# interface 外部接口
Router(config-if)# ip nat outside
```


---

### 📄 Slide 24：例：

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

例：
内部网络地址为10.0.0.0/8，注册的IP地址是200.1.1.1~200.1.1.254，用这些地址为内网的各个访问提供NAT翻译。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

NAT池
200.1.1.1~200.1.1.254/24
10.0.0.0/8
内部网络地址为10.0.0.0/8，注册的IP地址是200.1.1.1~200.1.1.254，用这些地址为内网的各个访问提供NAT翻译。
The internal network address is 10.0.0.0/8, and the registered IP address is 200.1.1.1~200.1.1.254. These addresses are used to provide NAT translation for each access to the internal network.
R1
f0/0
s0/0

</div>
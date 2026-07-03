# 第3章 子网与路由 — 单臂路由VLAN间通信

> 5 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 49：路由器接口显示命令The router interface displays commands

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

(表示物理层协议正常) (表示数据链路层协议正常)
(表示物理层协议正常) (表示数据链路层协议不正常)
(表示物理层协议不正常)
(表示从管理上将该接口处于关闭状态)

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

路由器接口显示命令The router interface displays commands
   Red-Giant#show interfaces serial 0
serial0 is up, line protocol is up
serial0 is up, line protocol is down
serial0 is down, line protocol is down
serial0 is administratively down, line protocol is down

</div>
**💻 配置命令：**

```cisco
路由器接口显示命令The router interface displays commands
```


---

### 📄 Slide 50：配置文件的管理

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

配置文件的管理
将当前运行参数保存到flash 中用于系统初始化时初始化参数。
擦除初始配置文件，注意不能用erase flash命令

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Management of configuration files
保存文件:save file
Save the current running parameters to flash to initialize parameters when the system is initialized.
Router#copy running-config startup-config
Router#write memory
Router#write
Router#show running-config。
Router#erase startup-config
擦除初始配置文件，注意不能用erase flash命令
erase the initial configuration file.Note that the erase flash command is not used

</div>

---

### 📄 Slide 51：项目：使用单臂路由实现不同VLAN通讯Project: Using single-arm routing to achieve different VLAN ...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

王先生所在公司楼上是销售部，由于楼上销售部机位不够，因此销售部中有部分员工计算机不得不连接在客户服务部网交换机端口上。
由于二个部门共享一台交换机办公，为避免二个部门之间干扰，保护客户服务部客户信息资源安全，需要把两个部门计算机分隔开，形成两个互不连通、互相不干扰安全网络。
公司的网络中心，按照部门划分出销售部和服务部二个Vlan。现在公司希望使用路由设备，连接两个Vlan，实现二个不同Vlan间安全连通。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目：使用单臂路由实现不同VLAN通讯Project: Using single-arm routing to achieve different VLAN communication
【任务描述】task description
Mr. Wang's company upstairs is the sales department, because the upstairs sales department is not enough, so some staff computers in the sales department have to connect to the customer service network switch port.
Since the two departments share a switch office, in order to avoid interference between the two departments and protect the security of customer service department customer information resources, it is necessary to separate the computers of the two departments to form two disconnected and non-interference security networks.
The company's network center, according to the division of the department of sales and service two Vlan. Now the company wants to use routing equipment to connect two VLans and achieve secure connectivity between two different VLans.

</div>

---

### 📄 Slide 52：项目：使用单臂路由实现不同VLAN通讯Project: Using single-arm routing to achieve different VLAN ...

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

【任务目标】：task object
单臂路由技术。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

项目：使用单臂路由实现不同VLAN通讯Project: Using single-arm routing to achieve different VLAN communication
【任务目标】：task object
single-arm routing technology

</div>

---

### 📄 Slide 53：谢 谢!

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

谢 谢!

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

谢 谢!
THANKS

</div>
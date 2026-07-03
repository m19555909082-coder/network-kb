# 第1章 VLAN技术 — VLAN配置命令—Access端口

> 3 张幻灯片 | 中英双语完整保留

---


---

### 📄 Slide 5：创建VLAN100，将它命名为test的例子

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

创建VLAN100，将它命名为test的例子

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

创建VLAN100，将它命名为test的例子
Create VLAN100 and name it the test example
Switch #  configure terminal
Switch(config) #  vlan 100
把fastethernet 0/10作为access口加入了VLAN100
The fastethernet 0/10 is added to the VLAN100 as an access port
Switch(config) #  interface fastethernet0/10
Switch(config-if) # switchport access vlan 100
配置Port VLAN-Access(1)Configuring Port VLAN-Access(1)

</div>
**💻 配置命令：**

```cisco
Switch(config) #  vlan 100
Switch(config) #  interface fastethernet0/10
Switch(config-if) # switchport access vlan 100
```


---

### 📄 Slide 6：将一组接口加入某一个VLAN

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

将一组接口加入某一个VLAN
注：连续接口 0/1-10，中间使用空格分离;
不连续多个接口，中间用逗号隔开；
如果使用模块，一定要写明模块编号。

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

Add a set of interfaces to a VLAN
Switch(config)#interface range fastethernet 0/1-10，0/15，0/20
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#no shutdown
注：连续接口 0/1-10，中间使用空格分离;
Note: continuous interface 0/1-10, use space separation in the middle;
Discontinuous multiple interfaces, separated by commas;
If using a module, be sure to specify the module number.
配置Port VLAN-Access(2)
Configuring Port VLAN-Access(2)

</div>
**💻 配置命令：**

```cisco
Switch(config)#interface range fastethernet 0/1-10，0/15，0/20
Switch(config-if-range)#switchport access vlan 20
Switch(config-if-range)#no shutdown
Note: continuous interface 0/1-10, use space separation in the middle;
```


---

### 📄 Slide 7：VLAN相关配置

<div class="bilingual-cn" markdown>

**🇨🇳 中文**

VLAN相关配置
如果批量将端口加入VLAN，可用关键字range（见端口加入VLAN30配置），如果只加单一接口（见端口加入VLAN40配置）

</div>

<div class="bilingual-en" markdown>

**🇬🇧 English**

VLAN相关配置
VLAN30
VLAN40
Switch(config)#interface range fastethernet 0/1-2
Switch(config-if-range)#switchport access vlan 30
Switch(config-if)#exit
Switch(config)#interface fastethernet 0/3
Switch(config-if)#switchport access vlan 40
Switch(config-if)#exit
Switch(config)#interface fastethernet 0/4
Switch(config-if)#switchport access vlan 40
Switch(config-if)#exit
如果批量将端口加入VLAN，可用关键字range（见端口加入VLAN30配置），如果只加单一接口（见端口加入VLAN40配置）
If multiple ports are added to the VLAN , use the keyword range (see Port Join VLAN30 configuration). If only a single interface is added (see Port Join VLAN40 configuration).
VLAN related configuration

</div>
**💻 配置命令：**

```cisco
Switch(config)#interface range fastethernet 0/1-2
Switch(config-if-range)#switchport access vlan 30
Switch(config-if)#exit
Switch(config)#interface fastethernet 0/3
Switch(config-if)#switchport access vlan 40
Switch(config-if)#exit
Switch(config)#interface fastethernet 0/4
Switch(config-if)#switchport access vlan 40
Switch(config-if)#exit
If multiple ports are added to the VLAN , use the keyword range (see Port Join VLAN30 configuration). If only a single interface is added (see Port Join VLAN40 configuration).
VLAN related configuration
```

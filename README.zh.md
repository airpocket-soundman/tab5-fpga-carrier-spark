# Tab5 FPGA Carrier — Spark

> **主电源修订中，禁止下单。当前公开的原理图、PCB及仿真采用旧SW3（仅停止FPGA供电）配置。用于同时接通/切断Tab5和FPGA外部12V供电的自锁主电源尚未反映。Tab5内置电池运行不在切断范围内。**

[日本語](README.ja.md) · **中文** · [English](README.md)

**[日中英切换的设计与仿真页面](https://airpocket-soundman.github.io/tab5-fpga-carrier-spark/)**

两款 LCSC 优先的共用载板连接 M5Stack Tab5 与 Tang Primer20K Core，用于**128MB外部DDR3 RAM存储、通用GPU及图形加速器研究**。DDR3是通过专用API显式读写的外部数据区，不会自动扩展Tab5的系统主存。Linux存储实验与图形实验使用不同的软件和FPGA比特流。

截至2026-10-26，处于工程评审和EasyEDA Spark参赛准备阶段。物理通信、DDR3初始化、绘图性能、外壳配合及制造批准仍待确认。尚未报名、申请材料、下单或付款。

| | 完整版 | A型经济版 |
| --- | --- | --- |
| PCB |125×78mm，4层 |99×78mm，4层 |
| 功能 |稳压12V圆孔输入、USB PD12V、HDMI |保留相同功能 |
| 电源 |TPS5430、Bourns15µH、TLV1117LV33 |TPS5430、COILMX15µH、XC6206 |
| PCBA报价候选 |103个器件、45行 |105个器件、45行 |
| EasyEDA内实际求解 |172个条件 |187个条件 |
| 电源电压在模型范围内 |6/6，不含局部LDO动态 |19/21，包括2项失败的严苛灵敏度测试 |
| PCB DRC |0项违规 |0项违规 |
| 原理图 |0项致命错误，13项警告待分类 |相同 |

经济版以板面积和器件选型争取降低成本，实际差价需报价确认。其反馈电阻网络增加了器件数量。

## 设计文件

- [完整版嘉立创EDA专业版工程](hardware/full/spark-lcsc-priority-review.epro2) · [BoM](hardware/full/bom.csv) · [制造评审资料](hardware/full)
- [A型经济版嘉立创EDA专业版工程](hardware/lite-a/spark-lite-a-lcsc-review.epro2) · [BoM](hardware/lite-a/bom.csv) · [制造评审资料](hardware/lite-a)
- [完整版EasyEDA仿真记录](simulation/full) · [A型EasyEDA仿真记录](simulation/lite-a)

`.epro2`包含原理图、PCB及工程库。BoM/CPL、Gerber和装配图是报价与评审候选，尚未获准直接投产。

## 采购、装配与运行条件

所有计划安装的板上器件均已选定LCSC编号。DC插座C381116、背面Tab5排针C56496、ARM排针C124375和停止开关C692500也纳入波峰焊报价；若厂商不接受装配，则从LCSC单独采购并手工焊接。仅在LCSC没有合适器件时才使用秋月替代。目录显示支持并不等同于具体订单获批。

短路帽C5305单独包装，初次不安装。Tab5和Core由用户单独购买，不计入支持申请。不能预期Spark通常支持LCSC单独采购。外壳、螺钉和隔柱需机械确认后确定。

初期通信为**1MHz、弱驱动/SLOW、DATA建立和保持时间各≥250ns、DIR等待≥500ns**。150个通信条件中，接收端150/150在电压范围内，而发送端仅60/150，快速边沿的限制仍然存在。1MHz周期模型4/4通过，不证明10–40MHz稳定运行或实机DMA已完成。

A型局部3.3V正常负载≤10mA，不对外供电；50mA突变等2项超出±5%的案例也已公开。输入仅使用稳压12V，初次评估以Core正常0.5A为基准。

仿真使用在EasyEDA API Gateway内运行的官方NGspice46 WASM及分析等效电路，不代表完整制造原理图的自动SPICE仿真、热验证、PD协商、HDMI认证或实机性能。

公开仓库不表示已报名、申请材料或入选。包括设计流程在内的参赛资格及完整产品/外壳要求仍需主办方确认。注册不会自动打款，材料支持需设计、报价审核和优惠券批准。

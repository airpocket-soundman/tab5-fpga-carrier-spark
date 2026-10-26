# Tab5 FPGA Carrier — Spark

**r4：SMT仅在正面。省略主电源开关和旧FPGA停止SW3。J3从LCSC单独购买并手焊。PoC下单文件已完成。厂商常规装配预览、库存与DFM受理，以及制造后实机验证分别进行。**

[日本語](README.ja.md) · **中文** · [English](README.md)

[日中英切换的设计与仿真页面](https://airpocket-soundman.github.io/tab5-fpga-carrier-spark/)

连接M5Stack Tab5与Tang Primer20K Core的四层载板，用于FPGA侧128MB DDR3的**RAM存储、通用GPU及图形加速研究**。DDR3是通过专用API显式访问的数据区，不会自动扩展Tab5系统主存。Linux与图形实验使用不同软件和FPGA比特流。

| | 完整版 | A型经济版 |
| --- | --- | --- |
| 载板 |125×78mm、四层 |99×78mm、四层 |
| 接口 |稳压12V圆孔输入、USB PD12V、HDMI |相同 |
| 电源器件 |TPS5430、Bourns15µH、TLV1117LV33 |TPS5430、COILMX15µH、XC6206 |
| PCBA报价候选 |101器件、43行 |103器件、43行 |
| 手工焊接 |J3/C56496，不在PCBA BOM/CPL内 |相同 |
| SMT装配面 |仅正面 |仅正面 |
| 嘉立创EDA内完成求解 |207条件 |221条件 |
| 电源数值范围内 |6/6，不含局部LDO动态响应 |18/20，含两项超限敏感性试验 |
| HDMI工程判据 |35/35 |35/35 |
| PCB DRC |0违规 |0违规 |
| 原理图 |0致命错误、0错误，13项警告已全部分类、未分类0 |相同 |

完成求解与满足电路条件是不同指标。库存、装配受理、旋转、实物插合及实机运行仍待确认。PoC下单文件已经完成。尚未报名、申请材料、提交制造订单或付款。

## 文件

- [完整版嘉立创EDA专业版工程](hardware/full/spark-lcsc-priority-review.epro2) · [BoM](hardware/full/bom.csv) · [Gerber/PCBA BOM/CPL/装配图](hardware/full)
- [A型嘉立创EDA专业版工程](hardware/lite-a/spark-lite-a-lcsc-review.epro2) · [BoM](hardware/lite-a/bom.csv) · [Gerber/PCBA BOM/CPL/装配图](hardware/lite-a)
- [完整版仿真](simulation/full) · [A型仿真](simulation/lite-a) · [方法与限制](simulation/README.md)
- [装配要求](hardware/ASSEMBLY.md) · [r4修订](hardware/MAIN_POWER_REVISION.md) · [文件哈希](manifest.json)

`.epro2`包含原理图、PCB及库。CPL已修正为JLCPCB官方封装坐标系，应使用随附CPL，不要从原始库旋转值重新生成。PCBA报价时配套使用`jlc-bom.csv`与`jlc-cpl.csv`，两者均不含J3。总体`bom.csv`区分并列出手焊J3。

## 采购与运行条件

器件优先从LCSC采购。**J3/C56496单独采购并手焊**，保留朝向背面的插合方向。用户在背面安装THT排针不要求背面SMT装配。J2/J4/J5要求PCBA，包括J5的通孔外壳焊片。J1/C381116与JP1/C124375的THT装配需厂商确认。不接受时，购买相同适配LCSC器件并手焊，仅在LCSC无合适器件时考虑秋月电子。单面SMT不保证所有器件均获装配受理。

SW3与r3主电源电路均不存在。外部电源有效时，载板既有电源电路运行；板上不具备统一切断外部电源或仅停止FPGA供电的开关。保留复位、用户按钮与BUS ARM。C5305短路帽单独包装、初次不安装。Tab5与Core由用户购买，不计入PCBA及支持申请。

初始通信采用**1MHz、弱驱动/SLOW、DATA建立及保持各至少250ns、DIR切换至少500ns**。每款150项通信条件中，接收端150/150、发送端60/150满足电压范围，保留快速边沿失败案例。1MHz周期模型4/4通过，不证明10–40MHz稳定运行、实机DMA或GPU性能。

使用稳压12V，以Core正常0.5A作为初次评估条件。A型局部3.3V正常负载不超过10mA，不向外部供电。50mA突变及慢LDO环路两项敏感性试验超出±5%。

HDMI采用耦合RLGC线、假设Thevenin驱动源及理想接收端，不含线缆。中心100mV及0.4UI窗口为工程判据，不是HDMI认证掩模。厂商IBIS、认证及实机视频输出尚未验证。

仿真通过嘉立创EDA API Gateway在客户端内执行官方NGspice46 WASM等效电路，不代表完整制造原理图的自动SPICE、实际开关、热或PD协商验证。

## Spark

本仓库准备申请[国际EasyEDA Spark](https://oshwlab.com/activities/easyeda-spark-2026?tab=2#P1)。设计流程资格、完整产品要求及支持批准仍需主办方确认。注册不会自动发放开发资金，材料支持须经设计和报价审核及优惠券批准。LCSC单独采购支持尚未确认。尚未报名、申请材料、下单或付款。

Copyright2026 airpocket-soundman。[MIT](LICENSE)及[第三方许可声明](THIRD_PARTY_NOTICES.md)。

## 制造条件及警告复核

PoC制造条件为**JLC04161H-7628、四层、板厚1.6mm、外层铜35µm、内层15.2µm、εr=4.4**。完整设置见各款order-profile JSON。保持仅正面SMT，J3由LCSC单独采购并手焊。

原理图13项警告已全部分类：预留PD_PG/TAB_SCL/TAB_SDA网络3项，同名VBUS_PD/GND重复2项，定制库销售属性4组，J4的94个有意不使用引脚4组。致命错误0、错误0、未分类0。未放宽DRC规则或抑制警告，按电路及引脚核对结果接受用于PoC，并保留复核记录。

## PoC下单文件

- [完整版 ZIP](hardware/full/full-r4-poc-order.zip)
- [A型经济版 ZIP](hardware/lite-a/lite-a-r4-poc-order.zip)

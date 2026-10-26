# Main-power revision / 主電源改訂 / 主电源修订

## 日本語

主電源改訂中・発注不可。公開中の回路・PCB・解析は旧SW3（FPGA専用停止）構成です。外部12VをTab5とFPGAへ一括ON/OFFするオルタネート主電源は未反映です。Tab5の内蔵バッテリー動作は停止対象に含めません。

USB PDとDCジャックの保護・OR合流後、Tab5 HVINとCore降圧入力の分岐前を制御する仕様です。PD交渉回路は上流に残し、リセット・ユーザーボタン・BUS ARMは保持します。旧SW3 C692500は新仕様の部品ではありません。

新部品の保護協調、接点・負荷定格、突入、電圧降下、温度、Tab5バッテリー動作時の逆給電、電源断・再投入の検証が必要です。部品選定・基板変更・EasyEDA反映・同環境での過渡解析が終わるまで、新版の製造データは公開しません。

BoMの実装列は旧版の記録です。J2/J4/J5はPCBA必須、一般SMDはPCBA予定、J1/J3/JP1はTHT実装の業者確認待ちです。旧SW3は廃止対象と表示します。手はんだ品もLCSC調達を優先し、適合品がLCSCにない場合のみ秋月電子を検討します。Extended登録やLCSC在庫だけで、個別注文の実装が承認されるわけではありません。

## 中文

主电源修订中，禁止下单。当前公开的原理图、PCB及仿真采用旧SW3（仅停止FPGA供电）配置。用于同时接通/切断Tab5和FPGA外部12V供电的自锁主电源尚未反映。Tab5内置电池运行不在切断范围内。

在USB PD和DC插座的保护及OR汇合之后、Tab5 HVIN和Core降压输入分支之前控制供电；PD协商电路保留在上游。复位、用户按钮及BUS ARM保持不变。旧SW3 C692500将移除。

仍需完成器件和保护协调、额定值、浪涌、电压降、温升、电池运行时的反向供电及断电/重启验证。新版制造文件须在PCB、嘉立创EDA原生数据和实际过渡仿真完成后发布。

BoM装配列描述旧版：J2/J4/J5要求PCBA；一般SMD计划PCBA；J1/J3/JP1的THT装配待厂商确认；旧SW3标为待移除。手工焊接器件也优先从LCSC采购，只有无合适器件时才考虑秋月电子。Extended或LCSC库存不等于具体订单已获装配批准。

## English

Main-power revision in progress — do not fabricate. Published schematics, PCBs and simulations use the old SW3 FPGA-only shutdown circuit. The latching main switch that cuts external12V to both Tab5 and FPGA is not yet implemented in these files. Tab5 battery operation remains outside the switch scope.

Control power after the protected DC/PD OR node and before the split to Tab5 HVIN and the Core converter. Keep PD negotiation upstream. Retain reset, user button and BUS ARM. Remove the old SW3 C692500 function.

Protection coordination, ratings, inrush, voltage drop, temperature, reverse feeding with Tab5 on battery, shutdown and restart remain to be validated. New manufacturing files require a revised PCB, native EasyEDA data and actual transient simulation.

BOM assembly labels describe the legacy revision: J2/J4/J5 require PCBA; ordinary SMD parts are planned for PCBA; J1/J3/JP1 need supplier THT approval; old SW3 is marked for removal. Hand-solder parts also use LCSC first, with Akizuki only when no suitable LCSC part exists. Extended listing or LCSC stock does not approve a specific assembly order.

# r4: single-sided SMT / 片面SMT / 单面SMT

2026-10-26

## 日本語

両面SMTをやめるユーザー指示により、主電源スイッチを省略するr4へ変更しました。旧FPGA専用停止SW3も除去しました。r3で検討したU11/R53〜R58/C25/C26はr4にはありません。これは未実装の主電源スイッチを残した版ではなく、スイッチ機能を省く版です。

フル125×78mm、廉価版A99×78mm、4層、HDMI・USB PD12V・バレル12V、リセット・ユーザーボタン・BUS ARMを維持。SMTは全て表面です。外部給電が有効なら既存電源回路が動作し、基板上に外部給電の一括切断やFPGA専用停止スイッチはありません。Tab5内蔵バッテリーの停止制御もありません。

J3/C56496はLCSC別購入・手はんだ。PCBA用BOMとCPLの両方から除外し、裏向き嵌合方向は維持します。J1/JP1のTHT実装可否、部品在庫・回転・DFM・実物嵌合は業者と確認が必要です。

掲載する解析はr4の等価回路をEasyEDA内で再計算した記録です。主電源スイッチが存在しないため、そのON/OFF・突入や遮断の検証結果として扱いません。PoC発注用データは完成しています。業者の通常実装プレビュー・在庫・DFM受理と、製造後の実機検証は別途行います。Spark支援の受理は未完了です。

## 中文

按用户要求取消双面SMT，r4省略主电源开关，并移除旧的仅停止FPGA供电的SW3。r3中的U11/R53–R58/C25/C26不属于r4。此版明确省略开关功能，并非保留待实现开关的版本。

完整版125×78mm、A型99×78mm、四层，保留HDMI、USB PD12V、圆孔12V、复位、用户按钮和BUS ARM。SMT均在正面。外部电源有效时既有电源电路运行，无板上统一断电或仅关闭FPGA的开关，也不控制Tab5内置电池关机。

J3/C56496从LCSC单独购买并手焊，从PCBA BOM和CPL同时排除，保留朝向背面的插合方向。J1/JP1的THT受理、库存、旋转、DFM及实物插合须确认。

发布记录是r4等效电路在嘉立创EDA内的重新计算。不存在主电源开关，因此不得将其作为开关ON/OFF、浪涌或切断的验证。PoC下单文件已完成。厂商常规装配预览、库存、DFM受理及制造后实机验证分别进行。Spark支持尚未获批准。

## English

The user requested single-sided SMT and permitted omission of the main-power switch. r4 omits it and removes the old FPGA-only shutdown SW3. U11/R53–R58/C25/C26 from r3 are absent. This revision deliberately omits the switch function.

Full125×78mm and Lite A99×78mm retain four layers, HDMI, USB PD12V, barrel12V, reset, user button and BUS ARM. All SMT is top-side. The existing power circuitry runs while external power is present. There is no board-mounted main or FPGA-only shutdown switch, and no Tab5 battery shutdown control.

J3/C56496 is separately purchased from LCSC and hand soldered, excluded from both PCBA BOM and CPL while retaining its bottom-facing mating orientation. J1/JP1 THT acceptance, stock, rotations, DFM and physical mating require review.

Published analytical records are r4 equivalent circuits recalculated inside EasyEDA. They do not validate main-switch operation, switched inrush or disconnection, because that switch is absent. PoC order files are complete. Normal supplier placement preview, stock and DFM acceptance, followed by post-manufacturing hardware validation, remain separate steps. Spark support acceptance is pending.

## Manufacturing and warning review

PoC profile: JLC04161H-7628, four layers,1.6mm, outer35µm/inner15.2µm,εr4.4. The supplied CPL is corrected to the official JLCPCB footprint frame.

Schematic fatal/errors0, warnings13 reviewed, unclassified0: reserved nets3, identical labels2, custom-library supplier metadata4 groups, unused94 J4 pins4 groups. Warnings are documented and accepted for PoC without suppressing DRC checks.

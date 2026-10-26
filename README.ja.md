# Tab5 FPGA Carrier — Spark

**r4：SMTは表面のみ。主電源スイッチと旧FPGA停止SW3は省略。J3はLCSC別購入・手はんだ。PoC発注用データは完成。業者の通常実装プレビュー・在庫・DFM受理と、製造後の実機検証は別途行います。**

**日本語** · [中文](README.zh.md) · [English](README.md)

[日中英切替の設計・解析ページ](https://airpocket-soundman.github.io/tab5-fpga-carrier-spark/)

M5Stack Tab5とTang Primer20K Coreを接続する4層キャリアです。FPGA側128MB DDR3の**RAMストレージ利用、汎用GPU、グラフィックアクセラレータの研究**を想定しています。DDR3は専用APIで明示的にアクセスするデータ領域であり、Tab5の通常RAMが自動で増える構成ではありません。Linuxとグラフィックスは別ソフト・別ビットストリームで使用します。

| | フル版 | 廉価版A |
| --- | --- | --- |
| 基板 |125×78mm・4層 |99×78mm・4層 |
| 機能 |安定化12Vバレル・USB PD12V・HDMI |同じ機能を保持 |
| 電源部品 |TPS5430・Bourns15µH・TLV1117LV33 |TPS5430・COILMX15µH・XC6206 |
| PCBA見積候補 |101部品・43行 |103部品・43行 |
| 手はんだ |J3/C56496。PCBA BOM/CPLから除外 |同じ |
| SMT実装面 |表面のみ |表面のみ |
| EasyEDA内で計算完了 |207条件 |221条件 |
| 電源の数値範囲内 |6/6。局所LDO動特性は対象外 |18/20。厳しい感度試験の範囲外2件を含む |
| HDMI工学的判定条件 |35/35 |35/35 |
| PCB DRC |違反0 |違反0 |
| 回路図 |致命的エラー0・エラー0、警告13件は全件分類済み・未分類0 |同じ |

計算完了と回路条件への合格は別の指標です。部品在庫、実装受理、回転、実物嵌合、実機動作の確認は残っています。PoC発注用データは完成しています。応募・材料申請・注文・支払いは未実施です。

## データ

- [フル版EasyEDA Pro](hardware/full/spark-lcsc-priority-review.epro2)・[BoM](hardware/full/bom.csv)・[Gerber/PCBA BOM/CPL/組立図](hardware/full)
- [廉価版A EasyEDA Pro](hardware/lite-a/spark-lite-a-lcsc-review.epro2)・[BoM](hardware/lite-a/bom.csv)・[Gerber/PCBA BOM/CPL/組立図](hardware/lite-a)
- [フル版EasyEDA解析](simulation/full)・[廉価版A EasyEDA解析](simulation/lite-a)・[解析手法と制約](simulation/README.md)
- [実装指示](hardware/ASSEMBLY.md)・[r4改訂](hardware/MAIN_POWER_REVISION.md)・[ファイルハッシュ](manifest.json)

`.epro2`には回路図・PCB・ライブラリを収録。CPLはJLCPCB公式フットプリントの座標系へ補正済みです。生のライブラリ回転から再生成せず、同梱CPLを使用してください。PCBA見積もりには同梱の`jlc-bom.csv`と`jlc-cpl.csv`を組で使用してください。両方ともJ3を除外しています。全体の`bom.csv`では手はんだJ3も区別して記載します。

## 調達・動作条件

選定部品はLCSC優先。**J3/C56496はLCSC別購入・手はんだ**で、裏向きの嵌合方向を維持します。ユーザーが裏面にTHTヘッダーを取り付けることは両面SMT実装ではありません。J2/J4/J5はPCBA必須。J5はスルーホールのシェル端子もはんだ付けします。J1/C381116とJP1/C124375のTHT実装可否は業者確認が必要です。不可なら適合する同じLCSC部品を別購入して手はんだとし、適合品がLCSCにない場合だけ秋月を検討します。片面SMTでも全品の実装受理を保証しません。

SW3とr3の主電源回路はありません。外部給電が有効なら基板の既存電源回路が動作し、基板上で外部給電を一括切断したりFPGAだけを停止したりするスイッチはありません。リセット・ユーザーボタン・BUS ARMは維持。ショートピンC5305は別梱包・初期未装着です。Tab5とCoreはユーザー購入でPCBA・支援申請対象に含めません。

初期通信は**1MHz、弱ドライブ/SLOW、DATA setup/hold各250ns以上、DIR待ち500ns以上**。各版の通信150条件は受信端150/150、送信端60/150が範囲内です。高速エッジの不合格条件も公開。周期モデルの1MHzは4/4ですが、10〜40MHz安定動作や実機DMA・GPU性能の証明ではありません。

安定化12Vを使用し、Core通常0.5Aを初回評価条件とします。廉価版の局所3.3Vは通常10mA以下・外部給電なし。50mA急変と遅いLDOループの感度試験2条件が±5%を外れます。

HDMIは結合RLGC線路、仮定したThevenin駆動源、理想受信端の等価モデルで、ケーブルは含みません。中心100mV・窓0.4UIは工学的判定条件であり、HDMI認証のマスクではありません。ベンダーIBISモデル、認証、実機映像出力は未確認です。

解析は公式NGspice46 WASMをEasyEDA API Gateway内で実行した等価回路モデルです。製造回路図全体の自動SPICE解析、実スイッチング・熱・PD交渉の検証ではありません。

## Spark

[国外向けEasyEDA Spark](https://oshwlab.com/activities/easyeda-spark-2026?tab=2#P1)への応募準備です。設計工程を含む資格、完成品要件、支援受理は主催者確認が必要です。登録後の自動入金を想定せず、設計・見積の審査とクーポン承認を前提とします。LCSC単品購入への支援は未確認。応募・材料申請・製造注文・支払いは未実施です。

Copyright2026 airpocket-soundman。[MIT](LICENSE)および[第三者ライセンス表示](THIRD_PARTY_NOTICES.md)。

## 製造条件と警告の確認

PoC製造条件は**JLC04161H-7628・4層・板厚1.6mm・外層銅厚35µm・内層15.2µm・εr=4.4**です。全設定は各版のorder-profile JSONを参照。SMTは表面のみ、J3はLCSC別購入・手はんだを維持します。

回路図警告13件は全て分類済みです。予約PD_PG/TAB_SCL/TAB_SDAが3件、同名VBUS_PD/GND重複が2件、カスタムライブラリの販売属性が4グループ、意図的に未使用のJ4端子94本が4グループ。致命的エラー0・エラー0・未分類0です。DRCルールの緩和や警告の抑制をせず、回路・端子照合に基づきPoC用に受理した内容を記録しています。

## PoC発注用一式

- [フル版 ZIP](hardware/full/full-r4-poc-order.zip)
- [廉価版A ZIP](hardware/lite-a/lite-a-r4-poc-order.zip)

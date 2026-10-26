# r4 assembly instructions / 実装指示 / 装配要求

Both variants use **top-side SMT only**. Main-power and FPGA-only shutdown SW3 are omitted. These are quotation-review candidates; supplier DFM, rotations and actual fit require approval before manufacturing.

| | Full | Lite A |
| --- | --- | --- |
| PCBA quotation candidates |101 parts /43 rows |103 parts /43 rows |
| Separately purchased and hand soldered |J3/C56496 ×1 |J3/C56496 ×1 |
| Board |125×78mm, four layers |99×78mm, four layers |

## PCBA versus manual work

- Use each variant's `jlc-bom.csv` and `jlc-cpl.csv` as a matching pair. **Both exclude J3.** `bom.csv` also lists manual J3 and identifies its assembly method.
- **J3/C56496 is bought separately from LCSC and manually soldered by the user.** Preserve bottom-facing mating orientation, the confirmed mirrored pin assignment, 6mm mating pins, 3mm solder tails and2.54mm insulator. It is not bottom-side SMT. Confirm actual Tab5 mating and screw/standoff clearances before soldering.
- **J2 USB-C, J4 Core socket and J5 HDMI require manufacturer assembly.** J5 MOLEX2086581001/C916313 requires soldering all19 signal contacts and all four through-hole shell tabs. Include this process in the quotation.
- J1/C381116 and JP1/C124375 are THT quotation candidates requiring supplier acceptance. If declined, buy the selected suitable LCSC parts separately and hand solder. Avoid duplicate orders for parts already supplied by PCBA. Only when no suitable LCSC part exists should Akizuki be considered.
- SMT is top-side only, but this alone does not guarantee acceptance of every part under Economic PCBA or any other selected service.
- Tab5, Tang Primer20K Core, cables and mechanical hardware are excluded from PCBA. The C5305 shunt is separately packed and initially absent.

## Orientation and mechanics

1. J1 DC-005-5A-2.0/C381116: regulated12V, center positive. Pad1=DC_RAW, pads2/3=GND. Manufacturer A1 layout: pad2 X−5.9mm, pad3 X−3.0/Y4.7mm from pad1; three1×3.5mm slots. Verify actual plug fit. The connector's5A rating does not rate the board for5A.
2. Full SW1/SW2 C480272: XKB TS-1102S-B-D-B, height5.5mm. Check contact groups and cover/actuator fit.
3. Lite A SW1/SW2 C318884: XKB TS-1187A-B-A-B, height1.5mm. The local land pattern is rotated90° from the datasheet view. CAD left pair1 corresponds to common A/B; right pair2 to common C/D. Confirm library rotation and actual contact groups in the assembly preview.
4. JP1 C124375: fit the1×2 header, leave the C5305 shunt absent until firmware GPIO ownership and power behavior are reviewed.
5. Full has six mounting locations; Lite A has four. Review spacer lengths, screw penetration, Core insertion/removal clearance, Tab5 mating and protective enclosure fit.
6. No SW3, U11, R53–R58 or C25/C26 belongs to r4. Do not mix r3 main-power parts or files into this quotation.

## Bring-up limits

Check shorts, input polarity and regulator outputs with Tab5 and Core disconnected, then use current-limited power. There is no board-mounted main switch: external power present means the carrier supply runs. Initial communication is1MHz, weak drive/SLOW, DATA setup/hold≥250ns each, DIR turnaround≥500ns. Leave ARM unshunted until firmware ownership is verified. Lite A local3.3V normal load≤10mA, no external loads. Begin Core evaluation at its documented normal0.5A condition.

日本語：J3はLCSC別購入・手はんだで、PCBA BOM/CPLから除外。両版ともSMTは表面のみ、SW3は省略。裏向きTHTの手付けを両面SMTとして見積もらないこと。

中文：J3从LCSC单独购买并手焊，不计入PCBA BOM/CPL。两款SMT均仅在正面，省略SW3。背向THT手焊不应按双面SMT报价。

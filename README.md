# Tab5 FPGA Carrier — Spark

> **Main-power revision in progress — do not fabricate. Published schematics, PCBs and simulations use the old SW3 FPGA-only shutdown circuit. The latching main switch that cuts external12V to both Tab5 and FPGA is not yet implemented in these files. Tab5 battery operation remains outside the switch scope.**

[日本語](README.ja.md) · [中文](README.zh.md) · **English**

**[Design notebook / 日中英 GitHub Pages](https://airpocket-soundman.github.io/tab5-fpga-carrier-spark/)**

Two LCSC-first carrier designs connect **M5Stack Tab5 and Tang Primer 20K Core** for explicitly addressed external DDR3 RAM storage, general-purpose GPU research and graphics acceleration. Linux memory experiments and graphics experiments use separate software and FPGA bitstreams. The Core's128MB DDR3 does not automatically become Tab5 system RAM.

Status: **engineering review / EasyEDA Spark entry preparation**,2026-10-26. Physical communication, DDR3 initialization, rendering performance, enclosure fit and manufacturing acceptance remain unverified. No entry, support application, manufacturing order or payment has been submitted through this repository.

| | Full | Lite A |
| --- | --- | --- |
| Board |125×78mm,4 layers |99×78mm,4 layers |
| Inputs / video |Regulated12V barrel, USB PD12V, HDMI |Same functions retained |
| Power |TPS5430, Bourns15µH, TLV1117LV33 |TPS5430, COILMX15µH, XC6206P332MR-G |
| HDMI bias |499Ω |510Ω |
| PCBA quotation candidates |103 components /45 BOM rows |105 components /45 BOM rows |
| EasyEDA-run numerical cases |172 |187 |
| Power cases within model voltage limits |6/6; local LDO dynamics excluded |19/21; includes deliberately severe sensitivity cases |
| Native PCB DRC |0 violations |0 violations |
| Native schematic |0 fatal errors /13 warnings awaiting classification |Same |

Lite A targets lower cost through board area and parts selection; actual savings require manufacturer quotations. The extra feedback resistors make its populated-component count slightly higher.

## Files

- [Full native EasyEDA Pro project](hardware/full/spark-lcsc-priority-review.epro2) · [BOM](hardware/full/bom.csv) · [manufacturing review files](hardware/full)
- [Lite A native EasyEDA Pro project](hardware/lite-a/spark-lite-a-lcsc-review.epro2) · [BOM](hardware/lite-a/bom.csv) · [manufacturing review files](hardware/lite-a)
- [Full EasyEDA simulation records](simulation/full) · [Lite A EasyEDA simulation records](simulation/lite-a)
- [Simulation method and limitations](simulation/README.md) · [file hashes](manifest.json)

Open the `.epro2` project in EasyEDA Pro. It contains the schematic, PCB and project libraries. Manufacturing files are **quotation/review candidates**, not fabrication release. Verify component rotations, pin1, polarity, solderable shell tabs, bottom-header assembly and stock with the manufacturer.

## LCSC-first sourcing

All populated board components have selected LCSC IDs. The four former manual-assembly items are now PCBA quotation candidates: DC jack **C381116**, bottom Tab5 header **C56496**, ARM header **C124375**, stop switch **C692500**. Official JLCPCB listings show Extended / Wave Soldering / Economic and Standard; this does not constitute acceptance of this particular board. If assembly is declined, direct LCSC purchase and hand soldering is the fallback. Only unavailable suitable LCSC parts fall back to Akizuki.

The **C5305 shunt is a separate accessory**, initially absent. Tab5 and the Core module are purchased separately and excluded from sponsorship requests. Enclosure, spacers and screws require mechanical review. Standalone LCSC support is not assumed under Spark.

## Operating envelope

- Stabilized12V input; begin Core bring-up at its documented normal0.5A condition.
- Initial parallel-link evaluation at **1MHz**, weak drive/SLOW, DATA setup and hold≥250ns each, DIR turnaround≥500ns.
- Both variants:150 communication sensitivity cases solve;150 receiver-voltage cases pass, but only60 transmitter-voltage cases pass. Fast-edge cases exceed the source envelope. These are not150 unconditional passes.
- The1MHz periodic model passes4/4 conditions. Stable10–40MHz communication is not established.
- Lite A local3.3V: normal load≤10mA, no external loads. The50mA step and slow-loop sensitivities exceed±5%; failed cases remain published.
- Fully modelled switching/thermal behavior, PD negotiation, HDMI certification and physical DMA/DDR3 operation are not established.

The simulations use the official **NGspice46 WASM inside EasyEDA's API Gateway client** and analytical equivalent circuits. They are not automatic SPICE simulation of every component on the manufacturing schematic. The complete product still needs software, FPGA bitstreams, a fitted protective enclosure and hardware demonstration.

## Spark status

This repository is preparation for the [international EasyEDA Spark program](https://oshwlab.com/activities/easyeda-spark-2026?tab=2#P1), not an assertion of eligibility or acceptance. Design-process eligibility and complete-product requirements still need organizer confirmation. Registration does not automatically provide cash: material support requires an approved design/quotation application and coupons. No prize money or completion coupons are counted as initial funding.

Copyright2026 airpocket-soundman. Original material is under [MIT](LICENSE); [third-party notices](THIRD_PARTY_NOTICES.md) apply separately.

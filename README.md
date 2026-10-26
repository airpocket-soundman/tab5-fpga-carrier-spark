# Tab5 FPGA Carrier — Spark

**r4: top-side SMT only. Main-power and FPGA-only shutdown switch SW3 are omitted. J3 is separately purchased from LCSC and manually soldered. PoC order files are complete; normal supplier placement/stock/DFM acceptance and post-manufacturing validation are separate steps.**

[日本語](README.ja.md) · [中文](README.zh.md) · **English**

[Trilingual design and simulation site](https://airpocket-soundman.github.io/tab5-fpga-carrier-spark/)

Four-layer carriers connecting M5Stack Tab5 and Tang Primer 20K Core for **FPGA DDR3 RAM storage, general-purpose GPU research and graphics acceleration**. The 128MB DDR3 is an explicitly accessed data store. It does not automatically expand Tab5 system RAM. Linux and graphics experiments use separate software and FPGA bitstreams.

| | Full | Lite A |
| --- | --- | --- |
| Board |125×78mm, four layers |99×78mm, four layers |
| Interfaces |Regulated 12V barrel, USB PD12V, HDMI |Same |
| Supply components |TPS5430, Bourns15µH, TLV1117LV33 |TPS5430, COILMX15µH, XC6206 |
| PCBA candidates |101 parts /43 BOM rows |103 parts /43 BOM rows |
| Manual assembly |J3/C56496, outside PCBA BOM and CPL |Same |
| SMT side |Top only |Top only |
| Cases calculated inside EasyEDA |207 |221 |
| Power cases within numerical limits |6/6; TLV1117 dynamics excluded |18/20; two severe sensitivities exceed limits |
| HDMI engineering criteria |35/35 |35/35 |
| Native PCB DRC |0 violations |0 violations |
| Native schematic |0 fatal errors,0 errors /13 reviewed warnings,0 unclassified |Same |

Numerical completion and circuit-limit approval are separate measures. PoC data preparation is complete. Supplier acceptance, stock, physical fit and hardware operation still require the usual order review and post-manufacturing checks. No entry, order or payment has been submitted.

## Files

- [Full EasyEDA Pro project](hardware/full/spark-lcsc-priority-review.epro2) · [BOM](hardware/full/bom.csv) · [Gerber, PCBA BOM/CPL and drawings](hardware/full)
- [Lite A EasyEDA Pro project](hardware/lite-a/spark-lite-a-lcsc-review.epro2) · [BOM](hardware/lite-a/bom.csv) · [Gerber, PCBA BOM/CPL and drawings](hardware/lite-a)
- [Full simulation records](simulation/full) · [Lite A simulation records](simulation/lite-a) · [method and limits](simulation/README.md)
- [Assembly instructions](hardware/ASSEMBLY.md) · [r4 revision](hardware/MAIN_POWER_REVISION.md) · [file hashes](manifest.json)

Each `.epro2` contains the schematic, PCB and libraries. The supplied CPL is corrected to the official JLCPCB footprint frame; use it for placement rather than regenerating raw library rotations. Use the supplied `jlc-bom.csv` and `jlc-cpl.csv` together for the PCBA quotation. They exclude J3. The broader `bom.csv` also identifies the manually soldered J3.

## Sourcing and operation

All selected board parts use LCSC IDs. **J3/C56496 is separately purchased and manually soldered**, retaining its bottom-facing mating orientation. Bottom-side THT installation by the user does not require bottom-side SMT assembly. J2/J4/J5 require PCBA, including J5's through-hole shell tabs. J1/C381116 and JP1/C124375 THT acceptance requires supplier confirmation. If declined, purchase the same suitable LCSC part for hand soldering. Akizuki is a fallback only when no suitable LCSC part is available. Single-sided SMT alone does not guarantee acceptance under every assembly service.

SW3 and the r3 main-power circuit are absent. External power enables the existing carrier power circuit; there is no board-mounted main switch or FPGA-only shutdown switch. Reset, user button and BUS ARM remain. The C5305 shunt is separately packed and initially absent. Tab5 and Tang Primer 20K Core are user purchases outside PCBA and the sponsorship request.

Begin communication at **1MHz, weak drive/SLOW, DATA setup and hold ≥250ns each, DIR turnaround ≥500ns**. In each variant, receiver-voltage cases pass150/150, but source-voltage cases pass60/150; fast-edge failures remain published. The1MHz periodic model passes4/4. Stable10–40MHz operation, physical DMA and GPU throughput are unverified.

Use regulated12V. Begin Core evaluation at its documented normal0.5A condition. Lite A local3.3V normal load is limited to10mA, without external loads. The50mA step and slow-LDO-loop sensitivities exceed±5%.

HDMI cases use coupled RLGC lines, an assumed Thevenin driver and ideal receiver without a cable. The100mV center margin and0.4UI window are engineering criteria, not HDMI compliance masks. Vendor IBIS, HDMI certification and actual video output are unverified.

Calculations use the official NGspice46 WASM inside the EasyEDA API Gateway client. They are analytical equivalent circuits, rather than automatic SPICE simulation of the complete manufacturing schematic. Switching, thermal and PD negotiation qualification remain outside this analysis.

## Spark status

This repository prepares an application to the [international EasyEDA Spark program](https://oshwlab.com/activities/easyeda-spark-2026?tab=2#P1). Design-process eligibility, complete-product requirements and support approval require organizer confirmation. Registration does not automatically provide development funds. Material support is subject to an approved design/quotation application and coupons. Standalone LCSC support is not assumed. No entry, material application, manufacturing order or payment has been submitted.

Copyright2026 airpocket-soundman. Original material is under [MIT](LICENSE); [third-party notices](THIRD_PARTY_NOTICES.md) apply separately.

## Manufacturing profile and warning review

The PoC profile is **JLC04161H-7628, four layers,1.6mm board,35µm outer copper,15.2µm inner copper,εr=4.4**. See the variant order-profile JSON for the complete settings. The top-side SMT and separate manually soldered J3 configuration is retained.

All13 schematic warnings are classified: three reserved PD_PG/TAB_SCL/TAB_SDA nets, two repeated identical VBUS_PD/GND labels, four custom-library supplier-attribute groups, and four groups for94 intentionally unused J4 pins. There are zero fatal errors, zero errors and zero unclassified warnings. The reviewed warnings are accepted for PoC without suppressing warnings or changing DRC rules; detailed evidence is retained with the design records.

## PoC order packages

- [Full ZIP](hardware/full/full-r4-poc-order.zip)
- [Lite A ZIP](hardware/lite-a/lite-a-r4-poc-order.zip)

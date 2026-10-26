# Assembly review instructions / 組立レビュー / 装配评审

**Engineering quotation candidate. Do not manufacture without preview/DFM, fit and warning review.** Quantities and placement files are per board. The proposed initial quotation is five PCBs with two assemblies, subject to support approval.

## Manufacturer assembly

- Full:103 populated components. Lite A:105. DNP connectors, holes, modules and separate accessories are excluded.
- **J4 Core socket, J2 USB-C and J5 HDMI require manufacturer assembly.** If the selected service cannot assemble them, revise the service/selection; do not silently move them to customer soldering.
- J5 MOLEX2086581001/C916313: solder all19 signal contacts **and all four through-hole shell tabs**. Include the shell-tab process in the quotation.
- J3 is installed on the **bottom side**. Its confirmed mirrored pin assignment must be retained. Check the top-SMT/bottom-THT process, wave/selective soldering or fixture,3mm solder-tail clearance,6mm mating-pin length and2.54mm insulator height.
- J1/C381116, J3/C56496, JP1/C124375 and SW3/C692500 are Extended / Wave Soldering candidates on the official JLCPCB pages. Listing support does not approve the specific assembly process, stock or rotation for this design.
- If these four items are declined for assembly, buy the selected compatible parts from LCSC and hand solder. Avoid duplicate purchases for items already included in PCBA. Akizuki is the fallback only when no suitable LCSC part is available.

## Polarity, orientation and mechanics

1. **J1 DC-005-5A-2.0/C381116:** stabilized12V, center positive. CAD pad1=DC_RAW; pads2/3=GND. Manufacturer A1 layout: pad2X−5.9mm; pad3X−3.0/Y4.7mm relative to pad1; three1×3.5mm slots. Nominal center-pin2.0mm and opening6.2mm require actual plug-fit confirmation. The5A component rating is not a5A board rating.
2. **SW3 DS-02BLP/C692500:** first physical pole closes BUCK_EN to GND and stops the FPGA supply; open means running. The second pole is unused. **Both switches OFF initially.** Local CAD DIP-style numbering is1–4 and2–3; the supplier's aligned-contact diagram calls the same physical poles1–3 and2–4. Use physical contact correspondence, not a numbering assumption. Body ON therefore means FPGA stopped.
3. **Full SW1/SW2 C480272:** XKB TS-1102S-B-D-B, height5.5mm, manufacturer-derived lands. Verify contact groups and actuator height against the cover.
4. **Lite A SW1/SW2 C318884:** XKB TS-1187A-B-A-B, height1.5mm, recommended7.0/5.0 by4.5/3.0mm land envelope **rotated90° relative to the datasheet view**. CAD left pair is number1 and must correspond to the manufacturer's common **A/B** terminals; CAD right pair number2 corresponds to common **C/D**. They connect only when pressed. **Do not assume CPL rotation0° equals the supplier library's orientation0°. Confirm the preview's contact groups.** The low button requires a matching cover/actuator design.
5. **JP1 C124375:** fit the1×2 header, but pack the **C5305 shunt separately**, initially absent. Install only after firmware GPIO ownership and power behavior are reviewed.
6. Four mounting locations on Lite A versus six on Full. Spacer lengths, screw penetration, Core insertion/removal clearance and protective-cover fit remain unvalidated. Do not use an unreviewed cover for ordering.

## First power-on

Keep the Core and Tab5 disconnected while checking shorts, input polarity and regulator outputs. Confirm SW3 stop/run behavior, then proceed with the modules under current-limited power. Initial communication is1MHz with weak drive/SLOW, DATA setup/hold≥250ns each and DIR turnaround≥500ns. Keep ARM unshunted until firmware pin ownership is checked. Lite A local3.3V normal load≤10mA, no external loads; Core normal0.5A is the initial evaluation condition.

The carrier does not provide proven DDR3/GPU functionality by itself. Compatible firmware and FPGA bitstreams, hardware measurements and a mechanically fitted complete product remain necessary.

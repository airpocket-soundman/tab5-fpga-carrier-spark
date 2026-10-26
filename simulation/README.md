# r4 EasyEDA simulation records

Calculations execute **inside the EasyEDA API Gateway client** with the official NGspice46 WASM from [easyeda/eext-simulation-with-ngspice](https://github.com/easyeda/eext-simulation-with-ngspice/tree/50d2d3928d9e02f0b3617f51419936930629699f). These are analytical equivalent circuits, rather than automatic SPICE simulation of the complete manufacturing schematic.

| Model | Full | Lite A |
| --- | --- | --- |
| Power |6 cases,6 within voltage limits |20 cases,18 within voltage limits |
| Parallel step response |150 |150 |
| Periodic link |16 |16 |
| HDMI |35 |35 |
| Total completed solves |207 |221 |

All completed solves are distinct from all conditions passing. r4 has no main-power or FPGA-only shutdown switch. These results do not validate switched shutdown/inrush behavior.

## Contents and runtime

- `power-results.json`: actual EasyEDA voltage extrema, conditions and outcomes.
- `link-results.json`:150 pin-envelope and settling sensitivity cases per variant.
- `periodic-results.json`:16 threshold tests at1/10/20/40MHz, fast/slow, both directions.
- `hdmi-results.json`:35 differential-line cases and engineering criteria per variant.
- `execution-records.json`: actual engine, execution project, timing and input/native hashes.
- `*-inputs.json`: portable equivalent-circuit inputs and analysis conditions.
- `*.csv`: representative power waveform samples exported from the EasyEDA calculation.
- `raw-output-hashes.json`: complete engine export hashes and sizes; large raw files remain with the project maintainer.
- `engine.json`: pinned engine source and artifact hashes. `runtime/worker.js` is the adapter; licenses are in `runtime/licenses`.

The full simulation UI extension was not installed. The desktop client executes the official solver runtime through its API environment, with no GUI automation. Use the [API Gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway) and pinned official engine files to reproduce this runtime.

Power inputs require `TPS5430_TRANS.LIB` obtained separately from [Texas Instruments](https://www.ti.com/product/TPS5430#design-tools-simulation). The proprietary library is not redistributed. Portable paths are relative. For actual WASM execution the library was inlined with copyright comments decoded as Windows-1252 and `psa` PSpice compatibility enabled. This does not change the circuit equations.

## Model conditions and limits

Power uses an averaged TPS5430 controller retaining its compensation network. Full excludes TLV1117 dynamic response. Lite A uses XC6206 dynamics fitted to typical curves, not a vendor transistor model. Its50mA load-step and slow-LDO-loop sensitivity cases exceed3.3V±5%; normal local load is≤10mA without external loads. Both failed cases remain published. A zero-ohm PD-path resistance is floored to1e-12Ω by the engine.

The parallel link uses distributed linear RLC, fixed switch Ron and IBIS-derived pin capacitance, rather than a complete nonlinear GPIO IBIS model. Each variant has receiver150/150 and source60/150 voltage-envelope passes. Fast-edge failures remain published. Initial use assumes1MHz, weak drive/SLOW, DATA setup/hold≥250ns each and DIR turnaround≥500ns.

Periodic equations, analysis settings and end times are unchanged. After solving, NGspice `linearize` exports100ps samples to remain under the WASM100000-point limit. The150 step-response cases retain adaptive output. At1MHz,4/4 periodic cases pass; higher-frequency failures do not establish usable throughput.

HDMI uses coupled RLGC sections, an assumed Thevenin driver and ideal50Ω-per-leg receiver. Cases cover four lanes at742.5/1485Mb/s across nominal, fast/low-impedance and weak/high-capacitance corners;251.75Mb/s nominal; data-lane control patterns; and segmentation refinement. The model includes assumed socket, bias, coupling-capacitor, ESD and connector parasitics. It excludes cable effects and Gowin vendor IBIS. A minimum100mV signed center margin and0.4UI sample window are engineering criteria, not HDMI compliance masks.35/35 meeting these criteria does not prove HDMI certification or actual video output.

These records do not establish switching or thermal qualification, PD negotiation, physical PARLIO/DMA, DDR3 initialization, GPU throughput or manufactured-hardware operation.

Execution records retain the UUID of the project in which calculations actually ran. Final native projects include a mask/paste-only correction of U2 thermal copper, with exact pad and drill geometry retained. Solver inputs and electrical routing are unchanged. Actual native paste and drill output was inspected separately.

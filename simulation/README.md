# EasyEDA Pro simulation records

These published records contain calculations executed **inside the EasyEDA API Gateway client**, using the official NGspice46 WASM from [easyeda/eext-simulation-with-ngspice](https://github.com/easyeda/eext-simulation-with-ngspice/tree/50d2d3928d9e02f0b3617f51419936930629699f). No GUI automation or synthetic simulation-result events produced these results.

The full design has6 power,150 communication and16 periodic cases:172 total. Lite A has21 power,150 communication and16 periodic cases:187 total. The per-case records retain actual engine identity, client version, elapsed calculation time, diagnostics, netlist hashes and native project hashes.

## Contents

- `power-results.json`: voltage extrema, per-case voltage-limit outcomes and diagnostics.
- `link-results.json`:150 sensitivity results, pin extrema, settling time and per-pin envelope outcomes.
- `periodic-results.json`:16 periodic threshold tests at1/10/20/40MHz, fast/slow, both directions.
- `execution-records.json`: actual engine and execution metadata. Numerical completion is distinct from circuit-limit approval.
- `*-inputs.json`: portable equivalent-circuit inputs and analysis parameters.
- `*.csv`: up to4000 representative samples of power waveforms **exported from the EasyEDA execution**.
- `raw-output-hashes.json`: hashes and sizes of complete engine exports retained by the project maintainer; large raw files are not stored in this repository.
- `engine.json`: pinned engine source commit and runtime artifact hashes.
- `runtime/worker.js`: adapter for the unmodified official engine; third-party licenses are in `runtime/licenses`.

Power decks require `TPS5430_TRANS.LIB` obtained separately from [Texas Instruments](https://www.ti.com/product/TPS5430#design-tools-simulation). The vendor library itself is not distributed here. Portable `.include` paths are relative. For the WASM execution, the library was inlined with its copyright comments decoded as Windows-1252, and PSpice compatibility mode `psa` applied to the inlined helper definitions. The original engine input hashes are recorded. This portability adjustment does not change circuit equations.

Use the [EasyEDA API Gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway), obtain the pinned official engine files, then provide the netlists and WASM binary to the included worker inside the EasyEDA client. These data are **analytical equivalent circuits**, not a pre-bound SPICE model for every component on the manufacturing schematic. The full official simulation UI extension was not installed; the existing desktop client executed the official solver runtime through its API environment.

## Model limits

The link is linear distributed RLC with fixed switch Ron and IBIS-derived port capacitance, rather than a full nonlinear GPIO IBIS model. Falling excursions are inferred from linearity. Receiver150/150 passes does not imply every source pin passes:60/150 source-voltage cases pass, with fast-edge failures retained. Initial1MHz, weak drive/SLOW, DATA setup/hold≥250ns each and DIR turnaround≥500ns remain constraints.

The periodic solver retains its original equations, analysis settings and end time. After solving, NGspice `linearize` exports100ps samples because the WASM vector export is capped at100000 points. Periodic thresholds use this output. The150 step-response extrema use the full adaptive output without resampling.

Full power cases use an averaged TPS5430 model, excluding TLV1117 dynamics. Lite A includes approximate XC6206 dynamics fitted to typical curves, not a vendor-validated transistor model. Lite A19/21 voltage-limit passes include two50mA sensitivity failures; normal local3.3V load is limited to10mA without external loads. A zero-ohm PD-path resistor is floored to1e-12Ω by the engine, with its warning retained.

These records do not establish switching/thermal qualification, PD negotiation, HDMI certification, physical PARLIO/DMA, DDR3 initialization or achieved GPU throughput.

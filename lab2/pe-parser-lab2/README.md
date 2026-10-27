# Laboratory 2 — PE Parser (C++17)

A read-only Portable Executable (PE32/PE32+) header parser, based on the laboratory C++ starter kit. `pe_helpers.hpp` is unchanged.

## Build

```bash
g++ -std=c++17 -O2 main.cpp -o pe_parser
```

On Windows with MinGW, output `pe_parser.exe`; with MSVC use `cl /std:c++17 /EHsc /O2 main.cpp /Fe:pe_parser.exe`.

## Run

```bash
./pe_parser ../lab2-samples/valid/console64.exe
./pe_parser ../lab2-samples/malformed/wx_section.exe --bonus-red-flags
```

The program **reads** PE files; it never executes them.

## Implemented laboratory requirements

- DOS header and PE signature verification
- COFF header, machine names and flags
- PE32 and PE32+ optional headers
- Data directories (maximum 16)
- Section headers, permissions, and entry point
- RVA-to-file-offset conversion
- Bounds checking on binary reads and graceful malformed-file errors

## Bonus status

- **Bonus 1: Red flags — implemented** (`--bonus-red-flags`): W+X sections, entry point outside `.text` or in the last section, and unusual timestamps (zero / before 1995 / future).
- **Bonus 2–7 — not implemented yet**: imports, exports, PDB path, TLS callbacks, Rich header, and corkami torture tests.

Heuristic warnings are not proof of malicious behavior. Bonus mode is separate so normal output remains identical to the provided sample references.

## Validation

All five valid samples and both suspicious-but-valid samples (`wx_section.exe`, `ep_outside.exe`) match the supplied `expected/` output byte-for-byte in standard mode. The remaining six malformed samples return a nonzero exit status with a clear error rather than crashing; exact error texts may differ from the professor's reference.

See `docs/manual-analysis.md` for Exercise 1 and `tests/test_parser.py` for automated regression tests.

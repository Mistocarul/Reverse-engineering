# Analiza instrucțiunilor ASM – P1, P2, P4, P5 și P6

## P1 – Atribuiri și copieri între variabile

### Instrucțiuni ASM

```asm
mov dword ptr [ebp + var_4], 2
mov dword ptr [ebp + var_8], 4
mov eax, dword ptr [ebp + var_8]
mov dword ptr [ebp + var_4], eax
mov eax, dword ptr [ebp + var_4]
mov dword ptr [ebp + var_8], eax
xor eax, eax
```

### Echivalent C++

```cpp
int valoareA = 2;   // var_4
int valoareB = 4;   // var_8
valoareA = valoareB;
valoareB = valoareA;
```

`xor eax, eax` pune `eax` la zero. Deoarece apare după atribuiri, în epilog, este compatibil cu returnarea valorii `0` de către funcție.

## P2 – Calcul aritmetic cu înmulțire și indexare

### Instrucțiuni ASM

```asm
mov dword ptr [ebp + var_8], 1
mov dword ptr [ebp + var_4], 2
mov dword ptr [ebp + var_C], 3
imul eax, dword ptr [ebp + var_C], 3
mov ecx, dword ptr [ebp + var_8]
lea edx, [eax + ecx*2 - 5]
mov dword ptr [ebp + var_4], edx
imul eax, dword ptr [ebp + var_4], 3
mov dword ptr [ebp + var_8], eax
xor eax, eax
```

### Echivalent C++

```cpp
int rezultat = 1;      // var_8
int calcul = 2;       // var_4
int factor = 3;       // var_C

calcul = 3 * factor + 2 * rezultat - 5;
rezultat = 3 * calcul;
```

Instrucțiunea `lea` efectuează aici **un calcul aritmetic**, fără citirea memoriei de la adresa calculată. Prima expresie produce `3*3 + 2*1 - 5 = 6`, iar apoi `rezultat = 18`.

## P4 – Expresii aritmetice echivalente

### Instrucțiuni ASM

```asm
mov dword ptr [ebp + var_8], 1
mov dword ptr [ebp + var_4], 2
mov eax, dword ptr [ebp + var_4]
sub eax, 2
imul ecx, dword ptr [ebp + var_8], 3
add ecx, 1
imul eax, ecx
mov edx, dword ptr [ebp + var_8]
sub edx, 2
imul ecx, edx, 3
sub eax, ecx
mov dword ptr [ebp + var_4], eax
xor eax, eax
```

### Echivalent C++

```cpp
int valoareA = 1; // var_8
int rezultat = 2; // var_4

rezultat = (rezultat - 2) * (3 * valoareA + 1)
          - 3 * (valoareA - 2);
```

**Valorile finale:** `valoareA = 1`, `rezultat = 3`.

## P5 – Operatori aritmetici: adunare și scădere

### Instrucțiuni ASM

```asm
mov dword ptr [ebp + var_8], 1
mov dword ptr [ebp + var_4], 2
mov dword ptr [ebp + var_C], 3
mov eax, dword ptr [ebp + var_4]
add eax, 5
mov dword ptr [ebp + var_4], eax
mov eax, dword ptr [ebp + var_8]
sub eax, 4
mov dword ptr [ebp + var_8], eax
mov eax, dword ptr [ebp + var_C]
sub eax, 1
mov dword ptr [ebp + var_C], eax
mov ecx, dword ptr [ebp + var_4]
add ecx, dword ptr [ebp + var_C]
add ecx, dword ptr [ebp + var_8]
mov dword ptr [ebp + var_4], ecx
mov edx, dword ptr [ebp + var_8]
add edx, 1
mov dword ptr [ebp + var_8], edx
xor eax, eax
```

### Echivalent C++

```cpp
int suma = 2;       // var_4
int termenB = 1;    // var_8
int termenC = 3;    // var_C

suma += 5;
termenB -= 4;
termenC -= 1;
suma = suma + termenC + termenB;
termenB += 1;
```

La final, valorile sunt `suma = 6`, `termenB = -2` și `termenC = 2`.

## P6 – Operatori pe biți: AND, XOR și OR

### Instrucțiuni ASM

```asm
mov dword ptr [ebp + var_4], 7
mov eax, dword ptr [ebp + var_4]
and eax, 5
mov dword ptr [ebp + var_8], eax
mov dword ptr [ebp + var_4], 9
mov eax, dword ptr [ebp + var_4]
and eax, 6
mov dword ptr [ebp + var_8], eax
mov dword ptr [ebp + var_4], 9
mov eax, dword ptr [ebp + var_4]
xor eax, 6
mov dword ptr [ebp + var_8], eax
mov dword ptr [ebp + var_4], 3
mov eax, dword ptr [ebp + var_4]
and eax, 1
mov dword ptr [ebp + var_8], eax
mov dword ptr [ebp + var_4], 2
mov eax, dword ptr [ebp + var_4]
or eax, 1
mov dword ptr [ebp + var_8], eax
xor eax, eax
```

### Echivalent C++

```cpp
int operand = 7;          // var_4
int rezultatBiti = operand & 5; // var_8, rezultatul este 5

operand = 9;
rezultatBiti = operand & 6;    // 0

operand = 9;
rezultatBiti = operand ^ 6;    // 15

operand = 3;
rezultatBiti = operand & 1;    // 1

operand = 2;
rezultatBiti = operand | 1;    // 3
```

Operatorii C++ au următoarele semnificații: `&` = AND pe biți, `^` = XOR pe biți, `|` = OR pe biți. În această funcție, variabila `rezultatBiti` este suprascrisă la fiecare pas.

---

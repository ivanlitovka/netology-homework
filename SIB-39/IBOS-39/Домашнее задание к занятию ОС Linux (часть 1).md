```
d:\hashcat-6.2.6>hashcat.exe -a 0 -m 1800 hash 10-million-password-list-top-100000.txt
hashcat (v6.2.6) starting

hiprtcCompileProgram is missing from HIPRTC shared library.

OpenCL API (OpenCL 2.1 AMD-APP (3608.0)) - Platform #1 [Advanced Micro Devices, Inc.]
=====================================================================================
* Device #1: AMD Radeon RX 5700 XT, 8064/8176 MB (6732 MB allocatable), 20MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt
* Uses-64-Bit

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 281 MB

Dictionary cache hit:
* Filename..: 10-million-password-list-top-100000.txt
* Passwords.: 100000
* Bytes.....: 781896
* Keyspace..: 100000

$6$iMDxXB6C.bGVPgP/$dzNU7.0TSuoY8LUBKInul8kkDbjNsTEJWC6ake4pBi9Mf8icvzTm7aydpgs7ciJsRurui/SVBHsKWP0Ji4f7U1:fear

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$iMDxXB6C.bGVPgP/$dzNU7.0TSuoY8LUBKInul8kkDbjNsTE...i4f7U1
Time.Started.....: Mon Apr 29 23:05:08 2024 (1 sec)
Time.Estimated...: Mon Apr 29 23:05:09 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (10-million-password-list-top-100000.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    23001 H/s (7.93ms) @ Accel:32 Loops:256 Thr:128 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 20480/100000 (20.48%)
Rejected.........: 0/20480 (0.00%)
Restore.Point....: 16384/100000 (16.38%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:4864-5000
Candidate.Engine.: Device Generator
Candidates.#1....: wizzard -> 260689
Hardware.Mon.#1..: Temp: 68c Fan: 25% Util: 53% Core:1830MHz Mem:1742MHz Bus:16

Started: Mon Apr 29 23:05:05 2024
Stopped: Mon Apr 29 23:05:10 2024

d:\hashcat-6.2.6>
```
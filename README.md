# WordJong DS Buffer Overflow
**NOTE: THIS EXPLOIT CORRUPTS THE SOUND OF THE GAME, IT IS HIGHLY RECOMMENDED TO MUTE THE EMULATOR OR SYSTEM IF YOU RUN THIS EXPLOIT**

**NOTE: THIS HAS BEEN TESTED AND WORKS ON ALL EMULATORS, BUT CANNOT BE HARDWARE VERIFIED, IT IS BELIEVED THIS IS DUE TO CORRUPTION OF THE CPSR** 

## About

This is a buffer overflow exploit for the game **WordJong DS (U)**. This exploit only works for the 2007 USA release and **NOT** the 2010 European and Australian releases.

I have written a small paper about finding the exploit [here](https://borga.rs/nds.pdf).

## Pre-Requisites

If you just want to see the exploit working, use an emulator if you are permitted to do so.

**Python 3** as well as the **pwntools** library for Python, this can be installed using pip. This is used for the CRC patching script.

**make** and **devkitPro** with **libnds** to compile payloads into ARM assembly and binary.

## Files

**PoC.sav** - NDS save file that contains the exploit and a Proof of Concept payload, which makes the bottom screen change colour.

**patch.py** - Python script that patches the CRC so that the game will not delete said save file when it is loaded into the cartridge.

**payload.s** - The proof of concept payload in ARM assembly format, credits to [CTurt](https://github.com/CTurt "CTurt's GitHub")

**Makefile** - Make file that converts ARM assembly files to binary format, credits to [CTurt](https://github.com/CTurt "CTurt's GitHub")

**stub.sav** - NDS save file that contains the exploit with no payload code.

## Usage

To patch a save file's CRC:
```bash
python3 patch.py [INPUT FILE] [OUTPUT FILE]
```

To trigger the exploit:
Press Start when told to do so, click on 'Awards' and the press the R button.
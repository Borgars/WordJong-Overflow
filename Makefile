include $(DEVKITARM)/ds_rules

payload.bin: payload.s
	$(CC) -nostartfiles -nostdlib -x assembler-with-cpp payload.s -Ttext=0x02fbee40 -o payload.elf
	$(OBJCOPY) -O binary payload.elf $@
	@rm -f payload.elf

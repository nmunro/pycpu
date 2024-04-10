section .prog
    org 0x1000
    move.l #0x00000000, r1
    move.l #hello, r2

print_loop:
    move.b (r2)+, r3       ; Load next character from string
    cmp.b #0, r3           ; Check for null terminator
    beq print_done         ; If null terminator, end loop
    move.b r3, (r1)+       ; Write character to display
    bra print_loop         ; Continue to next character

print_done:
    halt

section .data
hello:
    dc.b "Hello World!", 0

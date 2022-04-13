data segment
    array  db 09h, 08h, 02h, 01h, 03h, 07h, 05h, 06h, 04h, 00h
    grst dw 0000h
    last dw 0000h
data ends
code segment
          assume cs:code, ds:data
    start:
          mov    dx, data
          mov    ds, dx
          lea di, array
          mov last, 09h[di]
          loop1:
            mov si, di
            loop2:
                inc si
                ; code to compaire and find the gretest number
                cmp si, last
            jnz loop2
            mov al, [di]
            xchg al, [grst]
            mov [di], al
            inc di
            cmp di, last
            jnz loop1
          int    03h
code ends
end start
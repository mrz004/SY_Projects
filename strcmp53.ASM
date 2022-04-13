data segment
    strs db 'computer$'
    strd db 'computers$'
    msg1 db 'Strings are equal$'
    msg2 db 'Strings are not equal$'
data ends

code segment
              assume cs: code, ds: data
    start:    
              mov    ax, data
              mov    ds, ax
              lea    si, strs
              lea    di, strd
    up:       
              mov    al, [si]
              cmp    al, [di]
              jne    noteq
              cmp    al, '$'
              je     outofloop
              mov    al, [di]
              cmp    al, '$'
              je     outofloop
              inc    si
              inc    di
              jmp    up
    outofloop:
              mov    ah, 09h
              lea    dx, msg1
              int    21h
              jmp    exit
    noteq:    
              mov    ah, 09h
              lea    dx, msg2
              int    21h
    exit:     
              int    03h
code ends
end start
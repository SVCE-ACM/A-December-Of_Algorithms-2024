section .data
    trips db 0
    current_load db 0
    houses db 10, 20, 30, 40, 50
    W db 100

section .text
    global _start

_start:
    ; Initialize loop counter and pointers
    mov si, 0                ; SI will serve as an index into the houses array
    mov al, 0                ; AL will hold the current load
    mov bl, 0                ; BL will hold the trips count

.loop_start:
    mov dl, [houses + si]    ; Load current house gift amount into DL
    add al, dl               ; Add gift amount to current load
    cmp al, [W]              ; Compare current load with W
    jg .new_trip             ; If the load exceeds W, take a new trip

    inc si                   ; Move to the next house
    cmp si, 5                ; Check if we've processed all houses
    jl .loop_start
    jmp .done

.new_trip:
    inc bl                   ; Increment the trip count
    mov al, dl               ; Reset current load to the current house's gift
    inc si                   ; Move to the next house
    cmp si, 5                ; Check if we've processed all houses
    jl .loop_start

.done:
    mov eax, 1               ; Exit system call
    int 0x80

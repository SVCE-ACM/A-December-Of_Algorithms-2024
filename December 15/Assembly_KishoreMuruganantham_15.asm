section .data
    houses db 10, 15, 5, 20, 7  ; Example array of gifts per house
    W db 25                     ; Max weight a person can carry

section .bss
    trips resb 1                 ; Variable for the number of trips
    current_load resb 1          ; Variable for the current load

section .text
    global _start

_start:
    ; Initialize variables
    mov byte [trips], 0         ; trips = 0
    mov byte [current_load], 0  ; current_load = 0
    mov ecx, 0                  ; Loop index (ecx will be used for iterating through houses)
    mov al, [W]                 ; Load the maximum weight W into register al

loop_start:
    ; Check if we've reached the end of the array (this will depend on the number of houses)
    ; For this example, we assume the array size is 5 (hardcoded here).
    cmp ecx, 5
    jge loop_end                ; If we've checked all houses, jump to loop_end

    ; Load the number of gifts in the current house (houses[ecx])
    movzx edx, byte [houses + ecx]
    add al, dl                  ; Add the current house gifts to the current load (current_load += gifts)

    ; Check if current load exceeds the max weight (W)
    cmp al, byte [W]
    jg new_trip                 ; If current_load > W, we need a new trip

    ; Otherwise, continue to the next house
    inc ecx
    jmp loop_start

new_trip:
    ; Increment trips by 1
    inc byte [trips]

    ; Reset current load to 0 (start a new trip)
    mov byte [current_load], 0

    ; Add current gifts to the new trip
    movzx edx, byte [houses + ecx]
    add byte [current_load], dl

    ; Continue to the next house
    inc ecx
    jmp loop_start

loop_end:
    ; Final check: if there is remaining load, count another trip
    cmp byte [current_load], 0
    je end_program
    inc byte [trips]            ; If current_load > 0, increment trips

end_program:
    ; Exit the program
    mov eax, 1                  ; sys_exit
    int 0x80                    ; call kernel

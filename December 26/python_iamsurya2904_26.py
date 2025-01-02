       IDENTIFICATION DIVISION.
       PROGRAM-ID. CanEscapeLava.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NUMS.
           05 NUM-LENGTH     PIC 9(02) VALUE 5.
           05 NUM-TABLE       OCCURS 5 TIMES INDEXED BY IDX.
              10 NUM-ELEMENT   PIC 9(02).
       01 MAX-REACH          PIC 9(02) VALUE 0.
       01 I                   PIC 9(02) VALUE 0.
       01 JUMP                PIC 9(02).
       01 RESULT              PIC X VALUE 'N'.

       PROCEDURE DIVISION.
       
       * Initialize the NUM-TABLE with values
           MOVE 2 TO NUM-TABLE(1).
           MOVE 3 TO NUM-TABLE(2).
           MOVE 1 TO NUM-TABLE(3).
           MOVE 0 TO NUM-TABLE(4).
           MOVE 4 TO NUM-TABLE(5).
       
       * Call the function to check if escape is possible
           PERFORM CAN-ESCAPE-LAVA.

           DISPLAY "Result: " RESULT.

       STOP RUN.

       CAN-ESCAPE-LAVA.
           PERFORM VARYING I FROM 1 BY 1 UNTIL I > NUM-LENGTH
               MOVE NUM-TABLE(I) TO JUMP
               
               * Check if current position is unreachable
               IF I > MAX-REACH
                   MOVE 'N' TO RESULT
                   EXIT PERFORM
               END-IF

               * Update the maximum reach
               COMPUTE MAX-REACH = FUNCTION MAX(MAX-REACH, I + JUMP)
               
               * Check if we can reach the end of the array
               IF MAX-REACH >= NUM-LENGTH - 1
                   MOVE 'Y' TO RESULT
                   EXIT PERFORM
               END-IF
           END-PERFORM.

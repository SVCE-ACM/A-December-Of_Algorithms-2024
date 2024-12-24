       IDENTIFICATION DIVISION.
       PROGRAM-ID. PascalTriangle.

       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
       01 numRows         PIC 99 VALUE 0.
       01 i               PIC 99 VALUE 0.
       01 j               PIC 99 VALUE 0.
       01 result          OCCURS 10 TIMES
                             OCCURS 10 TIMES
                             PIC 99 VALUE 0.
       01 row             OCCURS 10 TIMES PIC 99 VALUE 0.

       PROCEDURE DIVISION.
           DISPLAY "Enter the number of rows: " WITH NO ADVANCING.
           ACCEPT numRows.

           IF numRows = 0 THEN
               DISPLAY "No Pascal's Triangle."
               STOP RUN
           END-IF.

           MOVE 1 TO result(1, 1).

           PERFORM VARYING i FROM 2 BY 1 UNTIL i > numRows
               MOVE 1 TO row(1)
               PERFORM VARYING j FROM 2 BY 1 UNTIL j = i
                   COMPUTE row(j) = result(i - 1, j - 1) + result(i - 1, j)
               END-PERFORM
               MOVE 1 TO row(i)
               PERFORM VARYING j FROM 1 BY 1 UNTIL j > i
                   MOVE row(j) TO result(i, j)
               END-PERFORM
           END-PERFORM.

           PERFORM VARYING i FROM 1 BY 1 UNTIL i > numRows
               DISPLAY "Row ", i, ": " WITH NO ADVANCING
               PERFORM VARYING j FROM 1 BY 1 UNTIL result(i, j) = 0
                   DISPLAY result(i, j) WITH NO ADVANCING
                   DISPLAY " " WITH NO ADVANCING
               END-PERFORM
               DISPLAY ""
           END-PERFORM.

           STOP RUN.

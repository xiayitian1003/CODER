> PS D:\CODE\codestore\ostep-homework\cpu-intro> python .\process-run.py -s 1 -l 3:50,3:50, -s 2 -l 3:50,3:50, -s 3 -l 3:50,3:50 -c -p -I IO_RUN_IMMEDIATE
> Time        PID: 0        PID: 1           CPU           IOs
>   1        RUN:cpu         READY             1
>   3        WAITING        RUN:io             1             1
>   4        WAITING       WAITING                           2
>   5        WAITING       WAITING                           2
>   6        WAITING       WAITING                           2
>   7        WAITING       WAITING                           2
>   8*   RUN:io_done       WAITING             1             1
>   9*         READY   RUN:io_done             1
>  10          READY        RUN:io             1
>  11        RUN:cpu       WAITING             1             1
>  12           DONE       WAITING                           1
>  13           DONE       WAITING                           1
>  14           DONE       WAITING                           1
>  15           DONE       WAITING                           1
>  16*          DONE   RUN:io_done             1
>  17           DONE       RUN:cpu             1
>
> Stats: Total Time 17
> Stats: CPU Busy 9 (52.94%)
> Stats: IO Busy  11 (64.71%)
>
> PS D:\CODE\codestore\ostep-homework\cpu-intro> python .\process-run.py -s 1 -l 3:50,3:50, -s 2 -l 3:50,3:50, -s 3 -l 3:50,3:50 -c -p -I IO_RUN_LATER
> Time        PID: 0        PID: 1           CPU           IOs
>   1        RUN:cpu         READY           1
>   2         RUN:io         READY             1
>   3        WAITING        RUN:io              1             1
>   4        WAITING       WAITING                           2
>   5        WAITING       WAITING                           2
>   6        WAITING       WAITING                           2
>   7        WAITING       WAITING                           2
>   8*   RUN:io_done       WAITING         1             1
>  10           DONE   RUN:io_done          1
>  11           DONE        RUN:io              1
>  12           DONE       WAITING                           1
>  13           DONE       WAITING                           1
>  14           DONE       WAITING                           1
>  15           DONE       WAITING                           1
>  16           DONE       WAITING                           1
>  17*          DONE   RUN:io_done             1
>  18           DONE       RUN:cpu             1
>
> Stats: Total Time 18
> Stats: CPU Busy 9 (50.00%)
> Stats: IO Busy  11 (61.11%)
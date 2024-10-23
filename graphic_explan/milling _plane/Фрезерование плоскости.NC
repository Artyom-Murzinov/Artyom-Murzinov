%
O0001
#1 = 10 (radius frezji)
#2 = 100 (dlina ploskosty)
#3 = 100 (wisota ploskosti)
#4 = 0 (NACHALNAYA Z)
#5 = -5 (konechnaya po Z)
#6 = -50 (Nachalnaya X)
#7 = -50 (nachalnaya Y)
#8 = 0.31 (Shag po Z)
#9 = 0.8 ( koeficient na radius)
#10 = 5 (BEZOPASNOE RASTOYANIE PO X)
#11 = 3 (BEZOPASNOE RASTOYANIE Z)
#12 = 100
#500 = #6 - #10 - #1 (X)
#501 = #7 (Y)
#503 = #2 + #6 +#10 + #1
#504 = #3 + #7
#505 = #1 * #9
#506 = #4
N1
G90 G0 X#500 Y#501
Z#506
G1X#503
G91 G0 Z#11
IF [#501EQ#504] GOTO 2 
#501 = #501 + #505
IF [#501GE#504] THEN #501 = #504
IF [#501LT#504] GOTO 1
IF [#501EQ#504] GOTO 1
N2
#501 = #7
IF [#506EQ#5] GOTO3
#506 = #506 - #8
IF [#506LE#5] THEN #506 = #5
IF [#506GT#5] GOTO 1
IF [#506EQ#5] GOTO 1
N3
#506 = #4
G90 G0 Z#12
M30

cat test.txt | python3 ATCGVariants.py -a 5 -b 6 -c

#1       1:82154 0       82154   T       A
#1       1:752566        0       752566  C       G
#1       1:776546        0       776546  G       C
#1       1:800007        0       800007  A       T

cat test.txt | python3 ATCGVariants.py -a 5 -b 6 -c -r -m
##test comments
#1       1:752721        0       752721  G       A
#1       1:768448        0       768448  0       0
#1       1:798959        0       798959  G       A
#1       1:838555        0       838555  A       C

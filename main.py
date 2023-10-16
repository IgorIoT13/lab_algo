from  Stila import stilla

val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
val2 = [-1, 4, 6, 3, 12, 15, 9, 22, 44, 69, 24]
val3 = [1, 2]
val4 = [1, 4, 6]

test = stilla(5, 3, val2)

cur = test.finaly_cal()

print(cur)


cov = stilla(3, 3, [-1, 2, 5, 7, 1])
cur = cov.finaly_cal()
print(cur)
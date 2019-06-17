import tensorflow as tf

A=tf.constant(2)
B=tf.constant(3)
C=tf.constant(4)

Calc1_op=A+B+C
Calc2_op=(A+B)*C

Sess = tf.Session()
Res1 = Sess.run(Calc1_op)
Res2 = Sess.run(Calc2_op)

print(Res1)
print(Res2)
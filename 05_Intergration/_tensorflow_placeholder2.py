import tensorflow as tf

A = tf.placeholder(tf.int32, [None])
B = tf.constant(10)
X10_op=A*B
Div=A/B

Sess = tf.Session()

R1=Sess.run(X10_op,feed_dict={A:[1,2,3,4,5]})
print(R1)
R2 = Sess.run(X10_op,feed_dict={A:[10,20]})
print(R2)
R3 = Sess.run(Div,feed_dict={A:[2,4,6,8,10]})
print(R3)
# 형변환도 알아서 해준다~
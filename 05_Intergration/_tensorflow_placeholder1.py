import tensorflow as tf

A = tf.placeholder(tf.int32,[3])
# int32 - 32bit의 인수를 의미, [3]은 리스트 하나에 3개의 값을 넣는다. 32비트 정수 배열 3개
B = tf.constant(2)
X2_op=A*B

Sess = tf.Session()

R1=Sess.run(X2_op,feed_dict={A:[1,2,3]}) # 여기서 A는 위의 변수 A를 의미.
print(R1)
R2=Sess.run(X2_op,feed_dict={A:[10,20,10]})
print(R2)
import tensorflow as tf

A=tf.constant(1234)
B=tf.constant(5000)
# 텐서플로는 이런식으로 어떤 공간을 만들어줘야만 한다고 함.
Add_op=A+B

Sess= tf.Session()
# Sess - 프린트 하기 전 상수를 더한 결과를 세션에 넣는 중간단계
Res = Sess.run(Add_op)
print(Res)


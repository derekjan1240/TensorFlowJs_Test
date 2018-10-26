import tensorflow as tf

a = tf.constant(1)
sess = tf.Session()
print(sess.run(a + 1))

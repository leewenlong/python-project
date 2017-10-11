# coding: utf-8

import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3], stddev=2, seed=2))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

x = tf.constant([[0.8, 0.5]])

ax = tf.matmul(x, w1)
y = tf.matmul(ax, w2)

# with tf.Session() as sess:
#     sess.run(w1.initializer)
#     sess.run(w2.initializer)
#     print sess.run(y)

# init method 2
with tf.Session() as s:
    s.run(tf.global_variables_initializer())
    print s.run(y)


print tf.VERSION
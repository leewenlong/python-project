# coding: utf-8

import tensorflow as tf

a = tf.constant([1, 2.0], name='aa')
b = tf.constant([2.0, 3], name='bb')

result = a + b;
with tf.Session() as sess:
    print sess.run(result)

with tf.Session().as_default():
    print result.eval()

print (a.graph is tf.get_default_graph())

g1 = tf.Graph()

with g1.as_default():
    v = tf.get_variable(name="v", initializer=tf.zeros_initializer(), shape=1)
    print v

g2 = tf.Graph()

with g2.as_default():
    v = tf.get_variable(name="v", initializer=tf.ones_initializer(), shape=1)
    print v


with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('',reuse=True):
        print (sess.run(tf.get_variable('v')))


with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('',reuse=True):
        print (sess.run(tf.get_variable('v')))
# coding: utf-8
import tensorflow as tf

a = tf.constant([1,3],name='a')
b = tf.constant([2,4],name='b')

result = a + b

session = tf.Session()
r = session.run(result)
print r

result = tf.add(a,b)

print result

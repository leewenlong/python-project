# coding: utf-8
import tensorflow as tf

tf.train.exponential_decay(0.1,tf.Variable(0),100,0.96,True)
tf.train.GradientDescentOptimizer(0.1).minimize({},())
# coding: utf-8
import tensorflow as tf
from numpy.random import  RandomState

tf.Session().as_default()
v = tf.constant([[1, 2, 3], [3, 4, 5.]])

r = tf.clip_by_value(v, 2, 4)
# 1
with tf.Session() as sess:
    tf.initialize_all_variables()
    print r.eval(session=sess)

# 2

with tf.Session().as_default():
    print r.eval()

# 3
print tf.Session().run(r)

# math log
with tf.Session().as_default():
    print tf.log(v).eval()

# math mean
with tf.Session().as_default():
    print tf.reduce_mean(v).eval()

# cross_entropy entropy
# cross_entropy = tf.nn.softmax_cross_entropy_with_logits(y,y_)
# only one right answer
# tf.nn.sparse_softmax_cross_entropy_with_logits(y,y_)

# tf.reduce_mean(tf.square(y-y_))
v1 = tf.constant([1, 2, 3, 4.0])
v2 = tf.constant([4, 4, 3, 3.0])
with tf.Session().as_default():
    print tf.greater(v1, v2).eval()
    print tf.select(tf.greater(v1, v2), v1, v2).eval()

# input: x , output: y_ , real value: y , weight: w1
#
def train():


    batch = 8
    x = tf.placeholder(tf.float32,(None,2))
    y_ = tf.placeholder(tf.float32,(None,1))
    w1 = tf.Variable(tf.random_normal([2,1],stddev=1,seed=1))
    y = tf.matmul(x,w1)

    loss_1 = 1
    loss_10 = 10

    loss = tf.reduce_sum(tf.select(tf.greater(y,y_),(y-y_)*loss_10,(y_-y)*loss_1))

    # loss = tf.reduce_mean(tf.square(y-y_))
    # loss = - tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y ,1e-10,1.0)))
    # loss = tf.nn.softmax_cross_entropy_with_logits(y,y_)
    train_step = tf.train.AdamOptimizer().minimize(loss)

    rdm = RandomState(1)

    datasize = 128
    X = rdm.rand(datasize,2) # (128,2) array
    Y = [[x1 + x2 + rdm.rand()/10.0-0.05] for (x1,x2) in X]
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        steps = 5000
        for i in range(steps):
            start = (i * batch)%datasize
            end = min(start + batch , datasize)
            sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
            print sess.run(w1)

if __name__ =="__main__":
    train()
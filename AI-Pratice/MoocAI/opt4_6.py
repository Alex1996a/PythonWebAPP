

LEARNING_RATE_BASE = 0.1
LEARNING_RAGE_DECAY = 0.99
LEARNING_RAGE_STEP = 1

global_step = tf.Variable(0, trainable=False)
learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,
        global_step, LEARNING_RATE_STEP, LEARNING_RATE_DECAY,
        stairecase=True)

w = tf.Variable(tf.constan(5, dtype=tf.float32))
loss = tf.square(w+1)

train_step = 
        tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, 
                                            global_step=global_step)

with tf.Session() as sess:
    init_ip = tf.global_variables_initializer()
    sess.run(init_op)

    for i in range(40):
        sess.run(train_step)
        learning_rate_val = sess.run(learning_rate)
        global_step_val = sess.run(global_step)
        w_val = sess.run(w)
        loss_val = sess.run(loss)

        print 'After steps: global_step, is %f, w is %f, learning rate is %f                '%(i, global_step_val, w_val, learning_rate_val, loss_val)



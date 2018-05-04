import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer  ## define a new var
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')

            tf.summary.histogram(layer_name + '/weights', Weights)  # tensorflow >= 0.12

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')

            # tf.histogram_summary(layer_name+'/biase',biases)   # tensorflow 0.12 以下版的
            tf.summary.histogram(layer_name + '/biases', biases)  # Tensorflow >= 0.12

        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)

        tf.summary.histogram(layer_name + '/outputs', outputs)  # Tensorflow >= 0.12

    return outputs

x_data = np.linspace(-1,1,300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_in')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_in')

l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)

prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]), name='loss')

    # tf.scalar_summary('loss',loss) # tensorflow < 0.12
    tf.summary.scalar('loss', loss)  # tensorflow >= 0.12

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()  # 替换成这样就好

sess = tf.Session()

# merged= tf.merge_all_summaries()    # tensorflow < 0.12
merged = tf.summary.merge_all() # tensorflow >= 0.12

# writer = tf.train.SummaryWriter('logs/', sess.graph)    # tensorflow < 0.12
writer = tf.summary.FileWriter("logs/", sess.graph) # tensorflow >=0.12

sess.run(init)

# plot the real data
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data, y_data)
# # plt.ion()#本次运行请注释，全局运行不要注释
# plt.show()

for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    # if i % 1000 == 0:
    #     # to see the step improvement
    #     print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
    #
    #     # to visualize the result and improvement
    #     # try:
    #     #     ax.lines.remove(lines[0])
    #     # except Exception:
    #     #     pass
    #     # prediction_value = sess.run(prediction, feed_dict={xs: x_data})
    #     # # plot the prediction
    #     # lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
    #     # plt.pause(1)

    if i % 50 == 0:
        rs = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(rs, i)

for i in range(3):
    print(x_data[i])

    print(sess.run(prediction,  feed_dict={xs: x_data, ys: y_data})[i])

    print(y_data[i])


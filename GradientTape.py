import tensorflow as tf
x = tf.convert_to_tensor(2.0)

with tf.GradientTape() as tape:
    tape.watch(x)
    y = x * x - 2
    z = y * x

grads = tape.gradient(z, x)
print(grads)
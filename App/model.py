import tensorflow as tf
from tensorflow.keras.layers import Layer

class ReflectionPadding2D(Layer):
    def __init__(self, padding=(1, 1), **kwargs):
        self.padding = padding
        super(ReflectionPadding2D, self).__init__(**kwargs)

    def call(self, x):
        padding_width, padding_height = self.padding
        return tf.pad(x, [[0, 0],[padding_height, padding_height], [padding_width, padding_width], [0, 0]], 'REFLECT')

    def get_config(self):
        config = super().get_config()
        config.update({"padding": self.padding})
        return config

#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import tensorflow as tf
import numpy as np
import os
import slim.nets.alexnet as alexnet

import merge_checkpoint as merge

def main():
    """
    You can also run these commands manually to generate the pb file
    1. git clone https://github.com/tensorflow/models.git
    2. export PYTHONPATH=Path_to_your_model_folder
    3. python alexnet.py
    """
    dir = os.path.dirname(os.path.realpath(__file__))
    if not os.path.isdir(dir + '/model'):
        os.mkdir(dir + '/model')
    batch_size = 5
    height, width = 224, 224
    #inputs = tf.placeholder(tf.float32, [None, height, width, 3])
    inputs = tf.Variable(tf.random_uniform((1, height, width, 3)), name='input')
    net, end_points  = alexnet.alexnet_v2(inputs, is_training=False)
    output = tf.Variable(tf.random_uniform(tf.shape(net)),name='output')
    result = tf.assign(output,net)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)   
        print(sess.run(result))
        checkpointpath = saver.save(sess, dir + '/model/alexnet.chkp')
        tf.train.write_graph(sess.graph, dir + '/model', 'alexnet.pbtxt')
        tf.summary.FileWriter(dir + '/log', sess.graph)

    input_graph = dir + "/model/alexnet.pbtxt"    
    input_checkpoint = dir + "/model/alexnet.chkp"
    output_node_names= "alexnet_v2/fc8/squeezed,output"
    output_graph = dir + "/alexnet_save.pb"

    merge.merge_checkpoint(input_graph, input_checkpoint, output_node_names, output_graph)

if __name__ == "__main__":
    main()
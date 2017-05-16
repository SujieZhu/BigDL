/*
 * Copyright 2016 The BigDL Authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.intel.analytics.bigdl.utils

import com.intel.analytics.bigdl.nn.{Graph, ReLU}
import org.scalatest.{FlatSpec, Matchers}
import com.intel.analytics.bigdl.numeric.NumericFloat

class TensorflowSaverSpec extends FlatSpec with Matchers {
  "Tensorflow saver" should "save graph model" in {
    val relu = ReLU().setName("relu").apply()
    val graph = Graph(relu, relu)

    val tmpfile = java.io.File.createTempFile("tensorflow", "saver")
    TensorFlowSaver.saveGraph(graph, Seq(("input", Seq(2, 4))), tmpfile.getPath)
  }
}
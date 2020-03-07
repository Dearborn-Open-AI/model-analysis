# Lint as: python3
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test for writer."""

from __future__ import division
from __future__ import print_function

import apache_beam as beam
import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import
from tensorflow_model_analysis.eval_saved_model import testutil
from tensorflow_model_analysis.writers import writer


class WriterTest(testutil.TensorflowModelAnalysisTest):

  def testWriteIgnoresMissingKeys(self):
    with beam.Pipeline() as pipeline:
      test = pipeline | beam.Create(['test'])
      # PTransform is None so this will throw exception if it tries to run
      _ = {'test': test} | writer.Write('key-does-not-exist', None)


if __name__ == '__main__':
  tf.test.main()

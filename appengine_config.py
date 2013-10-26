# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration for App Engine."""

__author__ = 'sll@google.com (Sean Lip)'

import os
import sys

appstats_CALC_RPC_COSTS = True


def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app


# Root path of the app.
ROOT_PATH = os.path.dirname(__file__)

THIRD_PARTY_LIBS = [
    os.path.join(ROOT_PATH, 'third_party/bleach-1.2.2'),
    os.path.join(ROOT_PATH, 'third_party/html5lib-python-0.95')
]

for lib_path in THIRD_PARTY_LIBS:
    if not os.path.isdir(lib_path):
        raise Exception('Invalid path for third_party library: %s' % lib_path)
    sys.path.insert(0, lib_path)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
App module unit and functional tests
"""

import unittest

# class RunServerTestCase(unittest.TestCase):
#
#     def setUp(self):
#         """ Test pre-setup """
#         self.app_server_thread = None
#         self.timeout = 2
#
#     def tearDown(self):
#         """ Test post-setup """
#         self.app_server_thread.join(self.timeout)
#         self.app_server_thread.terminate()
#
#     def test_run_server(self):
#         self.app_server_thread = multiprocessing.Process(target=init.setup().run)
#         self.app_server_thread.start()
#         time.sleep(self.timeout)
#         self.assertTrue(self.app_server_thread.is_alive())
#
#     def test_run_server_flask_env(self):
#         self.app_server_thread = multiprocessing.Process(target=init.setup().run)
#         self.app_server_thread.start()
#         time.sleep(self.timeout)
#         response = requests.get('http://localhost:8443/admin/token')
#         response_content = json.loads(response.text)
#         self.assertEqual(dict(error='Any argument given'), response_content)


if __name__ == '__main__':
    unittest.main()

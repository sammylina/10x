import os
import sys
import unittest

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.loader import SlackDataLoader

class TestPandas(unittest.TestCase):

    def setUp(self):
        data_loader = SlackDataLoader('/home/eyuel/Documents/10x/week0_starter_network_analysis/anonymized')
        df = data_loader.slack_parser('/home/eyuel/Documents/10x/week0_starter_network_analysis/all-week89/')

        self.data_frame_cols = list(df.columns.values)
        self.expected_cols = ['msg_type', 'msg_content', 'sender_name', 'msg_sent_time',
       'msg_dist_type', 'time_thread_start', 'reply_count',
       'reply_users_count', 'reply_users', 'tm_thread_end', 'channel']

    def test_pandas_columns(self):
        self.assertListEqual(self.data_frame_cols, self.expected_cols)


if __name__ == '__main__':
    unittest.main()

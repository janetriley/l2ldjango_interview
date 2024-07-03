from django.test import TestCase
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt, ISO_INPUT_FORMAT, L2L_DT_OUTPUT_FORMAT


class testL2l_dtTag(TestCase):

    def test_date_value(self):
        value = datetime.now()
        expected = value.strftime(L2L_DT_OUTPUT_FORMAT)
        result = l2l_dt(value)
        self.assertEqual(result, expected)

    def test_string_value(self):
        now = datetime.now()
        value = now.strftime(ISO_INPUT_FORMAT)
        expected = now.strftime(L2L_DT_OUTPUT_FORMAT)
        result = l2l_dt(value)
        self.assertEqual(result, expected)

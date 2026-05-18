import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    # --- ADD API TESTS ---
    def test_api_add_success(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "4")

    def test_api_add_failure_invalid_param(self):
        url = f"{BASE_URL}/calc/add/abc/2"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- SUBTRACT API TESTS ---
    def test_api_substract_success(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "2")

    def test_api_substract_failure_invalid_param(self):
        url = f"{BASE_URL}/calc/substract/5/abc"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- MULTIPLY API TESTS ---
    def test_api_multiply_success(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "12")

    def test_api_multiply_failure_invalid_param(self):
        url = f"{BASE_URL}/calc/multiply/3/abc"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- DIVIDE API TESTS ---
    def test_api_divide_success(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "5.0")

    def test_api_divide_failure_by_zero(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- POWER API TESTS ---
    def test_api_power_success(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "8")

    def test_api_power_failure_invalid_param(self):
        url = f"{BASE_URL}/calc/power/2/abc"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- SQUARE ROOT API TESTS ---
    def test_api_square_root_success(self):
        url = f"{BASE_URL}/calc/square_root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "3.0")

    def test_api_square_root_failure_negative(self):
        url = f"{BASE_URL}/calc/square_root/-9"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)

    # --- LOG10 API TESTS ---
    def test_api_log10_success(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        body = response.read().decode("utf-8")
        self.assertEqual(response.status, http.client.OK)
        self.assertEqual(body, "2.0")

    def test_api_log10_failure_non_positive(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(HTTPError) as ctx:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(ctx.exception.code, http.client.BAD_REQUEST)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

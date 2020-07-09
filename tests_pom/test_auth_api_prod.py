# -*- coding: utf-8 -*-
import requests
import pytest

"""
Запуск теста - pytest -s -v -m smoke test_autorization_api_prod.py
"""


@pytest.mark.smoke
def test_api_auth_user_not_found():
    data = {
        'username': 'some-non-existent-email@wrongdomain.domain',
        'password': 'some-random-text',
    }
    response = requests.post('https://robo.market/api/v1/auth/', json=data)
    assert response.status_code == 401

    response_data = response.json()

    assert response_data['code'] == 401
    assert response_data['result'] == 'User not found.'
    assert response_data['success'] is False
    assert response_data['headers'] == {}


@pytest.mark.smoke
def test_api_auth_success():
    data = {
        'username': 'test@robokassa.ru',
        'password': 'test-password',
    }
    response = requests.post('https://robo.market/api/v1/auth/', json=data)
    assert response.status_code == 200

    response_data = response.json()
    assert response_data['success'] is True
from pathlib import Path

from django.core.management import call_command

import pytest


@pytest.fixture(scope='class')
def django_db_setup(django_db_setup, django_db_blocker):
    fixtures_dir = Path(__file__).parent / "fixtures"
    user_fixture = fixtures_dir / "users.yaml"
    series_fixture = fixtures_dir / "series.yaml"
    with django_db_blocker.unblock():
        call_command('loaddata', str(user_fixture.resolve()))
        call_command('loaddata', str(series_fixture.resolve()))

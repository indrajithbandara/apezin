from django.apps import AppConfig
from django.conf.global_settings import APP_BASE


class BaseConfig(AppConfig):
    name = APP_BASE

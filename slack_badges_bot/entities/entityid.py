"""Tipo del identificador de entidades.
"""
from uuid import UUID, uuid4

__author__ = 'Jesús Torres'
__contact__ = "jmtorres@ull.es"
__license__ = "Apache License, Version 2.0"
__copyright__ = "Copyright 2019 {0} <{1}>".format(__author__, __contact__)


class EntityID(UUID):
    """Identificador de entidades.
    """
    @classmethod
    def generate_unique_id(cls):
        return cls(bytes=uuid4().bytes)

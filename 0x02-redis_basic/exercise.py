#!/usr/bin/env  python3
'''module for exercise.py '''



import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key and return the key.

        :param data: The data to be stored in the cache.
        :type data: Union[str, bytes, int, float]
        :return: The randomly generated key used to store the data in Redis.
        :rtype: str
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

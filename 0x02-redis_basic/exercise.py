#!/usr/bin/env python3
'''module for exercise.py '''


import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a
        edis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a
        random key and return the key.

        :param data: The data to be stored in the cache.
        :type data: Union[str, bytes, int, float]
        :return: The randomly generated key
        used to store the data in Redis.
        :rtype: str
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
         str, bytes, int, None]:
        """
        Retrieve the data associated with the given key from Redis.

        :param key: The key associated with the data.
        :type key: str
        :param fn: Optional callable to convert
        the data to the desired format.
        :type fn: Callable, optional
        :return: The data associated with the key,
        optionally converted by the provided callable.
        :rtype: Union[str, bytes, int, None]
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value associated with the given key from Redis.

        :param key: The key associated with the data.
        :type key: str
        :return: The string value associated with the key.
        :rtype: Union[str, None]
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value associated with the given key from Redis.

        :param key: The key associated with the data.
        :type key: str
        :return: The integer value associated with the key.
        :rtype: Union[int, None]
        """
        return self.get(key, fn=int)

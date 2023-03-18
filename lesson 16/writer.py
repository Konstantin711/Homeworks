from abc import ABC, abstractmethod


class Writer:
    @abstractmethod
    def write(self, data): ...

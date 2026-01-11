from abc import ABC, abstractmethod

class Geometry(ABC):
    @abstractmethod
    def metric(self, x): pass

    @abstractmethod
    def inverse_metric(self, x): pass

    @abstractmethod
    def volume_element(self, x): pass


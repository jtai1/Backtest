from abc import ABCMeta, abstractmethod

class backtestAbstract(metaclass=ABCMeta):
    """
       Define the abstract base class, which only requires user implementation of the run method
    """
    def __init__(self, portcash, slippage, commission):
        self.portcash = portcash
        self.slippage = slippage
        self.commission = commission

    @abstractmethod
    def run(self, startdate, enddate):
        raise NotImplementedError("Core method not implemented")
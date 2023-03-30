from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, ram, hdd, cpu):
        self._ram = ram
        self._hdd = hdd
        self._cpu = cpu
        self._type = None
    
    @property
    def ram(self):
        return self._ram
    
    @property
    def hdd(self):
        return self._hdd
    
    @property
    def cpu(self):
        return self._cpu
    
    @property
    def type(self):
        return self._type
    
    def __str__(self):
        return f"RAM: {self.ram}GB, HDD: {self.hdd}GB, CPU: {self.cpu}GHz, Type: {self.type}"
    
class PC(Computer):
    def __init__(self, ram, hdd, cpu):
        super().__init__(ram, hdd, cpu)
        self._type = "PC"
            
            
class Server(Computer):
    def __init__(self, ram, hdd, cpu):
        super().__init__(ram, hdd, cpu)
        self._type = "Server"    
                
class ComputerFactory:
    @staticmethod
    def create_computer(computer_type, ram, hdd, cpu):
        if computer_type == "PC":
            return PC(ram, hdd, cpu)
        elif computer_type == "Server":
            return Server(ram, hdd, cpu)
        else:
            raise ValueError(f"Invalid computer type: {computer_type}")        
pc = ComputerFactory.create_computer("PC", 8, 500, 3.0)
server = ComputerFactory.create_computer("Server", 32, 2000, 2.5)

print(pc)
print(server)
        
        
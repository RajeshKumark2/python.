from abc import ABC, abstractmethod 

class DataProcess(ABC):
    @abstractmethod 
    def load_data(self, source): 
        pass 

    @abstractmethod 
    def process(self): 
        pass 

    @abstractmethod 
    def save(self, destination): 
        pass 

    def run_pipleline(self, source, destination):
        self.load_data(source)
        self.process()
        self.save(destination)
        print("Pipeline completed")

class CSVProcessor(DataProcess):
    def load_data(self, source): 
        print(f"Loading CVS from {source}")

    def process(self):
        print(f"Cleaining and tranforming CVS data")

    def save(self, destination): 
        print(f"Saving processed data to {destination}")
processor = CSVProcessor()
processor.run_pipleline("input.csv", "output.csv")

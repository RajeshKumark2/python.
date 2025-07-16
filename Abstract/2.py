from abc import ABC, abstractmethod
class JSONSerializable(ABC):
    @abstractmethod
    def to_json(self):
        pass
class XMLSerializable(ABC):
    @abstractmethod
    def to_xml(self):
        pass
class Document(JSONSerializable, XMLSerializable):
    def __init__(self, content):
        self.content = content
        
    def to_json(self):
        return f'{{"content": "{self.content}"}}'
    
    def to_xml(self):
        return f'<document>{self.content}</document>'
doc = Document("Hello")
print(doc.to_json())  
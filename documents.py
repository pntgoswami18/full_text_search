from collections import Counter
from dataclasses import  dataclass

@dataclass
class Abstract:
    ''' Wikipedia Abstract '''
    ID: int
    title: str
    abstract: str
    URL: str

    @property
    def fulltext(self):
        return ' '.join([self.title, self.abstract])

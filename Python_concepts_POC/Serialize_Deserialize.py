# https://datausa.io/api/data?drilldowns=Nation&measures=Population
# nt6aRMCvEvDH43aA5-raTP9-JMpP4PJDRFqS2Y6Y6JVyquVh1XNzwuDuFcZP-YpPQpM

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Annotation:
    source_name: str
    source_description: str
    dataset_name: str
    dataset_link: str
    table_id: str
    topic: str
    subtopic: str

@dataclass
class Source:
    measures: List[str]
    annotations: Annotation
    name: str
    substitutions: List[Dict]  # Assuming substitutions is a list of dictionaries

@dataclass
class NationData:
    ID_Nation: str
    Nation: str
    ID_Year: int
    Year: str
    Population: int
    Slug_Nation: str

@dataclass
class ResponseData:
    data: List[NationData]
    source: List[Source]
    
    def __post_init__(self):
        self.data = [NationData(
            ID_Nation=d['ID Nation'],
            Nation=d['Nation'],
            ID_Year=d['ID Year'],
            Year=d['Year'],
            Population=d['Population'],
            Slug_Nation=d['Slug Nation']
            ) for d in self.data],
        self.source = [Source(
            measures=src['measures'],
            annotations=Annotation(**src['annotations']),
            name=src['name'],
            substitutions=src['substitutions']
            ) for src in self.source]

# @dataclass
# class Annotations:
#     source_name:str
#     source_description: str
#     dataset_name: str
#     dataset_link: str
#     table_id: str
#     topic: str
#     subtopic: str

# @dataclass
# class Source:
#      measures: List[str]
#      annotations: Annotations
#      name: str
#      substitutions: List[str]

# @dataclass
# class Population:
#      id_nation: str
#      nation: str
#      id_year: int
#      year: int
#      population: int
#      slug_nation: str
#      source: Source

# @dataclass
# class Data:
#      populaton: List[Population]

#      def __post_init__(self):
#           self.data = [Population(**d) for d in self.populaton]

# @dataclass
# class SourceData:
#      _source: Source

#      def __post_init__(self):
#           self.source = self._source

# @dataclass
# class Serialize_Deserialize:
#     data: Data
#     source: SourceData
     
#     def __post_init__(self):
#          self.data = Data(**self.data)
#         # self.source= SourceData(**self.source)

     


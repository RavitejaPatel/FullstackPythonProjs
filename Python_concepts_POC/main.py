from Serialize_Deserialize import NationData, ResponseData
import requests

streamPopulationData = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
streamResponse = requests.get(streamPopulationData).json()

#print(streamResponse.json())

#preparing Data object 

population_data = ResponseData(**streamResponse)
print("=========================================================================================================")
print(population_data)


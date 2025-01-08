import os
from openai import AzureOpenAI 

client = AzureOpenAI(
  azure_endpoint = "https://franc-m5o6p2b9-swedencentral.openai.azure.com/", 
  api_key= "E1MT69CPoobbRgPD11Dz8rMImV5S4KNm6ZgfkG1DUf0Kmv4b9Vi1JQQJ99BAACfhMk5XJ3w3AAAAACOGmVvJ",  
  api_version="2024-08-01-preview"
)

# ------------------------------------------------------------------------------
# PORCA TROIA, EVA CHE VADA A FARE IN C*** NON TOCCARE QUESTE RIGHE SOPRA
# ------------------------------------------------------------------------------


# client = AzureOpenAI(
#   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
#   api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
#   api_version="2024-02-01"
# )

response = client.chat.completions.create(
    model="gpt-4o", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Você é um analista de requisitos senior."},
        {"role": "user", "content": "Como identificar user stories a partir de prtótipos de telas?"}
        # ,
        # {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        # {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)



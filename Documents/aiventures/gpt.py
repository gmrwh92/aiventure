import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY


def generateCompanyDescription(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="Introduction of company within ten words : {} \n \n".format(prompt1),
      temperature=0,
      max_tokens=50,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
  
    return response['choices'][0]['text']

def generateSkills(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="list 10 few bullet points of key skills without adjective: {} \n\n".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def generateSkillsDescription(prompt1):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="Generate few bullet points to write my CV: {} \n\n- ".format(prompt1),
      temperature=0,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

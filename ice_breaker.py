import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import AzureChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break_with(name: str) -> str:
    # Lookup LinkedIn username using the agent - giving 4 LinkedIn profile
    linkedin_username = linkedin_lookup_agent(name=name)

    # Scrape LinkedIn profile data using the obtained username using proxyAPI
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    # Define the prompt template
    summary_template = """
        Given the linkedin information {information} about a person, please provide:
        1. A short summary.
        2. Two interesting facts about them.
    """

    # Create a PromptTemplate instance with the defined template and input variable
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    # Initialize the AzureChatOpenAI model with the specified parameters
    llm = AzureChatOpenAI(
        temperature=0,  # Controls the creativity of the model (0 means deterministic)
        model_name="gpt-35-turbo",  # The name of the deployed Azure OpenAI model
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),  # API key for authentication
        api_version="2024-02-15-preview"  # API version for Azure OpenAI
    )

    # Create an LLMChain instance that combines the prompt template and the language model
    chain = LLMChain(prompt=summary_prompt_template, llm=llm)

    # Run the chain with the provided information and print the output
    res = chain.run(information=linkedin_data)
    print(res)


if __name__ == "__main__":
    # Load environment variables from a .env file
    load_dotenv()

    # Ensure that the environment variables are set correctly
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not azure_openai_endpoint or not azure_openai_api_key:
        raise ValueError("AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set in the environment variables")

    # Run the ice breaker function
    ice_break_with("Eden Marco")

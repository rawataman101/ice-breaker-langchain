# Ice Breaker

Project Description: Ice Breaker
Overview
The "Ice Breaker" project is designed to help users quickly generate engaging conversation starters based on a person's LinkedIn profile information. By leveraging the power of Azure OpenAI and a custom LinkedIn profile scraper, this tool provides a short summary and interesting facts about individuals, making it easier to initiate meaningful conversations.

Key Features
LinkedIn Profile Scraping: The project includes a function to scrape publicly available data from LinkedIn profiles, either using mock data for testing or a real API for live data.
Azure OpenAI Integration: Utilizes the Azure OpenAI API to process and generate natural language summaries and interesting facts based on the scraped LinkedIn data.
Prompt Templates: Customizable prompt templates that format the input data to ensure relevant and accurate output from the language model.
Environment Configuration: Securely manages API keys and other sensitive information using environment variables.
Components
LinkedIn Profile Scraper:

Function: scrape_linkedin_profile
Description: Scrapes data from a LinkedIn profile URL. Uses mock data for testing purposes and can be configured to use a real API endpoint.
Azure OpenAI Integration:

Library: langchain_openai.AzureChatOpenAI
Description: Integrates with Azure OpenAI to generate content based on LinkedIn profile data.
Prompt Template:

Class: langchain.prompts.PromptTemplate
Description: Defines the format and structure of the prompts sent to the language model.
Environment Management:

Library: dotenv
Description: Loads environment variables from a .env file to securely manage API keys and other configuration settings.

Workflow
Load Environment Variables: Ensures all necessary configurations and API keys are loaded securely.
Scrape LinkedIn Profile: Fetches profile data using the provided LinkedIn URL. If in testing mode, uses mock data.
Generate Content: Uses Azure OpenAI to create a short summary and two interesting facts about the person based on their LinkedIn profile.
Output: The generated content is printed or returned, ready to be used for conversation starters.

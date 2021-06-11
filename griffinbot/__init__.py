# Setup env vars
try:
    from dotenv import load_dotenv

    print("Found .env file, loading environment variables from it.")
    load_dotenv(override=True)
except ModuleNotFoundError:
    pass


from griffinbot import logging

logging.setup()

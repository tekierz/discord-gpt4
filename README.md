# Discord-GPT4
GPT-4 Discord Bot

This is a simple Discord bot that allows users to interact with OpenAI's GPT-4 model. Users can send a prompt to the bot, and the bot will respond with an AI-generated response based on the prompt.
Requirements

    Python 3.10.6 or higher
    discord package
    interactions package
    openai package
    python-dotenv package

To install these packages, run:

pip install discord interactions openai python-dotenv

Setup

    Clone this repository to your local machine.

    Create a .env file in the project root directory with the following contents:

DISCORD_TOKEN=your_discord_token
DISCORD_GUILD=your_discord_guild_id
GPT4_API_KEY=your_openai_api_key

Replace your_discord_token, your_discord_guild_id, and your_openai_api_key with your actual Discord bot token, Discord guild ID, and OpenAI API key, respectively.

    Run the bot with:

python gpt4_discord_bot.py

Usage

To use the bot, type the following command in your Discord server:

/gpt prompt: Your prompt text here

Replace "Your prompt text here" with your desired prompt.

The bot will send a message indicating that it's waiting for a response from OpenAI, and then it will update the message with the AI-generated response.

License

This project is released under the MIT License. See the LICENSE file for details.
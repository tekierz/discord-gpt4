import os
import discord
import interactions
import openai
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))

# Configure GPT-4 API Key
openai.api_key = os.getenv('GPT4_API_KEY')

bot = interactions.Client(token=TOKEN)

async def fetch_gpt4_response(prompt: str):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}]
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    ))
    return response['choices'][0]['message']['content']

@bot.command(
    name="gpt",
    description="Interact with GPT-4",
    options=[
        interactions.Option(name="prompt", description="Enter your prompt for GPT-4", type=interactions.OptionType.STRING, required=True)
    ],
    scope=GUILD
)
async def gpt(ctx: interactions.CommandContext, prompt: str):
    print("Received prompt:", prompt)

    # Send initial response
    initial_message = await ctx.send("Waiting for a response from OpenAI...", ephemeral=False)
    
    # Fetch GPT-4 reply concurrently
    gpt4_task = asyncio.create_task(fetch_gpt4_response(prompt))

    print("Sending request to OpenAI API...")
    reply = await gpt4_task
    print("Reply:", reply)

    # Edit the initial message with the actual reply
    await initial_message.edit(content=reply)

bot.start()
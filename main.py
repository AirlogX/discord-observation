import os
import json
import time
import discord
from   datetime import datetime
from   discord.ext import commands, tasks

BASE_DIR = os.path.join(os.getcwd(), "AirLog")
USERS_DIR = os.path.join(BASE_DIR, "users")

os.makedirs(USERS_DIR, exist_ok = True)

bot = commands.Bot(
    command_prefix = "+",
    self_bot = True
)

def save_message(user_id: str, server_name: str, message_data: dict):
    user_dir = os.path.join(USERS_DIR, user_id, "messages")
    os.makedirs(user_dir, exist_ok = True)
    
    server_name = server_name.replace('[^a-zA-Z0-9]', "_")
    file_path = os.path.join(user_dir, f"{server_name}.json")
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding = "utf-8") as f:
                messages = json.load(f)
        except Exception as e:
            print(f"Error: {e}")
            
            messages = []
    else:
        messages = []
        
    new_message = {
        "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "content": message_data["content"],
        "channel": message_data["channel"]
    }
    messages.append(new_message)
    
    try:
        with open(file_path, "w", encoding = "utf-8") as f:
            json.dump(messages, f, indent = 4, ensure_ascii = False)
    except Exception as e:
        print(f"Error: {e}")
        
def save_voice(server_id, server_name, channel_id, channel_name, join_time, user_id):
    user_dir = os.path.join(USERS_DIR, user_id, "vocals")
    os.makedirs(user_dir, exist_ok = True)
    
    server_name = server_name.replace('[^a-zA-Z0-9]', "_")
    file_path = os.path.join(user_dir, f"{server_name}.json")
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding = "utf-8") as f:
                vocals = json.load(f)
        except Exception as e:
            print(f"Error: {e}")
            
            vocals = []
    else:
        vocals = []
        
    new_vocal = {
        "server_id": server_id,
        "server_name": server_name,
        "channel_id": channel_id,
        "channel_name": channel_name,
        "join_time": join_time
    }
    vocals.append(new_vocal)
    
    try:
        with open(file_path, "w", encoding = "utf-8") as f:
            json.dump(vocals, f, indent = 4, ensure_ascii = False)
    except Exception as e:
        print(f"Error: {e}")
        
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
    start_countdown()
    
@bot.event
async def on_message(message: discord.Message):
    if message.author.id == bot.user.id or not message.guild:
        return
        
    user_id = str(message.author.id)
    server_name = message.guild.name
    
    message_data = {
        "content": message.content,
        "channel": message.channel.name
    }
    
    save_message(user_id, server_name, message_data)
    
@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
    if before.channel != after.channel:
        if after.channel is not None:
            join_time = time.strftime("%Y-%m-%dT%H:%M:%S.", time.gmtime()) + str(time.time()).split(".")[1][:3] + "Z"
            server_id = str(member.guild.id)
            server_name = member.guild.name
            channel_id = str(after.channel.id)
            channel_name = after.channel.name
            
            save_voice(server_id, server_name, channel_id, channel_name, join_time, str(member.id))
    
def start_countdown():
    @tasks.loop(minutes = 1)
    async def count_users():
        try:
            total_messages = 0
            user_count = len(os.listdir(USERS_DIR))
            
            for user_id in os.listdir(USERS_DIR):
                user_id_path = os.path.join(USERS_DIR, user_id)
                
                for file in os.listdir(user_id_path):
                    file_path = os.path.join(user_id_path, file)
                    
                    try:
                        with open(file_path, "r", encoding = "utf-8") as f:
                            message_data = json.load(f)
                            total_messages += len(message_data)
                    except Exception as e:
                        print(f"Error: {e}")
                        
            print(f"Users scraped: {user_count}")
            print(f"Total messages: {total_messages}")
        except Exception as e:
            print(f"Error: {e}")
            
    count_users.start()

bot.run("")

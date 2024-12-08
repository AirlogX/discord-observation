# AirLog | Discord Observation

AirLog is a Discord bot designed for monitoring and recording messages and voice activity in Discord servers. The bot captures user interactions in text channels, logs voice channel join times, and stores all data in a local directory. The purpose of this bot is for observation and tracking of user activity.

## Features

- **Message Logging**: The bot records messages in a Discord server’s text channels, logging the message content, the channel name, and the timestamp.
- **Voice Channel Tracking**: The bot logs when a user joins a voice channel, including the server, channel, and the time they joined.
- **User Data Storage**: All captured data is saved in JSON format for later analysis.
- **Activity Count**: The bot periodically reports the total number of users and messages logged in the system.

## Setup and Installation

### Prerequisites
Before you begin, ensure you have the following:

1. **Python 3.8+**: Ensure Python is installed on your machine. You can download Python from [python.org](https://www.python.org/).
2. **Discord.py Library**: Install the necessary Python library to interact with the Discord API.
   
   To install `discord.py-self`, run:
   ```bash
   pip install discord.py-self
   ```

3. **Bot Token**: You need to create a bot on the Discord Developer Portal and get its token. This token will allow the bot to authenticate and interact with Discord.

### Running the Bot

Once the bot is running, it will automatically start recording:

- **Messages**: All messages sent by users (other than the bot itself) will be logged to `AirLog/users/{user_id}/messages/{server_name}.json`.
- **Voice State Updates**: When a user joins a voice channel, the bot records the event in `AirLog/users/{user_id}/vocals/{server_name}.json`.

### Data Structure

- **Messages**: Each logged message contains the following data:
  ```json
  {
    "date": "2024-12-08T14:00:00Z",
    "content": "Hello world",
    "channel": "general"
  }
  ```
  
- **Voice State**: Each logged voice state contains:
  ```json
  {
    "server_id": "123456789012345678",
    "server_name": "My Server",
    "channel_id": "987654321098765432",
    "channel_name": "Voice Channel 1",
    "join_time": "2024-12-08T14:00:00.123Z"
  }
  ```

## Usage

- **Bot Prefix**: The bot uses `+` as its command prefix. Currently, there are no additional commands implemented, but you can extend the bot's functionality by adding new commands.
  
- **Periodic Activity Count**: Every minute, the bot will output to the console the total number of messages logged and the number of users the bot is tracking.

## Example Output

When the bot starts and performs its periodic logging, you may see outputs like the following in the console:

```bash
Logged in as BotName
Users scraped: 5
Total messages: 120
```

## Troubleshooting

- **Missing Libraries**: If you encounter an error related to missing libraries, ensure all dependencies are installed using:
  ```bash
  pip install -r requirements.txt
  ```
  
- **Permissions**: Ensure the bot has the correct permissions on the Discord server to read messages and track voice state changes.

## Contributing

If you'd like to contribute to AirLog, feel free to fork the repository and submit a pull request with your proposed changes. We welcome improvements, bug fixes, and suggestions for additional features!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

---

This README is just a starting point. If you want to add more features or explanations later, feel free to expand it as needed!
import os
import time
import random
from modules import modules
from flask import Flask
from flask_discord_interactions import DiscordInteractions
from handlers.routes import configure_routes

app = Flask(__name__)
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.getenv("DISCORD_CLIENT_ID")
app.config["DISCORD_PUBLIC_KEY"] = os.getenv("DISCORD_PUBLIC_KEY")
app.config["DISCORD_CLIENT_SECRET"] = os.getenv("DISCORD_CLIENT_SECRET")


@discord.command()
def start(ctx):
    "Gives information about the bot."
    return "Discord-Bot is personal bot. It is currently in development."


@discord.command()
def help(ctx):
    "Gives information about all of the available commands."
    help_text = "The following commands are available: \n"
    for key in modules.COMMANDS:
        help_text += '/' + key + ': '
        help_text += modules.COMMANDS[key] + '\n'
    return help_text


@discord.command()
def ping(ctx):
    "Measure the execution time to run test and send a message."
    if str(ctx.author.id) != os.getenv("DISCORD_AUTHOR_ID"):
        return "You are not allowed to use this command."
    start_time = time.time()
    running_time = modules.get_running_time(start_time)
    return "Pong! Running time: {:.3f} s.".format(running_time)


@discord.command()
def caps(ctx, string: str):
    "Converts your sentence to uppercase."
    return string.upper()


@discord.command()
def rand(ctx, string: str):
    "Choose a random word from sentence, separated by space."
    string = string.split()
    idx = random.randint(0, len(string) - 1)
    return string[idx]


@discord.command()
def team(ctx, n_team: int, string: str):
    "Generate a random team from sentence, separated by space."
    string = string.split()
    try:
        int(n_team)
        result = modules.get_random_team(n_team, string)
        return result
    except:
        return "First argument must be a number!"


@app.before_first_request
def register_command():
    discord.update_commands()


discord.set_route("/interactions")

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

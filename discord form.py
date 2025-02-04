from flask import Flask, request
import discord
import asyncio
from datetime import datetime

app = Flask(__name__)

# Discord bot token and channel ID
DISCORD_TOKEN = "MTMyNTAzOTAyMDM2MjgyNTcyOQ.GB03oD.6nvS-QyQq9rkfZxLecTTlSKshOwWoO1BXRL_Rw"  # Replace with your bot token securely
DISCORD_CHANNEL_ID = 1329391476181827627 # Replace with the channel ID

# Define a function to send the message using the bot
async def send_to_discord(message):
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        if channel:
            await channel.send(message)
        await bot.close()

    await bot.start(DISCORD_TOKEN)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get form data
        friend_username = request.form.get("friend_username")
        your_username = request.form.get("your_username")  # User-provided username
        friend_gender = request.form.get("friend_gender")
        your_gender = request.form.get("your_gender")
        ott_code = request.form.get("ott_code")
        description = request.form.get("description")  # New description field

        # Get current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
        
        # Format the message
        message = (
            f"**New Form Submission:**\n"
            f"**Date and Time:** {current_time}\n"
            f"**Friend's Discord Username:** {friend_username}\n"
            f"**Submitted by:** @{your_username}\n"  # Use plain text @username
            f"**Friend's Gender:** {friend_gender}\n"
            f"**Your Gender:** {your_gender}\n"
            f"**OTT Request Code:** {ott_code}\n"
            f"**Description:**\n```{description}```"
        )
        
        # Send the message to Discord
        asyncio.run(send_to_discord(message))

        return f"""
        <div style="background-color: #2C003E; color: #F3E8E2; font-family: Arial, sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; flex-direction: column;">
            <h2>Form Submitted Successfully!</h2>
            <p>The details have been sent to your Discord channel.</p>
            <a href="/" style="color: #F3E8E2; text-decoration: underline;">Go back</a>
        </div>
        """
    
    return """
    <div style="background-color: #2C003E; color: #F3E8E2; font-family: Arial, sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center;">
        <div style="background-color: #4B0082; padding: 30px; border-radius: 10px; width: 50%; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);">
            <h1 style="text-align: center;">TodayMod - Application Form</h1>
            <form method="POST" style="display: flex; flex-direction: column; gap: 15px;">
                <label>Enter your friend's Discord username:</label>
                <input type="text" name="friend_username" required style="padding: 10px; border-radius: 5px; border: none;">

                <label>Enter your Discord Username (e.g., username#1234):</label>
                <input type="text" name="your_username" required style="padding: 10px; border-radius: 5px; border: none;">

                <label>Select your friend's gender:</label>
                <select name="friend_gender" required style="padding: 10px; border-radius: 5px; border: none;">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>

                <label>Select your gender:</label>
                <select name="your_gender" required style="padding: 10px; border-radius: 5px; border: none;">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>

                <label>Enter OTT Request Code:</label>
                <input type="text" name="ott_code" required style="padding: 10px; border-radius: 5px; border: none;">

                <label>Enter Description:</label>
                <textarea name="description" style="padding: 10px; border-radius: 5px; border: none; height: 100px;"></textarea>

                <button type="submit" style="background-color: #6A0DAD; color: #F3E8E2; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    Submit
                </button>
           </form>
        </div>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)
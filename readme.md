# Current Commands:

 - /fetchscript: Fetches Functions From A Static .py File Parsed With [BBTools](https://github.com/MorphRed/BBTools-py3)

# Hosting:

### Discord Application Setup:

1. Go to discord.dev and create a new application with a bot.

2. Enable both User Install and Guild Install in the installation tab

3. Ensure "application.commands" scope is selected for both

4. Optionally enable the bot scope for guild install, this isnt neccesary but allows the bot to show up in the member list

### Actual Hosting:

1. Clone the repo:
    ```shell
    git clone https://github.com/Noel-FGC/koko-bot.git
    ```
2. Set Up Node.js:
    ```
    npm install
    ```


3. Create a .env file with the following contents:
    ```
    TOKEN=(Your Bot Token Here)
    clientId=(Your Bots Client ID Here)
    # (and optionally)
    guildId=(Your Testing Guild ID Here)
   ```

4. Update Commands:
    ```
    node miscscripts/deploytoallguilds.js
    ```

5. Run The Bot:
    ```
    node .
    ```
    or
    ```
    node index.js
    ```

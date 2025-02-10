const { SlashCommandBuilder, InteractionContextType } = require('discord.js');
module.exports = {
  data: new SlashCommandBuilder()
    .setName('ping')
    .setDescription('Replies with Pong!')
    .setContexts(InteractionContextType.BotDM, InteractionContextType.Guild, InteractionContextType.PrivateChannel),
  async execute(interaction) {
    await interaction.reply('Pong!');
  },
};


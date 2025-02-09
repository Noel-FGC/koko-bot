const { InteractionContextType, SlashCommandBuilder } = require ('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
  .setName('userinstalltesting')
  .setDescription('User Install Testing')
  .setIntegrationTypes(0, 1)
  .setContexts(InteractionContextType.BotDM, InteractionContextType.Guild, InteractionContextType.PrivateChannel),

  async execute (interaction) {
    await interaction.reply({ content: 'TESTING', ephemeral: true });
  }
}

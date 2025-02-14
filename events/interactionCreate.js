const { Events, MessageFlags } = require('discord.js');

module.exports = {
  name: Events.InteractionCreate,
  async execute(interaction) {

    console.log(interaction)

    let command = interaction.client.commands.get(interaction.commandName);
      
    if (!command) {
      command = interaction.client.commands.get(interaction.message.interaction.commandName)
      if (!command) {
        return;
        console.error(`No command matching ${interaction.commandName} was found.`)
      }
    }
    if (interaction.isButton()) {
      try {
        let id = interaction.customId;
        await command.execute(interaction, id)
      } catch (error) {
        console.error(error);
        if (interaction.replied || interaction.deferred) {
          interaction.followUp({ content: 'There was an error with this interaction', flags: MessageFlags.Ephemeral });
        } else {
          interaction.reply({ content: 'There was an error with this interaction', flags: MessageFlags.Ephemeral });
        }
      }
    }
    if (interaction.isChatInputCommand()) {
      
      try {
        await command.execute(interaction);
      } catch (error) {
        console.error(error);
        if (interaction.replied || interaction.deferred) {
          await interaction.followUp({ content: `There was an error while executing this command!`, flags: MessageFlags.Ephemeral });
        } else {
          await interaction.reply({content: 'There was an error while executing this command!', flags: MessageFlags.Ephemeral });
        }
      }
    } else if (interaction.isAutocomplete()) {
      try {
        await command.autocomplete(interaction);
      } catch (error) {
        console.error(error);
      }
    }
  }
}


const { SlashCommandBuilder, InteractionContextType, EmbedBuilder, RichPresenceAssets } = require('discord.js');
const fs = require('node:fs');
const path = require('node:path');
const charfuncs = require('../../functions/imports.js');
require.extensions['.py'] = function (module, filename) {
	module.exports = fs.readFileSync(filename, 'utf8');
};

module.exports = {
  data: new SlashCommandBuilder()
    .setName('fetchscript')
    .setDescription('Replies with a script snippet')
   .setContexts(InteractionContextType.BotDM, InteractionContextType.Guild, InteractionContextType.PrivateChannel)
   .addStringOption(option =>
        option
          .setName('game')
          .setDescription('Which Game The Script Is From')
          .setRequired(true)
          .addChoices(
            { name: "BBCF2", value: "bbcf" },
            { name: "BBCF1", value: "bbcf1" },
            { name: "BBCF", value: "bbcf" },
            { name: "BBCPEX", value: "bbcpe" },
            { name: "BBCP", value: "bbcp" },
            { name: "BBCSE", value: "bbcse" },
            { name: "BBCS2", value: "bbcs2" },
            { name: "BBCS", value: "bbcs" },
            { name: "BBCT", value: "bbct" },
      )
    )
    .addStringOption(option =>
			option
				.setName('character')
				.setDescription('Character The Script Snippet Is In')
				.setRequired(true)
				.setAutocomplete(true)
    )
		.addStringOption(option =>
			option
				.setName('name')
				.setDescription('Name Of The Subroutine Or State')
				.setRequired(true)
		),






	async autocomplete(interaction) {
    const game = interaction.options.getString('game')
    const filter = interaction.options.getFocused();

    let choices = charfuncs.fetchCharacters(game, filter).slice(0, 25);
 
    try {
       await interaction.respond(
         choices.map(choice => ({ name: choice, value: choice })),
       );
    } catch (error) {
       console.error(error);
    }
  }, 
    async execute(interaction) {
      const game = interaction.options.getString('game');
      const state = `${interaction.options.getString('name')}` 
      const optCharacter = interaction.options.getString('character');
      

      const json = charfuncs.fetchJson(game);
      const characters = charfuncs.fetchCharacters(json); 
      const character = charfuncs.fetchCharacter(optCharacter, characters);
      const characterobj = charfuncs.fetchCharacterObj(character, json);


      let input = ' '
      const statedef = `def ${state}\\(\\):`

      if (state.startsWith('NmlAtk')) {
        input = state.slice(6, state.length)
      }
      
      let wikiurl = `https://dustloop.com/w/${game}`
      let url = characterobj.url
      let id = characterobj.id
      let color = characterobj.color
      let displayName = characterobj.displayName

      // I Am So Sorry To Whoever's Trying To Debug This
      // I Dont Know How It Works Either I Like Blacked Out For 6 Hours And Woke Up With This

      const script = require(path.resolve(path.join(__dirname, `../../GameAssets/${game}/scripts/char_${id}_scr/scr_${id}.py`))); 

      let tempscript = script

      const stateChar = script.search(statedef);

      let response = 'Unknown Error Has Occured'; // just incase it doesnt get set somehow
      let footer = ' ';

      if (stateChar == -1) {
        response = ('```\n' + `Definition Not Found In scr_${id}.py` + '\n```')
      } else {
        let endDecoratorChar = 0


        let decoratorChar = (stateChar - 12);

        tempscript = script.slice(decoratorChar, script.length);

        const decoratorOffset = (tempscript.search('@'))

        let tempdec = (decoratorChar + 1)

        decoratorChar += decoratorOffset

        tempscript = tempscript.slice(tempdec, tempscript.length)

        endDecoratorChar = script.slice((decoratorChar + 1), script.length).search('@');

        endDecoratorChar += decoratorChar

        responseNoSlice = ('```py\n' + script.slice(decoratorChar, endDecoratorChar - 1) + '\n```');
        response = ('```py\n' + script.slice(decoratorChar, (endDecoratorChar - 1)).slice(0, 4086) + '\n```');

        if (response.length < responseNoSlice.length) {
          footer = ('⚠️ Warning: Script Has Been Truncated To Fit In Character Limit');
        }

      }
      const embed = new EmbedBuilder()
        .setColor(color)
        .setTitle(displayName + ' -- ' + state)
        .setURL(wikiurl + '/' + url + '#' + input)
        .setAuthor({ name: game, iconURL: `https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/${game}_Logo.png`, url: wikiurl })
        .setDescription(response)
        .setThumbnail(`https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/chsele/${id}_chsele_icon.png`)
        .setFooter( { text: footer } )  

      await interaction.reply({ embeds : [embed] });
  },
};


const { SlashCommandBuilder, InteractionContextType, EmbedBuilder, RichPresenceAssets } = require('discord.js');
const fs = require('node:fs');
const path = require('node:path');


const bbcharacters = [
  {name: 'Ragna The Bloodedge', id: 'rg', url: 'Ragna_the_Bloodedge', color: 0xC30000},
  {name: 'Jin Kisaragi', id: 'jn', url: 'Jin_Kisaragi', color: 0x0A44F1},
  {name: 'Noel Vermillion', id: 'no', url: 'Noel_Vermillion', color: 0x0C9DEB},
  {name: 'Rachel Alucard', id: 'rc', url: 'Rachel_Alucard', color: 0xE34A46},
  {name: 'Taokaka', id: 'tk', url: 'Taokaka', color: 0xFFDB65},
  {name: 'Iron Tager', id: 'tg', url: 'Iron_Tager', color: 0xE26644},
  {name: 'Litchi Faye-Ling', id: 'lc', url: 'Litchi_Faye_Ling', color: 0xD03535},
  {name: 'Arakune', id: 'ar', url: 'Arakune', color: 0x746E62},
  {name: 'Bang Shishigami', id: 'bn', url: 'Bang_Shishigami', color: 0x555E1E},
  {name: 'Carl Clover', id: 'ca', url: 'Carl_Clover', color: 0x8058A4},
  {name: 'Hakumen', id: 'ha', url: 'Hakumen', color: 0xFFFFFF},
  {name: 'Nu-13', id: 'ny', url: 'Nu-13', color: 0x8D9EF1},
  {name: 'Lambda-11', id: 'rm', url: 'Lambda-11', color: 0xFFFCDB},
  {name: 'Tsubaki Yayoi', id: 'tb', url: 'Tsubaki_Yayoi', color: 0xFCD31A},
  {name: 'Hazama', id: 'hz', url: 'Hazama', color: 0x436B32},
  {name: 'Mu-12', id: 'mu', url: 'Mu-12', color: 0x5457C0},
  {name: 'Makoto Nanaya', id: 'mk', url: 'Makoto_Nanaya', color: 0xFF7B2E},
  {name: 'Valkenhayn R. Hellsing', id: 'vh', url: 'Valkenhayn_R._Hellsing', color: 0xC4BDAF},
  {name: 'Platinum The Trinity', id: 'pt', url: 'Platinum_the_Trinity', color: 0xEE9990},
  {name: 'Relius Clover', id: 'rl', url: 'Relius_Clover', color: 0xA33969},
  {name: 'Izayoi', id: 'iz', url: 'Izayoi', color: 0xFFC31E},
  {name: 'Amane Nishiki', id: 'am', url: 'Amane_Nishiki', color: 0xD41682},
  {name: 'Bullet', id: 'bl', url: 'Bullet', color: 0xA53716},
  {name: 'Azrael', id: 'az', url: 'Azrael', color: 0x627EC6},
  {name: 'Kagura Mutsuki', id: 'kg', url: 'Kagura_Mutsuki', color: 0x4E4743},
  {name: 'Yuuki Terumi', id: 'tm', url: 'Yuuki_Terumi', color: 0xEFCC42},
  {name: 'Kokonoe', id: 'kk', url: 'Kokonoe', color: 0xEF8091},
  {name: 'Celica A. Mercury', id: 'ce', url: 'Celica_A._Mercury', color: 0xD76253},
  {name: 'Hibiki Kohaku', id: 'hb', url: 'Hibiki_Kohaku', color: 0x5761EB},
  {name: 'Naoto Kurogane', id: 'nt', url: 'Naoto_Kurogane', color: 0xBB1A17},
  {name: 'Nine The Phantom', id: 'ph', url: 'Nine_the_Phantom', color: 0xA127A5},
  {name: 'Izanami', id: 'mi', url: 'Izanami', color: 0x552286},
  {name: 'Susano\'o', id: 'su', url: 'Susano\'o', color: 0x00A10E},
  {name: 'Es', id: 'es', url: 'Es', color: 0x4948E8},
  {name: 'Mai Natsume', id: 'ma', url: 'Mai_Natsume', color: 0x7173D4},
  {name: 'Jubei', id: 'jb', url: 'Jubei', color: 0xE0C37C}
];


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
            { name: "BBCF2", value: "BBCF" },
            { name: "BBCF1", value: "BBCF1" },
            { name: "BBCF", value: "BBCF" },
            { name: "BBCPEX", value: "BBCPEX" },
            { name: "BBCP", value: "BBCP" },
            { name: "BBCSE", value: "BBCSE" },
            { name: "BBCS2", value: "BBCS2" },
            { name: "BBCS", value: "BBCS" },
            { name: "BBCT", value: "BBCT" },
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

    console.log(game)
		
    if (game != "BBTAG") {

    var choices = bbcharacters.map(char => char.name); // return array with name property of each object in characters array

    if (game == "BBCT") { choices = choices.slice(0, 12) } else
    if (game == "BBCS") { choices = choices.splice(12, 1).slice(0, 15) } else // splice 12 to remove Nu-13
    if (game == "BBCS2") { choies = choices.splice(12, 1).slice(0, 18) } else
    if (game == "BBCSE" ) { choices = choices.splice(12, 1).slice(0, 19) } else
    if (game == "BBCP" ) { choices = choices.splice(13, 1).slice(0, 25) } else // splice 13 to remove Lambda-11
    if (game == "BBCPE" ) { choices = choices.slice(0, 28) } else
    if (game == "BBCF1" ) { choices = choices.slice(0, 35) } else
    if (game == "BBCF" ) { choices = choices }
   }
      const focusedValue = interaction.options.getFocused();
      const realfiltered = choices.filter(choice => choice.toLowerCase().startsWith(focusedValue.toLowerCase()));

      const	filtered = realfiltered.slice(0, 25);
        try {
        await interaction.respond(
          filtered.map(choice => ({ name: choice, value: choice })),
        );
      } catch (error) {
        console.error(error);
      }
    
    

	},
	async execute(interaction) {
    const game = interaction.options.getString('game')

    const character = interaction.options.getString('character')

    const characterobj = bbcharacters.filter(item => item.name === character)[0]

    const state = `${interaction.options.getString('name')}`
		const statedef = `def ${state}\\(\\):`

    let wikiurl = `https://dustloop.com/w/${game}`
    let page = characterobj.page
    let id = characterobj.id
    let color = characterobj.color

		console.log('state ' + state)

    // I Am So Sorry To Whoever's Trying To Debug This
    // I Dont Know How It Works Either I Like Blacked Out For 6 Hours And Woke Up With This

    const script = require(path.resolve(path.join(__dirname, `../../GameAssets/${game}/Char/char_${id}_scr/scr_${id}.py`))); 

		let tempscript = script

		const stateChar = script.search(statedef);

    let response = 'Unknown Error Has Occured'; // just incase it doesnt get set somehow
    let footer = ' ';

    if (stateChar == -1) {
      response = ('```\n' + `Definition Not Found In scr_${id}.py` + '\n```')
    } else {
      let endDecoratorChar = 0

      console.log('stateChar ' + stateChar)

      let decoratorChar = (stateChar - 12);
      console.log('decoratorChar ' + decoratorChar)


      tempscript = script.slice(decoratorChar, script.length);

      const decoratorOffset = (tempscript.search('@'))

      let tempdec = (decoratorChar + 1)

      decoratorChar += decoratorOffset

      console.log('decoratorChar ' + decoratorChar)

      console.log('tempscript.length', tempscript.length)

      tempscript = tempscript.slice(tempdec, tempscript.length)

      endDecoratorChar = script.slice((decoratorChar + 1), script.length).search('@');

      endDecoratorChar += decoratorChar

      console.log('endDecoratorChar ', endDecoratorChar)

      responseNoSlice = ('```py\n' + script.slice(decoratorChar, endDecoratorChar - 1) + '\n```');
      response = ('```py\n' + script.slice(decoratorChar, (endDecoratorChar - 1)).slice(0, 4086) + '\n```');

      if (response.length < responseNoSlice.length) {
        footer = ('⚠️ Warning: Script Has Been Truncated To Fit In Character Limit');
      }

    }
    const embed = new EmbedBuilder()
      .setColor(color)
      .setTitle(character + ' - ' + state)
      .setAuthor({ name: game, iconURL: `https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/${game}_Logo.png`, url: wikiurl })
      .setDescription(response)
      .setThumbnail(`https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/chsele/${id}_chsele_icon.png`)
      .setFooter( { text: footer } )  

    await interaction.reply({ embeds : [embed] });
  },
};


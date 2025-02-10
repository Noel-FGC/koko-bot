const { SlashCommandBuilder, InteractionContextType, EmbedBuilder, RichPresenceAssets } = require('discord.js');
const fs = require('node:fs');
const path = require('node:path');

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
		const choices = ['Ragna The Bloodedge', 'Jin Kisiragi', 'Noel Vermillion', 'Rachel Alucard', 'Taokaka', 'Iron Tager', 'Litchi Faye-Ling', 'Arakune', 'Bang Shishigami', 'Carl Clover', 'Hakumen', 'Nu-13', 'Lambda-11', 'Tsubaki Yayoi', 'Hazama', 'Mu-12', 'Makoto Nanaya', 'Valkenhayn R. Hellsing', 'Platinum The Trinity', 'Relius Clover', 'Izayoi', 'Amane Nishiki', 'Bullet', 'Azrael', 'Kagura Mutsuki', 'Yuuki Terumi', 'Kokonoe', 'Celica A. Mercury', 'Hibiki Kohaku', 'Naoto Kurogane', 'Nine The Phantom', 'Izanami', 'Susano\'o', 'Es', 'Mai Natsume', 'Jubei'];
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
		//const game = interaction.options.getSubcommand().toUpperCase()

    const game = interaction.options.getString('game')

    const character = interaction.options.getString('character')

    const state = `${interaction.options.getString('name')}`
		const statedef = `def ${state}\\(\\):`

    let wikiurl = `https://dustloop.com/w/${game}`
    let page = 'Ragna_the_Bloodedge'

		console.log('state ' + state)

		let id = 'rg';
		switch(character) {
		case 'Ragna The Bloodedge':
      page='Ragna_the_Bloodedge'
			id='rg'
			break;
		case 'Jin Kisiragi':
      page='Jin_Kisiragi'
			id='jn'
			break;
		case 'Noel Vermillion':
      page='Noel_Vermillion'
			id='no'
			break;
		case 'Rachel Alucard':
      page='Rachel_Alucard'
			id='rc'
			break;
		case 'Taokaka':
      page='Taokaka'
			id='tk'
			break;
		case 'Iron Tager':
			page='Iron_Tager'
      id='tg'
			break;
		case 'Litchi Faye-Ling':
			page='Litchi_Faye_Ling'
      id='lc'
			break;
		case 'Arakune':
      page='Arakune'
			id='ar'
			break;
		case 'Bang Shishigami':
			page='Bang_Shishigami'
      id='bn'
			break;
		case 'Carl Clover':
      page='Carl_Clover'
			id='ca'
			break;
		case 'Hakumen':
      page='Hakumen'
			id='ha'
			break;
		case 'Nu-13':
      page='Nu-13'
			id='ny'
			break;

		case 'Lambda-11':
      page='Lambda-11'
			id='rm'
			break;
		case 'Tsubaki Yayoi':
      page='Tsubaki_Yayoi'
			id='tb'
			break;
		case 'Hazama':
      page='Hazama'
			id='hz'
			break;
		case 'Mu-12':
      page='Mu-12'
			id='mu'
		case 'Makoto Nanaya':
      page='Makoto_Nanaya'
			id='mk'
			break;
		case 'Valkenhayn R. Hellsing':
      page='Valkenhayn_R._Hellsing'
			id='vh'
			break;
		case 'Platinum The Trinity':
      page='Platinum_the_Trinity'
			id='pt'
			break;
		case 'Relius Clover':
      page='Relius_Clover'
			id='rl'
			break;

		case 'Izayoi':
      page='Izayoi'
			id='iz'
			break;
		case 'Amane Nishiki':
      page='Amane_Nishiki'
			id='am'
			break;
		case 'Bullet':
      page='Bullet'
			id='bl'
			break;
		case 'Azrael':
      page='Azrael'
			id='az'
			break;
		case 'Kagura Mutsuki':
      page='Kagura_Mutsuki'
			id='kg'
			break;
		case 'Yuuki Terumi':
      page='Yuuki_Terumi'
			id='tm'
			break;
		case 'Kokonoe':
      page='Kokonoe'
			id='kk'
			break;
		case 'Celica A. Mercury':
      page='Celica_A._Mercury'
			id='ce'
			break;

		case 'Hibiki Kohaku':
      page='Hibiki_Kohaku'
			id='hb'
			break;
		case 'Naoto Kurogane':
      page='Naoto_Kurogane'
			id='nt'
			break;
		case 'Nine The Phantom':
      page='Nine_the_Phantom'
			id='ph'
			break;
		case 'Izanami':
      page='Izanami'
			id='mi'
			break;
		case 'Susano\'o':
      page='Susano\'o'
			id='su'
			break;
		case 'Es':
      page='Es'
			id='es'
			break;
		case 'Mai Natsume':
      page='Mai_Natsume'
			id='ma'
			break;
		case 'Jubei':
      page='Jubei'
			id='jb'
			break;
	}	




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
      
      tempdecorator = (decoratorChar + 1)

      console.log('tempdecorator', tempdecorator)

      console.log('tempscript.length', tempscript.length)

      tempscript = tempscript.slice(tempdec, tempscript.length)

      endDecoratorChar = script.slice((decoratorChar + 1), script.length).search('\@');

      endDecoratorChar += decoratorChar

      console.log('endDecoratorChar ', endDecoratorChar)

      responseNoSlice = ('```py\n' + script.slice(decoratorChar, endDecoratorChar - 1) + '\n```');
      response = ('```py\n' + script.slice(decoratorChar, (endDecoratorChar - 1)).slice(0, 4086) + '\n```');

      if (response.length < responseNoSlice.length) {
        footer = ('⚠️ Warning: Script Has Been Truncated To Fit In Character Limit');
      }

    }
    const embed = new EmbedBuilder()
      .setColor(0x65a4f2)
      .setTitle(character + ' - ' + state)
      .setAuthor({ name: game, iconURL: `https://github.com/Noel-FGC/koko-bot/GameAssets/${game}/${game}_Logo.png`, url: wikiurl })
      .setDescription(response)
      .setThumbnail(`https://github.com/Noel-FGC/koko-bot/GameAssets/${game}/chsele/${id}_chsele_icon.png?raw=true`)
      .setFooter( { text: footer } )  

    await interaction.reply({ embeds : [embed] });
  },
};


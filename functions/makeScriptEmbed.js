const { EmbedBuilder, ButtonBuilder, ButtonStyle, ActionRowBuilder } = require('discord.js')
const charfuncs = require('./characters.js')

const nextPage = new ButtonBuilder()
  .setCustomId('next')
  .setLabel('Next')
  .setStyle(ButtonStyle.Secondary);
const prevPage = new ButtonBuilder()
  .setCustomId('previous')
  .setLabel('Back')
  .setStyle(ButtonStyle.Secondary);
const row = new ActionRowBuilder()
  .addComponents(prevPage, nextPage);

module.exports = {
  makeScriptEmbed(optScript, characterObj, state, game, page) {
    let displayName = characterObj.name
    let wiki = `https://dustloop.com/w/${game}`
    let id = characterObj.id
    let script = optScript.trim()
    let offset = 0
    let footer = ' '

    if (characterObj.displayName !== undefined) {
      displayName = characterObj.displayName
    }

    if (script.length >= 4086 && page === undefined) {      
      page = 0
    }

    if (page !== undefined) {
      footer = '⚠️ Warning: Script Has Been Truncated To Fit In Character Limit'
      for(let i = 0; i <= page; i++) {


        console.log(`\n\n${i}\n\n`)
        script = optScript.trim().slice(offset, (offset + 4086))
        console.log(`\n\n${script}\n\n`)
        let scriptArray = script.split('\n');
        let lastArrayLine = (scriptArray.length - 1)
        let lastLine = scriptArray[lastArrayLine]
        console.log(`\n\n${lastLine}\n\n`)
        script = script.slice(0, (script.length - lastLine.length)).trim()
        console.log(`\n\n${script}\n\n`)


        offset += script.length
        console.log(`\n\n${offset}\n\n`)
      } 
    }



    const embed = new EmbedBuilder()
      .setColor(characterObj.color)
      .setTitle(`${displayName} -- ${state}`)
      .setURL(`${wiki}/${characterObj.url}`)
      .setAuthor({ name: game, iconURL: `https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/${game}_Logo.png`, url: wiki})
      .setDescription('```py\n' + script + '\n```')
      .setThumbnail(`https://raw.githubusercontent.com/Noel-FGC/koko-bot/refs/heads/master/GameAssets/${game}/chsele/${id}_chsele_icon.png`)
      .setFooter( { text: footer } )





    return { embeds: [embed], components: [row], withResponse: true, };
  }
}

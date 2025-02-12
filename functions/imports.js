const fs = require('node:fs');
const path = require('node:path');

function fetchJson (game) {
  if (game != "BBTAG") {
    let data = require(path.resolve(path.join(__dirname, '../GameAssets/BB/characters.json')));
    
    
    if ( game == "BBCS" || game == "BBCS2" || game == "BBCSE" ) {
      let lambdaIndex = data.findIndex(item => item.name == "Lambda-11");
      data[lambdaIndex].id = 'ny'
    }

    return data;
  }
}
function fetchCharacters (gameorjson, filter) {
  let game = "BB";
  let json = {};

  if (typeof gameorjson == 'string') {
    game = gameorjson 
    json = fetchJson(game)
  } else if (typeof gameorjson == 'object' ) {
    json = gameorjson
  }

  let characters = json.map(char => char.name);


  // realistically each of these should be their own json but i dont care 
  
  switch(game) {
    case "BBCT":
      characters = characters.slice(0, 12);
      break;
    case "BBCS":
      characters.splice(11, 1) // Splice 11 to remove Nu-13
      characters = characters.slice(0, 15);
      break;
    case "BBCS2":
      characters.splice(11, 1);
      characters = characters.slice(0, 18)
      break;
    case "BBCSE":
      characters.splice(11, 1);
      characters = characters.slice(0, 19)
      break;
    case "BBCP":
      characters.splice(12, 1) // Splice 13 to remove Lambda-11
      characters.slice(0, 25);
      break;
    case "BBCPE":
      characters = characters.slice(0, 28);
      break;
    case "BBCF1":
      characters = characters.slice(0, 35);
      break;
    case "BBCF":
      characters = characters
      break;
  }


  if (filter != undefined) {
    characters = characters.filter(char => char.toLowerCase().includes(filter.toLowerCase()));
  }
 
  return characters;
}

function fetchCharacter(character, gameorjsonorcharacters) {
  let json = {}
  let characters = []
  
  if (typeof gameorjsonorcharacters == 'string') {
    json = fetchJson(gameorjson)
  } else if (typeof gameorjsonorcharacters == 'object' ) {
    if (typeof gameorjsonorcharacters[1] == 'string') {
      characters = gameorjsonorcharacters
    } else if (typeof gameorjsonorcharacters[1].name == 'string') {
      json = gameorjsonorcharacters
    }
  }

  const filteredchar = characters.filter(entry => entry.toLowerCase().includes(character.toLowerCase()))[0].toString();
  return filteredchar
}

function fetchCharacterObj(character, gameorjson) {


  let json = ''

  if (typeof gameorjson == 'string') {
    json = fetchJson(gameorjson)
  } else if (typeof gameorjson == 'object') {
    json = gameorjson
  }

  let object = json.filter(entry => entry.name == character)[0]
  
  if (object.displayName == undefined) {
    object.displayName = object.name
  }

  return object;
}


function updateJson (characters) {
  fs.writeFile(path.resolve(path.join(__dirname, '/../GameAssets/BB/characters.json')), JSON.stringify(characters, null, 2), err => { 
    if (err) {
      console.error(err);
      return err;
    } else {
      return true;
    }
  })
}

module.exports = { fetchJson, fetchCharacters, fetchCharacterObj, fetchCharacter, updateJson }

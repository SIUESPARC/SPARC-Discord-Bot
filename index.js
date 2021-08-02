// install the needed classes
const { Client, Intents } = require('discord.js');
const dotenv = require('dotenv');

dotenv.config();

// create a new Discord client
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
	console.log('Ready!');
});

// login to Discord with your app's token
client.login(process.env.TOKEN);
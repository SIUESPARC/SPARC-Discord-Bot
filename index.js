// install the needed classes
const { Client, Intents } = require('discord.js');
const dotenv = require('dotenv');
const { MongoClient } = require('mongodb');

dotenv.config();

const uri = `mongodb+srv://m001-student:${process.env.MONGOPASS}@sandbox.asihp.mongodb.net/db?retryWrites=true&w=majority`;

// create a new Discord client
const mongo = new MongoClient(uri);

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

// when the client is ready, run this code
// this event will only trigger one time after logging in
client.once('ready', () => {
	console.log('Ready!');
});

client.on('interactionCreate', interaction => {
	console.log(interaction);
});

client.on('message', msg => {
	if (msg.content === 'ping') {
		msg.reply('pong');
	}
});

// login to Discord with your app's token
client.login(process.env.TOKEN);
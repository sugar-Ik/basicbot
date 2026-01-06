const { Telegraf } = require("telegraf");

// Replace with your bot token from BotFather
const bot = new Telegraf("6208314828:AAFv6m6kfJHY6rJsmWDcrRQNfWM7nkbBPV4");

// Respond to /start command
bot.start((ctx) => {
  ctx.reply("Hello!");
});

// Optional: Respond to any text message (for testing)
bot.on("text", (ctx) => {
  ctx.reply("You said: " + ctx.message.text);
});

// Launch the bot (uses polling to receive updates)
bot.launch();

console.log("Bot is running!");

// Graceful stop (Ctrl+C)
process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));

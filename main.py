import os
import time
import json
import keyboard
import requests
from typing import List
from colorama import init, Fore, Style

init()

class XBL:

    def __init__(self, xbl_token: str) -> None:
        self.xbl_token = xbl_token

    def get_user_friends(self, gamertag: str) -> List[str]:
        xuid = self.__gamertag_to_xuid(gamertag)
        if not xuid:
            return []
        
        url = f'https://xbl.io/api/v2/friends/{xuid}'
        headers = {
            'X-Authorization': self.xbl_token,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status() 
            data = response.json()
            return self.__get_friends_gamertag(data)
        except requests.exceptions.RequestException as e:
            print(Fore.LIGHTRED_EX + f' [-] Error retrieving friends for {gamertag}: {e}' + Style.RESET_ALL)
            return []

    def __get_friends_gamertag(self, data: dict) -> List[str]:
        return [friend.get('gamertag') for friend in data.get('people', [])]

    def __gamertag_to_xuid(self, gamertag: str) -> str:
        url = f'https://xbl.io/api/v2/search/{gamertag}'
        headers = {
            'X-Authorization': self.xbl_token,
            'Content-Type': 'application/json'
        }

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return str(data['people'][0]['xuid'])
        except (requests.exceptions.RequestException, IndexError, KeyError) as e:
            print(Fore.LIGHTRED_EX + f' [-] Error retrieving XUID for {gamertag}: {e}' + Style.RESET_ALL)
            return ''

    @staticmethod
    def save_gamertags_to_file(gamertags: List[str], file_path: str) -> None:
        with open(file_path, 'a') as file:
            file.write('\n'.join(gamertags) + '\n')

    @staticmethod
    def run():
        os.system('cls')
        logo = Fore.LIGHTMAGENTA_EX + '''
 __  _____ _    ___
 \ \/ / _ ) |  / __| __ _ _ __ _ _ __ _ __  ___ _ _
  >  <| _ \ |__\__ \/ _| '_/ _` | '_ \ '_ \/ -_) '_|
 /_/\_\___/____|___/\__|_| \__,_| .__/ .__/\___|_|
                                |_|  |_|  

 Telegram: @c0daxy | Discord: @codaxy
        ''' + Style.RESET_ALL
        print(logo)
        initial_gamertag = input(' Enter initial gamertag: ')
        with open('resources/constants.json') as f:
            data = json.load(f)
        xbox = XBL(data['XBL_API_KEY'])
        queue = [initial_gamertag]
        processed_gamertags = set()
        while True:
            if keyboard.is_pressed(' '):
                print('Pressed space. Closing the program...')
                break
            
            current_gamertag = queue.pop(0)
            if current_gamertag in processed_gamertags:
                continue

            friends = xbox.get_user_friends(current_gamertag)
            processed_gamertags.add(current_gamertag)
            print(Fore.LIGHTGREEN_EX + f' [+] {current_gamertag} -> {len(friends)} friends found' + Style.RESET_ALL)
            
            if not os.path.exists('output'):
                os.makedirs('output')

            XBL.save_gamertags_to_file(friends, 'output/gamertags.txt')
            queue.extend(friends)
            time.sleep(0.5)

if __name__ == '__main__':
    XBL.run()

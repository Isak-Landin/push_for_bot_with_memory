import cv2, time, pyautogui, PIL, json, pyperclip, importlib, keyboard, sys, random

from GrindGoatHorn_.main import GrindingExecution as bot


class Clients:
    def __init__(self):
        self.regions = list(pyautogui.locateAllOnScreen('open_screen.png', grayscale=True, confidence=0.94))

    def find_each_region(self):
        return self.regions


class Accounts:
    def __init__(self, accounts, regions):
        self.accounts = accounts
        self.regions = regions
        self.counter = 0
        self.account_memory = []
        """
        for i in self.regions:
            self.center = pyautogui.center(i)
            pyautogui.moveTo(self.center)
        """

    def execute_logins(self):

        for specific_region in self.regions:
            existing_user = list(pyautogui.locateOnScreen('existing_user.png', region=specific_region, confidence=0.95))
            center_existing_user = pyautogui.center(existing_user)

            pyautogui.moveTo(center_existing_user, duration=0.5)
            pyautogui.click()

            pyautogui.write(self.accounts[self.counter][0], interval=0.1)
            pyautogui.hotkey('altright', '2')
            pyautogui.write(self.accounts[self.counter][1], interval=0.1)

            pyautogui.press('tab')
            pyautogui.write(self.accounts[self.counter][2], interval=0.1)
            pyautogui.press('enter')

            account_location = [self.accounts[self.counter][0] + "@" + self.accounts[self.counter][1], specific_region]
            self.account_memory.append(account_location)

            self.counter += 1

    def click_to_play(self):
        self.location_click_to_play = pyautogui.locateAllOnScreen('click_to_play.png', confidence=0.95)

        for specific_button in self.location_click_to_play:
            center = pyautogui.center(specific_button)

            pyautogui.moveTo(center, duration=0.4)
            pyautogui.click()


time.sleep(10)
clients_var = Clients()
saved_client_regions = clients_var.find_each_region()
print(saved_client_regions)

list_of_accounts = [["jdwbieut59", "hotmail.com", "hnwvd71"], ["wmrhwfhn61", "outlook.com", "bhsvi39"],
                    ["helghfah17", "opera.com", "wdsha45"], ["ggetjaco62", "opera.com", "rqdes11"]]

Acc2 = Accounts(list_of_accounts, saved_client_regions)
Acc2.execute_logins()

print(Acc2.account_memory)
pyautogui.moveTo((1, 1), duration=0.2)

breaker_condition = 0

# Looks for click to play button on all of screen
while True:
    click_to_play_buttons_active = list(pyautogui.locateAllOnScreen('click_to_play.png', confidence=0.95))

    # Checks if each client is logged in
    if len(saved_client_regions) == len(click_to_play_buttons_active) or breaker_condition > 200:
        for i in click_to_play_buttons_active:
            click_to_play_buttons_active_center = pyautogui.center(i)
            pyautogui.moveTo(click_to_play_buttons_active_center, duration=0.2)
            pyautogui.click()
            breaker_condition = 0
        break

    breaker_condition += 1
    print(breaker_condition)

while True:
    click_to_play_buttons_active = pyautogui.locateOnScreen('click_to_play.png', confidence=0.90)
    if click_to_play_buttons_active is None:
        break
    breaker_condition += 1
    print("------------------------------------")
    print(breaker_condition)

for i in saved_client_regions:

    bot.set_up_view(region_to_act=i)
    bot.is_no_horns(region_to_act=i)
    bot.click_goat_horn(region_to_act=i)
    bot.grind_goat_horn(region_to_act=i)

while True:
    is_horn_in_first_client = pyautogui.locateOnScreen('Horn.png', region=saved_client_regions[0], confidence=0.85)
    if is_horn_in_first_client is None:
        time.sleep(random.randint(10, 30) / 10)
        break

logout_counter = 140
while True:

    for i in saved_client_regions:
        bot.bank_dust(region_to_act=i)
        bot.withdraw_horns(region_to_act=i)
        bot.click_goat_horn(region_to_act=i)
        bot.grind_goat_horn(region_to_act=i)


    logout_counter += 1

    if logout_counter > random.randint(90, 130):
        for i in saved_client_regions:
            bot.log_out(i)
        time.sleep(random.randint(10, 20))
        Acc2.counter = 0
        Acc2.execute_logins()

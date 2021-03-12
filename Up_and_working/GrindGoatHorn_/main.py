import pyautogui
import time
import random
import keyboard
import sys
import cv2


class GrindingExecution:
    @staticmethod
    def random_time(a, b):
        tal = random.randint(a, b) / 100
        return tal

    @staticmethod
    def click_goat_horn(region_to_act):
        # locate the horns on screen
        goatHornPos = pyautogui.locateOnScreen('Horn.png', region=region_to_act, confidence=0.8)

        # centralize the cursor on the goathorn
        goatHornCenter = pyautogui.center(goatHornPos)

        # Make position into list
        goatHornCenterList = list(goatHornCenter)

        # create offsets and add to clicks
        goatHornCenterList[0] = goatHornCenterList[0] + random.randint(-4, 4)
        goatHornCenterList[1] = goatHornCenterList[1] + random.randint(-3, 3)

        goatHornCenterTuple = tuple(goatHornCenterList)

        pyautogui.moveTo(goatHornCenterTuple, duration=GrindingExecution.random_time(20, 60))
        pyautogui.click()

        time.sleep(0.5)

    @staticmethod
    def grind_goat_horn(region_to_act):
        # Find pos of pestle and mortar
        pestlePos = pyautogui.locateOnScreen('pestleAndMortar.png', region=region_to_act, confidence=0.9)

        # Find center pos of pestle in pix
        pestlePosCenter = pyautogui.center(pestlePos)

        # make position into list
        pestlePosCenterList = list(pestlePosCenter)

        # add offset and click pestle
        pestlePosCenterList[0] = pestlePosCenterList[0] + random.randint(-6, 6)
        pestlePosCenterList[1] = pestlePosCenterList[1] + random.randint(-6, 6)

        pestlePosCenterTuple = tuple(pestlePosCenterList)

        pyautogui.click(pestlePosCenterTuple)

    @staticmethod
    def bank_dust(region_to_act):

        # find banker
        posBanker = pyautogui.locateOnScreen('banker.png', region=region_to_act, confidence=0.7)

        if posBanker is None:
            posBanker = pyautogui.locateOnScreen('window_banker.png', region=region_to_act, confidence=0.6)

            if posBanker is None:
                posBanker = pyautogui.locateOnScreen('body_bench.png', region=region_to_act, confidence=0.6)

                if posBanker is None:
                    posBanker = pyautogui.locateOnScreen('banker1.png', region=region_to_act, confidence=0.6)

                    if posBanker is None:
                        posBanker = pyautogui.locateOnScreen('banker2.png', region=region_to_act, confidence=0.6)

                        if posBanker is None:
                            posBanker = pyautogui.locateOnScreen('banker3.png', region=region_to_act, confidence=0.6)

                            if posBanker is None:
                                posBanker = pyautogui.locateOnScreen('banker4.png', region=region_to_act,
                                                                     confidence=0.6)
                                if posBanker is None:
                                    posBanker = pyautogui.locateOnScreen('banker5.png', region=region_to_act,
                                                                         confidence=0.6)

        posBankerCenter = pyautogui.center(posBanker)

        # make pos list
        posBankerCenterList = list(posBankerCenter)

        # change clickbox
        posBankerCenterList[1] += random.randint(8, 15)
        posBankerCenter = tuple(posBankerCenterList)
        pyautogui.moveTo(posBankerCenter, duration=GrindingExecution.random_time(20, 60))
        time.sleep(GrindingExecution.random_time(10, 30))
        pyautogui.click(posBankerCenter)

        # Withdraw fresh horns after depositing dust
        hornDustPos = pyautogui.locateOnScreen('hornDust.png', region=region_to_act, confidence=0.9)
        hornDustPosCenter = pyautogui.center(hornDustPos)

        # make position into list
        hornDustPosCenterList = list(hornDustPosCenter)

        # create offset and click
        hornDustPosCenterList[0] += random.randint(-4, 4)
        hornDustPosCenterList[1] += random.randint(-3, 3)

        hornDustPosCenter = tuple(hornDustPosCenterList)

        pyautogui.moveTo(hornDustPosCenter, duration=GrindingExecution.random_time(20, 60))
        time.sleep(GrindingExecution.random_time(10, 20))
        pyautogui.rightClick()

        # Find deposit all function
        depositAllPos = pyautogui.locateOnScreen('depositAll.png', region=region_to_act, confidence=0.8)
        allButtonActivated = pyautogui.locateOnScreen('all_button_activated.png', region=region_to_act, confidence=0.92)

        # Om "deposit all aktiv" inte kan hittas.... tryck på "all" knappen om den inte är aktiv, sen på dustet
        if depositAllPos is None:

            # Om "all knapp inaktiv"
            if allButtonActivated is None:

                allButtonDeactivated = pyautogui.locateOnScreen('all_button_deactivated.png', region=region_to_act, confidence=0.92)
                allButtonDeactivatedCenter = pyautogui.center(allButtonDeactivated)

                pyautogui.moveTo(allButtonDeactivatedCenter, duration=0.6)
                pyautogui.click()

                pyautogui.moveTo(hornDustPosCenter, GrindingExecution.random_time(30, 80))
                pyautogui.click()

            # Om "all knapp aktiv"
            elif allButtonActivated is not None:

                pyautogui.moveTo(hornDustPosCenter, duration=GrindingExecution.random_time(30, 40))
                pyautogui.click()



        else:
            depositAllPosCenter = pyautogui.center(depositAllPos)
            pyautogui.moveTo(depositAllPosCenter, duration=GrindingExecution.random_time(10, 30))
            time.sleep(GrindingExecution.random_time(30, 70))
            pyautogui.click()

    @staticmethod
    def withdraw_horns(region_to_act):

        # find banked hornstack
        hornPos = pyautogui.locateOnScreen('banked_horn.png', region=region_to_act, confidence=0.75)

        if hornPos is None:
            hornPos = pyautogui.locateOnScreen('banked_horn_semi_full.png', region=region_to_act, confidence=0.75)

            if hornPos is None:
                hornPos = pyautogui.locateOnScreen('banked_horn_full.png', region=region_to_act, confidence=0.75)

                if hornPos is None:
                    hornPos = pyautogui.locateOnScreen('k_stack.png', region=region_to_act, confidence=0.75)

                    if hornPos is None:
                        hornPos = pyautogui.locateOnScreen('bottom_of_stack.png', region=region_to_act, confidence=0.7)

        hornPosCenter = pyautogui.center(hornPos)

        # create offset
        hornPosCenterList = list(hornPosCenter)

        hornPosCenterList[0] += random.randint(-100, 100) / 100
        hornPosCenterList[1] += random.randint(-100, 100) / 100

        hornPosCenter = tuple(hornPosCenterList)

        # Move to and click out the horns
        pyautogui.moveTo(hornPosCenter, duration=GrindingExecution.random_time(30, 80))
        pyautogui.rightClick()

        time.sleep(GrindingExecution.random_time(16, 100))

        # Locate "withdraw all" and click
        withdrawAllPos = pyautogui.locateOnScreen('withdraw_all.png', region=region_to_act, confidence=0.7)
        withdrawAllCenter = pyautogui.center(withdrawAllPos)

        pyautogui.moveTo(withdrawAllCenter, duration=GrindingExecution.random_time(8, 40))

        time.sleep(GrindingExecution.random_time(10, 30))

        pyautogui.click()

        # Locate exit button
        exitButtonPos = pyautogui.locateOnScreen('exit_bank.png', region=region_to_act, confidence=0.9)
        exitButtonPosCenter = pyautogui.center(exitButtonPos)

        # Create offset
        exitButtonPosCenterList = list(exitButtonPosCenter)

        exitButtonPosCenterList[0] += random.randint(-300, 300) / 100
        exitButtonPosCenterList[1] += random.randint(-300, 300) / 100

        exitButtonPosCenter = tuple(exitButtonPosCenterList)

        # Move to exit and click
        pyautogui.moveTo(exitButtonPosCenter, duration=GrindingExecution.random_time(30, 45))
        pyautogui.click()

    @staticmethod
    def log_out(region_to_act):
        # Logout icon
        log_out_button = pyautogui.locateOnScreen('log_out.png', region=region_to_act, confidence=0.9)
        log_out_button_center = pyautogui.center(log_out_button)
        log_out_button_center_list = list(log_out_button_center)

        log_out_button_center_list[0] += random.randint(-3, 3)
        log_out_button_center_list[1] += random.randint(-4, 4)

        log_out_button_center = tuple(log_out_button_center_list)

        pyautogui.moveTo(log_out_button_center, duration=random.randint(40, 100)/100)
        pyautogui.click()

        # Red Logout button
        log_out_red = pyautogui.locateOnScreen('log_out_red.png', region=region_to_act, confidence=0.9)
        log_out_red_center = pyautogui.center(log_out_red)

        log_out_red_center_list = list(log_out_red_center)

        log_out_red_center_list[0] += random.randint(-14, 14)
        log_out_red_center_list[1] += random.randint(-5, 5)

        log_out_red_center = tuple(log_out_red_center_list)

        pyautogui.moveTo(log_out_red_center, duration= random.randint(20, 50)/100)
        pyautogui.click()

    @staticmethod
    def set_up_view(region_to_act):

        inventory = pyautogui.locateOnScreen('inventory_red.png', region=region_to_act, confidence=0.95)
        if inventory is None:
            inventory = pyautogui.locateOnScreen('inventory_grey.png', region=region_to_act, confidence=0.95)

        inventory_center = pyautogui.center(inventory)
        inventory_list = list(inventory_center)

        inventory_list[0] += random.randint(-5, 5)
        inventory_list[1] += random.randint(-5, 5)

        inventory_center = tuple(inventory_list)

        pyautogui.moveTo(inventory_center, duration=random.randint(10, 30) / 100)
        pyautogui.click()

        compass = pyautogui.locateOnScreen('compass.png', confidence=0.93)
        if compass is None:
            compass = pyautogui.locateOnScreen('compass2.png', confidence=0.9)

        compass_center = pyautogui.center(compass)
        compass_center_list = list(compass_center)

        compass_center_list[0] += random.randint(-4, 4)
        compass_center_list[1] += random.randint(-4, 4)

        compass_center = tuple(compass_center_list)

        pyautogui.moveTo(compass_center, duration=random.randint(10, 20) / 100)
        pyautogui.click()

        pyautogui.keyDown('down')
        time.sleep(2)
        pyautogui.keyUp('down')

        while True:
            pyautogui.keyDown('left')
            time.sleep(random.randint(25, 95) / 1000)
            pyautogui.keyUp('left')
            if pyautogui.locateOnScreen('banker.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker1.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker2.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker3.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker4.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker5.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('banker6.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('window_banker.png', region=region_to_act, confidence=0.82) is None:
                pass
            else:
                break
            if pyautogui.locateOnScreen('body_bench.png', region=region_to_act, confidence=0.82) is None:
                continue
            else:
                break

    @staticmethod
    def is_no_horns(region_to_act):
        horn = pyautogui.locateOnScreen('Horn.png', region=region_to_act, confidence=0.9)
        if horn is None:
            GrindingExecution.bank_dust(region_to_act=region_to_act)
            GrindingExecution.withdraw_horns(region_to_act=region_to_act)


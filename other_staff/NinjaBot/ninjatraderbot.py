from lackey import *
import time
import schedule

a = "C:\\go.log"
Debug.setLogFile(a)

Settings.MinSimilarity = 0.55


def open_platform():
	wait("header_of_platform.png", 5)
	doubleClick("file_button.png")
	wait("connect_hover.png", 5)
	hover("connect_hover.png")
	wait("cqg_connect.png", 5)
	click("cqg_connect.png")
	wait("connecting_in_progress.png", 30)
	wait("account_selector.png", 120)#("connection_success.png", 120)
	print("Connection success!!!")
	wait("account_selector.png", 5)
	click("account_selector_drop_down.png")
	wait("account_selector_opened.png", 5)
	click("account_select_demo_acc.png")
	wait("check_demo_acc_selector.png", 5).similar(0.55)
	print("Demo acc was set!")
	highlight("account_select_demo_acc.png")


print(Settings.MinSimilarity)

wait("check_demo_acc_selector.png", 5).similar(0.55)
open_platform()



def printera():
	print("Runned!")





#schedule.every(1).minutes.do(printera)


#while True:
    #schedule.run_pending()
    #time.sleep(1)





import random
import os
import time
def cleanChat_GLOBAL():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
        
cleanChat_GLOBAL()
class PlayTable_C:
    continuePlaying:bool = True
    playerMarkTimes:int = 0
    MarksInThisMatch:int = 0
    botMarkTimes:int = 0
    MatchTimes:int = 0
    Player1Name:str = ""
    boardMap = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "],
]
    Player1Symbol = "X"
    Player2Symbol = "O"
    __MIN_NICKNAME_LENGTH__ = 3
    __MAX_NICKNAME_LENGTH__ = 25
    def __init__(self):
        self.Player1Name = os.getlogin()     
    def checkNickname(self, nickname:str):
        if len(nickname) < self.__MIN_NICKNAME_LENGTH__:
            return f"The minimum length of nickname is {self.__MIN_NICKNAME_LENGTH__}."
        elif (len(nickname) > self.__MAX_NICKNAME_LENGTH__):
            return  f"The max length of nickname is {self.__MAX_NICKNAME_LENGTH__}."
        else:
            return True
        
    def confirmStartGame(self):
        print(f"Hello {self.Player1Name}")
        while True:
            readyToPlay=input("You Are Ready to Play? y/N ").capitalize()
            if (readyToPlay != "N"):
                break
        return
    @staticmethod
    def __SANITIZE_DIFICULTY_SELECT__(userInput):
        if userInput != "1" and userInput != "2" and userInput != "3":
            return {'isError': True, "Message": "Please select a valid difficulty, from 1 to 3."}
        message = ""
        if (userInput == "1"):
            message = "You Have Selected 1 - Easy"
        elif userInput == "2":
            message = "You Have Selected 2 - Medium"
        else:
            message = "You Have Selected 3 - Hard"
        return {
            "isError": False, "Message": message
        }
    @staticmethod
    def verifySelectedColumn(userInput):
        if userInput == "" or int(userInput) > 3 or userInput == None:
            return False
        return True

    def selectGameDificulty(self):
        while True:
            print("Select Dificult.")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard\n")
            dificult = input("-> ")
            sanitizeDificultResult = self.__SANITIZE_DIFICULTY_SELECT__(dificult)
            if sanitizeDificultResult['isError'] == False:
                cleanChat_GLOBAL()
                print(sanitizeDificultResult["Message"])
                time.sleep(0.8)
                break
            print(sanitizeDificultResult["Message"])
            time.sleep(1.4)
    def verifyWin(self):
        for i in range(3):
            if self.boardMap[i][0] == self.boardMap[i][1] == self.boardMap[i][2] and self.boardMap[i][0] != " ":
                if self.boardMap[i][0] == "X":
                    return {
                        "finished": True,
                        "message": f"{self.Player1Name} Wins!"
                    }
                else:
                    return {
                        "finished": True,
                        "message": "Player 2 (BOT) Wins!"
                    }
        for i in range(3):
            if self.boardMap[0][i] == self.boardMap[1][i] == self.boardMap[2][i] and self.boardMap[0][i] != " ":
                if self.boardMap[i][0] == "X":
                    return {
                    "finished": True,
                    "message": f"{self.Player1Name} Wins!"
                    }
                else:
                    return {
                        "finished": True,
                     "message": "Player 2 (BOT) Wins!"
                    }
        if (self.boardMap[0][0] == self.boardMap[1][1] == self.boardMap[2][2]) and self.boardMap[1][1] != " ":
            if self.boardMap[1][1] == self.Player1Symbol:
                return {
                    "finished": True,
                    "message": f"{self.Player1Name} Wins!"
                    }
            else:
                return {
                    "finished": True,
                    "message": "Player 2 (BOT) Wins!"
                }
        if (self.boardMap[0][2] == self.boardMap[1][1] == self.boardMap[2][0]) and self.boardMap[1][1] != " ":
            if self.boardMap[1][1] == self.Player1Symbol:
                return {
                    "finished": True,
                    "message": f"{self.Player1Name} Wins!"
                    }
            else:
                return {
                    "finished": True,
                    "message": "Player 2 (BOT) Wins!"
                }
        return {
            "finished": False,
            "message": ""
        }
    def markInBoard(self, row, column, markSymbol):
        if self.boardMap[row][column] != " ":
            return {
                "isError": True,
                "message": "This Row and column are already marked."
            }
        self.MarksInThisMatch+=1
        self.boardMap[row][column] = markSymbol
        return {
            "isError": False,
            "message": ""
        }      
    def playMachineWay(self):
        self.checkDrawWrapper()
        cleanChat_GLOBAL()
        print("Wait, the machine is thinking..")
        time.sleep(0.7)
        while True:
            markResult = self.markInBoard(random.randint(0, 2), random.randint(0, 2), self.Player2Symbol)
            if markResult["isError"] == False:
                break
    def playerMarkBoard(self, row, column):
        markResult = self.markInBoard(row, column, self.Player1Symbol)
        if markResult["isError"] == False:
            return True
        else:
            print(markResult["message"])
            return False
                
    def cleanBoard(self):
        for row in range(3):
            self.boardMap[row][0] = " "
            self.boardMap[row][1] = " "
            self.boardMap[row][2] = " "
        self.MarksInThisMatch = 0
    def callToAnotherMatch(self):
        wannaContinuePlaying = input("Do You Wanna Continue Playing y/N? ").capitalize()
        if (wannaContinuePlaying == "N"):
            self.continuePlaying = False
            quit()
        else:
            self.cleanBoard()
            self.continuePlaying = True
            self.startGame()
    def checkWinWrapper(self):
        checkWin = self.verifyWin()
        if checkWin["finished"] == True:
            print(checkWin["message"])
            self.callToAnotherMatch() 
    def showBoard(self):
        print("1:","|",self.boardMap[0][0], "|", self.boardMap[0][1], "|", self.boardMap[0][2], "|")
        print("----------------")
        print("2:","|",self.boardMap[1][0], "|", self.boardMap[1][1], "|", self.boardMap[1][2], "|")
        print("----------------")
        print("3:","|",self.boardMap[2][0], "|", self.boardMap[2][1], "|", self.boardMap[2][2], "|")
        print("----------------")
    def askToPlayerSelectRow(self):
        while True:
            selectedRow = input("Select a Row (1 ~ 3): ")
            checkResult = self.verifySelectedColumn(selectedRow)
            if (checkResult == False):
                print("Select a valid Row (1 ~ 3)")
            else:
                return int(selectedRow) - 1
    def askToPlayerSelectColumn(self):
        while True:
            self.checkDrawWrapper()
            selectedColumn = input("Select a Column (1 ~ 3): ")
            if self.verifySelectedColumn(selectedColumn) == False:
                print("Select a valid Column (1 ~ 3)")
            else:
                return int(selectedColumn) - 1
    def checkIfThereWasATie(self):
        if (self.MarksInThisMatch >= 9):
            return True
        return False
    def checkDrawWrapper(self):
        if self.checkIfThereWasATie():
            print("There was a draw")
            self.callToAnotherMatch()
    def startGame(self):
        if self.continuePlaying == False:
            return
        self.checkDrawWrapper()
        self.playMachineWay()
        self.showBoard()
        self.checkWinWrapper()
        while True:
            markCheckResult = self.playerMarkBoard(self.askToPlayerSelectRow(), self.askToPlayerSelectColumn())
            if (markCheckResult == True):
                break
        cleanChat_GLOBAL()
        self.checkWinWrapper()
        self.checkDrawWrapper()
        self.startGame()
            
class system_C:
    PlayTable_O = PlayTable_C()
    @staticmethod
    def cleanChat():
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    def startNewGame(self):
        self.PlayTable_O.confirmStartGame()
        self.cleanChat()
        self.PlayTable_O.selectGameDificulty()
        self.PlayTable_O.startGame()

System_O = system_C()
System_O.startNewGame()
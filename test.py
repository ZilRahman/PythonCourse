

def start():

    yarnSelect, ballSelect = livingRoomInput()
    print(yarnSelect, ballSelect)

    atticSelect(yarnSelect, ballSelect)


def atticSelect(yarnSelect, ballSelect):
    if(yarnSelect  == "y"):
        print("Selected yarrrrn")
    else:
        print("Not selected yarn")

    if(ballSelect == "y"):
        print("Selected ballsenect")
    else:
        print("Not selected ball")




def livingRoomInput():
    yarnSelect = input("Select yarn? y/n")
    ballSelect = input("select ball? y/n")
    return(yarnSelect, ballSelect)

start()
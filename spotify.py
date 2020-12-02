import json, sys

playlist = []
UserList = []

def addSong(artist, album, song):
    newSong = {"artist": artist, "album": album, "song": song}
    playlist.append(newSong)

def numberOfSongs():
    number = len(playlist)
    return number

def showPlaylist():
    for s in playlist:
        print(s["song"], "by", s["artist"],"found on",s["album"],"Added by:",s["added by"])

def playSong(songtitle):
    for s in playlist:
        if(songtitle == s["song"]):
            print("Currently playing", s["song"],"by",s["artist"])

def openPlaylist():
    with open("songs.json") as json_file:
        data = json.load(json_file)
        return data

def savePlaylist():
    with open("songs.json", "w") as outfile:
        json.dump(playlist, outfile)
        
# user add a song
def addSong(artist, album, song, username):
    newSong = {"artist" : artist, "album" : album, "song" : song, "added by" : username}
    playlist.append(newSong)
              
# get user list
def openUserList():
    with open("user.json") as json_file:
        data = json.load(json_file)
        return data
      
# save users
def saveUser():
    with open("user.json", "w") as outfile:
        json.dump(UserList, outfile)
  
# check user privilage
def getUserRole(username):
    user_Role = ""
    for user in UserList:
        if username == user["username"]:
            user_Role = user["role"]
    
    return user_Role
            
# owner users can add other members
def addUser(newUser,newPassword):
    newUser = {"username" : newUser, "password": newPassword, "role": "family member"}
    UserList.append(newUser)
    print("New User",newUser["username"],"added successfully")

    
# show user list
def showUserList():
    for name in UserList:
        print(name["username"])

# user logging in
def userlogin(username, password):
    
    logged_In = False
    for user in UserList:
        if user["username"] == username and user["password"] == password:
            logged_In = True
            break
        else:
            logged_In = False
    
    return logged_In
            
def unsuccessful_Login():
        print("unsuccessful entry")
        print("Terminating program")
        sys.exit()

def user_Input_Main():
    print("\n")
    print("Choose on of the following options:")
    print("1- Play songs from your playlist")
    print("2- Add a song to your play list")
    print("3- View your play list")
    print("4- Family sharing options")
    print("5- Quit")
    
    userIn = input("What is your choice of options? ")
    return userIn

def user_Quit(username):
    print("Thank you for using our HU Spotify Python App :)")
    print("Have a nice day", username)
    sys.exit()


##################
#MAIN
##################


logged_In = False
userIn = ""

print("Welcome to HU Spotify")
print("Login with your username and password")

UserList = openUserList()
userSongChoice = ""
UserFamilyInput = ""

# log in process
for log_counter in range(1,4):
    usrnme = input("username:")
    pswrd = input("password:")
    
    logged_In = userlogin(usrnme,pswrd)
    if logged_In == False:
        print("unsuccessfuly entry, this is your try",log_counter, "out of 3")
    else:
        print("welcome back",usrnme)
        break
# Force quit after 3 attempt
if log_counter == 3:
    unsuccessful_Login()        

# load play lists after successful login
playlist = openPlaylist()
print("Loading", usrnme, "Playlists...")

# Main menu 

while logged_In == True:
    
    userIn = user_Input_Main()
    if userIn == "1":
        print("\n")
        print("Pick a song:")
        showPlaylist()
        userSongChoice = input("what is your choice?")
        playSong(userSongChoice)
        continue
    
    elif userIn == "2":
        print("Add a song to your playlist")
        print("\n")
        artst = input("Pick the artist: ")
        albm = input("Pick an album Discography:") 
        sng = input("Now pick a song from the album:")
        addSong(artst,albm,sng,usrnme)
        print("your song", usrnme, "has been added successfully to the playlist")
        savePlaylist()
    
        
        
    elif userIn == "3":
        showPlaylist()
    
    elif userIn == "4":
        userRole = getUserRole(usrnme)
        if userRole != "owner":
            print("sorry, you are not authorized to do modifications")
            continue
        else:
            print("please make one of the following choices:")
            print("1- View users list")
            print("2- Add a user")
            UserFamilyInput = input("what is your choice:")
            if UserFamilyInput == "1":
                showUserList()
            elif UserFamilyInput == "2":
                newUserID = input("new user ID:")
                newPswd = input("new user password:")
                addUser(newUserID, newPswd)
                saveUser()
    
    if userIn == "5":
        user_Quit(usrnme)











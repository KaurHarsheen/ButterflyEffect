def main():
    import mysql.connector
    mydb= mysql.connector.connect(host='localhost', user='root', password='1234')
    mycursor= mydb.cursor()
    mycursor.execute("Show Databases")
    myrec2 = mycursor.fetchall()
    L1 = []
    for rec2 in myrec2:
        L1.append(rec2[0])
    key1 = "project"
    if key1 in L1:
        pass
    else:
        mycursor.execute("Create Database project")
    mycursor.execute("Use project")
    
    mycursor.execute("Show Tables")
    myrec1 = mycursor.fetchall()
    L = []
    for rec in myrec1:
        L.append(rec[0])
    key = "game"
    if key in L:
        pass
    else:
        mycursor.execute("Create table game( PID integer Primary key auto_increment,Name varchar(25),Games_played integer default 0,Games_won integer default 0,Rounds_played integer default 0,Rounds_won integer default 0)")

    import time
    def slow(word):
        z = 0
        while z<len(word):
            print(word[z],end ="")
            time.sleep(0.0260104111907)
            z = z+1
    def start():
        print()
        w = "\nHere is your performance in the game till now"
        slow(w)
        print()
        print("Games played: ",gamesplayed1)
        print("Games won: ",gameswon1)
        print("Rounds played: ",Roundsplayed1)
        print("Round won: ",Roundswon1)
        print()
        x = "\nDo you want to play again?"
        slow(x)
        print()
        
        X = "1)Yes.\n"+"2)No."
        slow(X)
        print()
        
        Ans = int(input("\nMake your choice\n"+"1 or 2: "))
        if Ans ==1:
            main()
        else:
            print("Game Over")
            
    def fetch(plid):
        mycursor.execute("select *from game where pid=%s",(plid,))
        myrec = mycursor.fetchall()
        global gamesplayed1,gameswon1,Roundsplayed1,Roundswon1
        gamesplayed1 = myrec[0][2]+1
        gameswon1 = myrec[0][3] + gameswon
        Roundsplayed1 = myrec[0][4] + Roundsplayed
        Roundswon1 = myrec[0][5] + Roundswon
        mycursor.execute("Update game set games_played=%s,games_won=%s,rounds_played=%s,rounds_won=%s where pid=%s",(gamesplayed1,gameswon1,Roundsplayed1,Roundswon1,c4))
        mydb.commit()
        
    print()
    print()
    c1 = "Have you played before? Choose Y or N\n"
    slow(c1)
    c2 = input("Enter choice: ")
    if c2 in "nN":
        c3 = input("Enter name: ")
        mycursor.execute("Insert into game(name) values(%s)",(c3,))
        mydb.commit()
        mycursor.execute("select max(PID) from game")
        myrecords = mycursor.fetchall()
        c4 = myrecords[0][0]
        print("Your player id is",c4)
    elif c2 in 'yY':
        c4 = int(input("Enter your player id: "))
        
    Y ="Thank you for playing with us.\n"+"Kindly choose from option 1 or 2 in the given game by typing 1 for 1st option and 2 for the latter one.\n"+"So lets begin"
    slow(Y)
    print()
    print()

    time.sleep(2)
    
    #Agreement
    a = "AGREEMENT\n"+"A mysterious van pulls in front of you.\n"+"You're given the chance to play deadly games for a fortune.\n"+"Do you play? \n"
    slow(a)
    print()
    a = "1)Yes.\n"+"2)No."
    slow(a)
    print()
    print()

    b = int(input("Make your choice\n"+"1 or 2: "))
    print()
    Roundsplayed = 0
    Roundswon = 0
    gameswon = 0
    
    #Round 1
    if b ==2:
        c = "You decide not to play the game.\n"+"Your creditors find you and kill you.\n"+" \n"+"YOU HAVE BEEN ELIMINATED"
        slow(c)
        Roundsplayed = Roundsplayed + 1
        fetch(c4)
        start()
        
        
    elif b ==1:
        c = "Congratulations! You made it to the first round.\n"+"From now on you need to pass through 6 rounds by making choices that will decide your fate.\n"+"\n"+"Round 1.\n"+"Players have started teaming up.\n"+"Going solo can be dangerous but you do not trust any of the other players.\n"+"What do you do? \n"
        slow(c)
        Roundsplayed = Roundsplayed + 1
        Roundswon = Roundswon + 1
        print()

        c = "1)Go solo.\n"+"2)Form an alliance. \n"
        slow(c)
        print()

        d = int(input("Make your choice\n"+"1 or 2: "))
        print()

        #Round 2
        if d ==1:
            e = "You can’t trust anyone but yourself- you go solo.\n"+"With no one to help you, you lose the next game.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
            slow(e)
            Roundsplayed = Roundsplayed + 1
            fetch(c4)
            start()
            
            
        elif d ==2:
            e = "Let me announce the results of the first game.\n"+"You choose wisely.\n"+"Your allies were useful.\n"+"\n"+"You SURVIVED\n"+"\n"+"Now for the second round.\n"+"You had one game of strength and one of wit.\n"+"For the next game, do you choose your partner based on strength or wit? \n"
            slow(e)
            Roundsplayed = Roundsplayed + 1
            Roundswon = Roundswon + 1
            print()
            
            e = "1)Strength. \n"+"2)Wit. \n"
            slow(e)
            print()
            
            f = int(input("Make your choice\n"+"1 or 2: "))
            print()

            #Round 3
            if f ==1:
                g ="It was a math problem.\n"+"You die.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
                slow(g)
                Roundsplayed = Roundsplayed + 1
                fetch(c4)
                start()

            elif f ==2:
                g = "Your partner's quick thinking saved you\n"+"\n"+"You SURVIVED\n"+"\n"+"As the 3rd round begins, a fight is brewing amongst the players. This is your chance to eliminate competition before the next round.\n"+"You can join the fight to knock out your competitors, or play defense. What do you do? \n"
                slow(g)
                Roundsplayed = Roundsplayed + 1
                Roundswon = Roundswon + 1
                print()

                g = "1)Attack others. \n"+"2)Defend yourself. \n"
                slow(g)
                print()

                h = int(input("Make your choice\n"+"1 or 2: "))
                print()
                
                #Round 4
                if h ==1:
                    i ="You decide to risk it all and fight the other players.\n"+"It’s hard to see in the dark, and someone hits you on the head while your back is turned.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
                    slow(i)
                    Roundsplayed = Roundsplayed + 1
                    fetch(c4)
                    start()
                    
                elif h ==2:
                    i = "You stayed out of the fight and went unnoticed.\n"+"\n"+"\n"+"You SURVIVED"+"\n"+"\n"+"For the 4th round,a guard slips you some inside information but if you tell anyone you'll be killed.\n" +"Your close ally will probably die if you don't share the tip.\n"+"What do you do? \n"
                    slow(i)
                    Roundsplayed = Roundsplayed + 1
                    Roundswon = Roundswon + 1
                    print()

                    i = "1)Keep it a secret. \n"+"2)Tell your ally. \n"
                    slow(i)
                    print()

                    j = int(input("Make your choice\n"+"1 or 2: "))
                    print()

                    #Round 5
                    if j ==2:
                        k = "Your ally survives, but the guard kills you for sharing the secret.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
                        slow(k)
                        Roundsplayed = Roundsplayed + 1
                        fetch(c4)
                        start()

                    elif j ==1:
                        k = "The guard killed those who snitched, but you were spared.\n"+"\n"+"\n"+"You SURVIVED"+"\n"+"\n"+"Before the 5th round,the strongest player chooses you to be their next partner.\n"+"But you will need to betray your ally and leave them behind.\n"+"What do you do? \n"
                        slow(k)
                        Roundsplayed = Roundsplayed + 1
                        Roundswon = Roundswon + 1
                        print()
                        
                        k = "1)Stick to your ally. \n"+"2)Betray your ally. \n"
                        slow(k)
                        print()

                        l = int(input("Make your choice\n"+"1 or 2: "))
                        print()

                        #Round 6
                        if l ==1:
                            m = "You stick with your ally.\n"+"Unfortunately, it’s a game of strength and the strongest player kills you both.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
                            slow(m)
                            Roundsplayed = Roundsplayed + 1
                            fetch(c4)
                            start()
                            
                        elif l ==2:
                            m = "The strategy was useful. You made it out alive.\n"+"\n"+"\n"+"You SURVIVED\n"+"\n"+"\n"+"As you hold onto your nerver and fifth round approaches, a player is seriously injured.\n"+"Do you try to help treat them or do you let them die? \n"
                            slow(m)
                            Roundsplayed = Roundsplayed + 1
                            Roundswon = Roundswon + 1
                            print()

                            m ="1)Let them die. \n"+"2)Help treat them. \n"
                            slow(m)
                            print()

                            n = int(input("Make your choice\n"+"1 or 2: "))
                            print()

                            #Round 7
                            if n==2:
                                o = "You manage to save them, but they end up betraying you and killing you in the final game.\n"+"\n"+"\n"+"YOU HAVE BEEN ELIMINATED"
                                slow(o)
                                Roundsplayed = Roundsplayed + 1
                                fetch(c4)
                                start()

                            elif n==1:
                                o = "We sincerely congratulate and commend you for successfully making it through the game.\n"+"\n"+"\n"+"YOU WIN!"
                                slow(o)
                                time.sleep(2)
                                print()
                                p = "But......at what cost?"
                                slow(p)
                                time.sleep(2)
                                
                                Roundsplayed = Roundsplayed + 1
                                Roundswon = Roundswon + 1
                                gameswon = 1
                                fetch(c4)
                                start()

main()

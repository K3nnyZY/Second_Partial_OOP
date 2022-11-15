from Movie_Tickets import Cine,Movie

royalfilms = Cine(seat_vip=5,seat_regular=3)
royalfilms.add_films([Movie("Black Panther", "9:15 PM"), Movie("Black Adam", "6:20 pm"), 
                    Movie("Spiderman","5:00 PM"), Movie("One Piece","2:00 PM")])
print("")
royalfilms.add_user(id="03", preference="vip")
royalfilms.sell(id="03",movie="Black Panther",time="9:15 PM",vip=2,regular=1)
print("")
print("otra compra el usuario 03")
royalfilms.sell(id="03",movie="Black Adam",time="6:20 PM",vip=2,regular=8)
print("")
royalfilms.sell(id="06",movie="Black Adam",time="9:15 PM",vip=2,regular=1)

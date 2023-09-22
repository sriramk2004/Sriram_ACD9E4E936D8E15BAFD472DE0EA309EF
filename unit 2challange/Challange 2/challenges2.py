'''implement a class called player that represents cricket player.
the player class should have a mathod called play() which prints "the player is playing cricket.derive two classea,batsman
and bowler,from the player class. override the play() mathod in each derived class to print " the batsman is batting"and "the bowler is bowling",respectively.write a program to crate objects of both the batsman and bowler classes and call the play() mathod for each object.'''

#define the base class player
class Player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class batsman
class Batsman(Player):
  def play(self):
    print("the batsman is batting.")

#define the derived class bowler
class Bowler(Player):
  def play(self):
     print("the bowler is bowling.")


#crate objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() mathod for each object
batsman.play()
bowler.play()

"""
ttt_logic
  This module contains the logic to drive a two-player Tic-Tac-Toe
  game.
"""

#---------------------------------------------------------------
#  Define any global variables this module may need to maintain the
#  state of a Tic-Tac-Toe game.
#---------------------------------------------------------------

cp3 = 'X'

NW,N,NE,W,C,E,SW,S,SE = None,None,None,None,None,None,None,None,None


def check_status():
    """
    Checks to see if either player has won or if the board is filled.  
    Returns a two-tuple in which the first component is the string
    "X" or the string "O" or the value None; the second component
    of the tuple is one of the following strings that indicates the
    Tic-Tac-Toe board's status:
      "Playing"     No one has won and a move is available
      "Win_NW_NE"   Win across top row
      "Win_W_E"     Win across middle row
      "Win_SW_SE"   Win across bottom row
      "Win_NW_SW"   Win along left colunm
      "Win_N_S"     Win along center column
      "Win_NE_SE"   Win along right column
      "Win_NW_SE"   Win from left-top corner to right-bottom 
      "Win_NE_SW"   Win from right-top corner to left-bottom 
      "Draw"        All squares filled with no winner
    The first component of the resulting tuple represents the game
    winner, and the second component of the tuple represents the
    winning configuration.  If the status component is "Playing" or
    "Draw", the winner component should be None; for example, the
    tuple ("X", "Win_NE_SE") would be a valid return value, but
    neither ("X", "Draw") nor ("O", "Playing") represents a valid
    result. 
    """

    global NW,N,NE,W,C,E,SW,S,SE   
    
    if NW == N == NE != None:
        return N, "Win_NW_NE"
    elif W == C == E != None:
        return W, "Win_W_E"
    elif SW == S == SE != None:
        return S, "Win_SW_SE"
    elif NW == W == SW != None:
        return W, "Win_NW_SW"
    elif N == C == S != None:
        return C, "Win_N_S"
    elif NE == E == SE != None:
        return E, "Win_NE_SE"
    elif NE == C == SW != None:
        return C, "Win_NE_SW"
    elif NW == C == SE != None:
        return C, "Win_NW_SE"
    elif NW != None and N != None and NE != None and W != None and C != None and E != None and SE != None and SW != None and S != None:
        return None, "Draw"
    else:
        return None,"Playing"

def move(location):
    """
    Places the current player's mark at the given location, if possible.
    The caller must pass one of the following strings specifying
    the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    Returns True if the specified location is available (that is,
    the global variable keeping track of that position is None);
    otherwise the function returns False for an illegal move.
    If the current player makes a valid move, the function ensures
    that control passes to the other player; otherwise, the move
    function does not affect the current player.
    """
    global NW,N,NE,W,C,E,SW,S,SE,cp3
    player,status = check_status()
    if status != 'Playing':
        return False
    else:
        if location == 'NorthWest': 
            if NW == None:
                NW = cp3
                change_player()
                return True
            else:
                return False
        elif location == 'North':
            if N == None:
                N = cp3
                change_player()
                return True
            else:
                return False
        elif location == 'NorthEast':
            if NE == None:
                NE = cp3
                change_player()
                return True
            else:
                return False    
        elif location == 'West':
            if W == None:
                W = cp3
                change_player()
                return True
            else:
                return False 
        elif location == 'Center':
            if C == None:
                C = cp3
                change_player()
                return True
            else:
                return False
        elif location == 'East':
            if E == None:
                E = cp3
                change_player()
                return True
            else:
                return False        
        elif location == 'SouthWest': 
            if SW == None:
                SW = cp3
                change_player()
                return True
            else:   
                return False
        elif location == 'South': 
            if S == None:
                S = cp3
                change_player()
                return True
            else:
                return False
        elif location == 'SouthEast': 
            if SE == None:
                SE = cp3
                change_player()
                return True
            else: 
                return False
    
        
        
    #return result   # Replace with your implementation


def current_player():
    """
    Returns the player whose turn it is to move.  This allows the
    presentation to report whose turn it is.
    Return value is one of either "X" or "O".
    """
    global cp3
    return cp3


def set_player(new_player):
    
    """
    Sets the current player.  Useful for games that require the
    player to answer a question correctly before a move.  If the
    player answers incorrectly, the turn moves to the opponent.
    Valid values for new_player are "X" or "O"; any other strings
    will not change the current player.
    """
    global cp3
    if new_player == "X" or new_player == "O":
        cp3 = new_player



def change_player():
    
    """
    Alternates turns between players.  X becomes O, and O becomes X.
    """
    global cp3
    if cp3 == "X":
        cp3 = "O"
    elif cp3 == "O":
        cp3 = "X"
        
def look(location):
    """
    Returns the mark at the given location.  The caller must pass 
    one of the following strings specifying the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    The function's valid return values are None, "X", or "O".
    Returns None if neither player has marked 
    the given location.  The function also returns None if the
    caller passes any string other than one of the location strings
    listed above.
    This function allows the presentation to draw the contents
    of the Tic-Tac-Toe board.
    """
    global NW,N,NE,W,C,E,SW,S,SE 
    if location == 'NorthWest':
        return NW
    elif location == 'North':
        return N
    elif location == 'NorthEast':
        return NE
    elif location == 'West':
        return W
    elif location == 'East':
        return E
    elif location == 'SouthWest':
        return SW
    elif location == 'South':
        return S
    elif location == 'SouthEast':
        return SE
    elif location == 'Center':
        return C 


def initialize_board():
    """
    Make all the board locations empty and set current player to
    "X" (that is, reset the board to the start of a new game)
    """
     
    global NW,N,NE,W,C,E,SW,S,SE,cp3
    
    cp3 = 'X'
    
    NW,N,NE,W,C,E,SW,S,SE = None, None,None,None,None,None,None,None,None

if __name__ == "__main__":
    pass   #  This module is not meant to be run as a standalone program

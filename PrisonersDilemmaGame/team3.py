####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


team_name = 'Laura and Dave' # Only 10 chars displayed.

strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

    opp_b = 0
    opp_c = 0
   
    

    # Strategy: First round, collude. Subsequesnt rounds, mimic the move they made in their last move.
    
    if len(their_history)<1: #It's the first round: collude
        return 'c'
   
    else:
        for choice in their_history:
            if choice == 'c':    # their previous choice was collude
                opp_c +=1
                return 'c'
            
            else:               # their previous choice was betray
                opp_b +=1
                return 'b'
               
                 
    

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False



if __name__ == '__main__':
# Test 1
    if test_move(my_history='',
                 their_history='',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print 'Test 1 passed'
    else:
        print 'Test 1 Failed'

#Test 2 
    if test_move(my_history='c',
                 their_history='c',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print 'Test 2  passed'
    else:
        print 'Test 2 Failed'

#Test 3
    if test_move(my_history='c',
                 their_history='b',
                 my_score=0,
                 their_score=0,
                 result='b'):
        print 'Test 3 passed'
    else:
        print 'Test 3 Failed'
   

import chess
import random
print("Luck V2 by PiKitty")
print("WORK IN PROGRESS")
board = chess.Board()


def minimax(depth,isMaxing,alpha,beta):
    if depth == 0 or board.is_game_over():
        return evaluate_static_position()
    if isMaxing == True:
        to_move=''
        i=0
        lis=list(board.legal_moves)
        maxEval=-9999999999999
        while i != len(lis):
            board.push(lis[i])
            evalu=minimax(depth-1,False,alpha,beta)
            if evalu > maxEval:
                maxEval=evalu
                to_move=lis[i]
            board.pop()
            alpha=max(alpha,evalu)
            if beta <= alpha:
                break
            i+=1
            print("bestmove "+str(to_move))
        return maxEval
    else:
        to_move=''
        i=0
        minEval=9999999999999999
        lis=list(board.legal_moves)
        while i != len(lis):            
            board.push(lis[i])
            evalu=minimax(depth-1,True,alpha,beta)
            if evalu < minEval:
                minEval=evalu
                to_move = lis[i]
            board.pop()
            beta=min(beta,evalu)
            if beta <= alpha:
                break
            i+=1
            print("bestmove "+str(to_move))
        return minEval
def evaluate_static_position():
    val=0
    for i in range (0,8):
        for j in range(0,8):
            if i == 0:
                s='A'
            if i == 1:
                s='B'
            if i == 2:
                s='C'
            if i == 3:
                s='D'
            if i == 4:
                s='E'
            if i == 5:
                s='F'
            if i == 6:
                s='G'
            if i == 7:
                s='H'
            if j == 0:
                e='1'
            if j == 1:
                e='2'
            if j == 2:
                e='3'
            if j == 3:
                e='4'
            if j == 4:
                e='5'
            if j == 5:
                e='6'
            if j == 6:
                e='7'
            if j == 7:
                e='8'
            piece=board.piece_at(getattr(chess,s+e))
            if str(piece) != 'None':
                if str(piece.piece_type) == '1':
                    if piece.color == True:
                        val+=1
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val+=1
                    else:
                        val-=1
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val-=1
                if str(piece.piece_type) == '2':
                    if piece.color == True:
                        val+=3
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val+=0.25
                    else:
                        val-=3
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val-=0.25
                if str(piece.piece_type) == '3':
                    if piece.color == True:
                        val+=3.25
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val+=0.25
                    else:
                        val-=3.25
                        if s+e == 'E4' or 'E5' or 'D4' or 'D5':
                            val-=0.25
                if str(piece.piece_type) == '4':
                    if piece.color == True:
                        val+=5
                    else:
                        val-=5
                if str(piece.piece_type) == '5':
                    if piece.color == True:
                        val+=9
                    else:
                        val-=9
    if board.is_checkmate() == True:
        if board.turn == True:
            val-=999999999
            return val
        else:
            val+=9999999999
            return val
    if board.is_fivefold_repetition() == True:
        if board.turn == True:
            if val < 0:
                val+=999
                return val
            else:
                val-=999
                return val
        
    return val
def make_move():
    player=input()
    if player == 'go': 
        if board.is_game_over():
            print("The Game Is Over")
        else: 
            if board.turn == True:
                minimax(5,True,-9999999999999999999999999999999999,9999999999999999999999999999999999999999999999)
            elif board.turn == False:
                minimax(5,False,-9999999999999999999999999999999999,9999999999999999999999999999999999999999999999)
    elif chess.Move.from_uci(player) in board.legal_moves:
        pmove = chess.Move.from_uci(player)
        board.push(pmove)
    else:
        print("Sorry wrong command :(")
while True:
    make_move()
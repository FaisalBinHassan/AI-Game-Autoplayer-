# Faisal AutoPlayer - CODE1/3 (VERSION1) = Should get around [ 14.2k to 15.4k ]
from board import Direction, Rotation, Action
from random import Random
import random
import time
from operator import itemgetter

last_score = 0
count = 0
Status = False
block_prev = 0


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class FaisalssPlayer(Player):

    # Height of each COLUMN
    def Collumn_heights(self, board):
        Collumn_heights_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(board.width):
            for y in range(board.height, 0, -1):
                if (x, y) in board.cells:
                    Collumn_heights_list[x] = board.height - y

        return Collumn_heights_list

    # ALL Height's of ALL COLUMN
    def Total_heights(self, board):
        col = self.Collumn_heights(board)
        avg_h = sum(col) / len(col)
        return avg_h


    # Variation of its column heights
    def Bumpiness(self, board):
        Bumpiness = 0
        Collumn_heights_list = self.Collumn_heights(board)
        for x in range(board.width - 1):
            if Collumn_heights_list[x] > Collumn_heights_list[x + 1]:
                Bumpiness += Collumn_heights_list[x] - Collumn_heights_list[x + 1]
            else:
                Bumpiness += Collumn_heights_list[x + 1] - Collumn_heights_list[x]
        return Bumpiness

    # SPACES between last and next block
    def Block_Space(self, board):
        Block_Space = 0
        for x, y in board.cells:
            carry_on = True
            count = 1
            while carry_on == True:
                if ((x, y + count) not in board.cells) and (count + y != 24):
                    Block_Space += 1
                    count += 1
                else:
                    carry_on = False

            #if ( Block_Space == 7 ):
                #Status = True

        return Block_Space

    # GAPS
    def GAPS(self, clonedBoard):
        board = sorted(clonedBoard.cells, key=itemgetter(1))
        start = board[0][1]
        end = board[len(board)-1][1]
        gaps = 0
        for row in range(start+1, end+1):
            currentRow = []
            for i in board:
                if i[1]==row:
                    currentRow.append(i)
                #else:
                #    break
            currentRow = sorted(currentRow)
            if len(currentRow)>1:
                potentialGaps = []
                for j in range(10):
                    x = j, row
                    if x not in currentRow:
                        potentialGaps.append(j)
                if len(potentialGaps)>0:
                    for num in potentialGaps:
                        test = num, row-1
                        if test in board:
                            gaps +=1
        return gaps

    def cleared_lines(self, sandbox):
        newScore = sandbox.score
        diff = newScore - last_score

        if 100 < diff < 130:
            return 1
        elif 400 < diff < 450:
            return 2
        elif 800 < diff < 850:
            return 3
        elif 1600 < diff < 1650:
            return 4
        else:
            return 0



    # Score of current block in current rotation and position
    def calc_score(self, board):
        gaps = self.GAPS(board)
        change_in_score = board.score - last_score
        Block_Space = self.Block_Space(board)
        Bumpiness = self.Bumpiness(board)
        total_height = self.Total_heights(board)
        complete_lines = self.cleared_lines(board)
        #score = (change_in_score * 0.1) + (Block_Space * -0.52) + (Bumpiness * -0.15) + (total_height * -0.8)
        #score = (change_in_score * 0.2) + (Block_Space * -0.531) + (Bumpiness * -0.37) + (total_height * -0.8)
        #score = (change_in_score * 0.44) + (Block_Space * -0.51) + (Bumpiness * -0.27) + (total_height * -0.81)
        #score = (change_in_score * 0.121) + (Block_Space * -0.51) + (Bumpiness * -0.27) + (total_height * -0.8)        #
        #score = (change_in_score * 0.1) + (Block_Space * -0.51) + (Bumpiness * -0.27) + (total_height * -0.8)
        # Got me 19,988 k --> score = (gaps * -4.6) + (Block_Space * -3.4) + (Bumpiness * -1.1) + (total_height * -4.1)
        #score = (gaps * -4.8) + (Block_Space * -3.4) + (Bumpiness * -1.1) + (total_height * -4.1)
        #score = (change_in_score * 0.1) + (Block_Space * -0.51) + (Bumpiness * -0.27) + (total_height * -0.8)
        score = (Bumpiness * -1.1) + (gaps * -4.2) + (Block_Space * -3.6) + (total_height * -1.1)
        #score = (complete_lines*0.760666) + (total_height*-0.510066) + (gaps * -0.35663)+ (Bumpiness*-0.184483)
        return score


#11,620 ->         score = (gaps * -4.6) + (Block_Space * -3.4) + (Bumpiness * -3.7) + (total_height * -4.1)
#10,670 ->         score = (gaps * -4.6) + (Block_Space * -3.4) + (Bumpiness * -1.1) + (total_height * -4.1)
#11,820 ->         score = (gaps * -4.6) + (Block_Space * -3.4) + (Bumpiness * -2.7) + (total_height * -4.1)
#12,840 ->         score = (gaps * -4.6) + (Block_Space * -3.9) + (Bumpiness * -2.7) + (total_height * -4.1)



    # ALG2 : Score of current block in current rotation and position
    def score_board(self, board):
        gaps = self.gapFinder(board)
        #complete_lines = self.complete_lines(board)
        rifBumpinessts = self.Bumpiness(board)
        Block_Space = self.Block_Space(board)
        total_height = self.Total_heights(board)
        change_in_score = board.score - last_sscore
        self.calc_collumn_heights(board)
        col_height = sum(collumn_heights)
        bumpiness = self.bumpiness(board)
        #total = (-0.51066*col_height) + (Bumpiness * -0.25) + (-0.35663*gaps) + (-0.184483*bumpiness) + (change_in_score*0.1)+ (Block_Space * -0.55) + (total_height * -0.7)
        #total = (gaps * -0.35663) + (total_height * -0.51066) + (bumpiness*-0.184483)
        return total


    # SHAPE the board to current position and rotation
    def move_to_target(self, board, sandbox, target_pos, taregt_rotations):
        for i in range(0, taregt_rotations):
            try:
                sandbox.rotate(Rotation.Clockwise)
            except:
                pass
        Shape_pos = board.falling.left
        while target_pos != Shape_pos:
            if target_pos < Shape_pos:
                Shape_pos -= 1
                try:
                    sandbox.move(Direction.Left)
                except:
                    pass
            elif target_pos > Shape_pos:
                Shape_pos += 1
                try:
                    sandbox.move(Direction.Right)
                except:
                    pass
        try:
            sandbox.move(Direction.Drop)
        except:
            pass



    # Save all MOVES!
    def make_best_move(self, board, best_target_pos, best_num_of_rotations):

        moves = []

        # Specific rotation
        for i in range(best_num_of_rotations):
            moves.append(Rotation.Clockwise)

        Shape_move = board.falling.left
        while best_target_pos != Shape_move:

            if best_target_pos < Shape_move:
                Shape_move -= 1
                moves.append(Direction.Left)

            elif best_target_pos > Shape_move:
                Shape_move += 1
                moves.append(Direction.Right)

        moves.append(Direction.Drop)

        return moves


    def choose_action(self, board):

        # Initiate best score, and always refresh last score
        last_score = board.score
        best_score = -1000000000
        # for all possible positions
        for target_pos in range(board.width):

            # for all number of rotations
            for target_num_of_rotations in range(4):
                sandbox = board.clone()

                # Move board to the specific position and rotation
                self.move_to_target(board, sandbox, target_pos, target_num_of_rotations)

                #self.choose_next_action(board, sandbox)
                '''
                
                # Drop BOMB! (if & only if)
                block = self.Block_Space(board)
                global count
                global block_prev
                if ( block == 4 ):
                    if ( count % 10 == 0 and Status ):
                        return Action.Bomb
                    #count += 1

                if ( count % 100 == 0  ):
                    if ( block_prev > block ):
                        if ( drop ):
                            return Action.Discard
                        else:
                count += 1

                 '''

                # Calculate score if this rotation in this specific posistion
                scoring = self.calc_score(sandbox)

                # Calculate score, adjust if it's bigger!
                if scoring > best_score:
                    best_score = scoring
                    best_target_pos = target_pos
                    best_num_of_rotations = target_num_of_rotations


        # Save all moves! ( of the best score rotation&position )
        return self.make_best_move(board, best_target_pos, best_num_of_rotations)


SelectedPlayer = FaisalssPlayer
''''
                block = self.Block_Space(board)
                global count
                if ( block == 4 ):
                    if ( count % 10 == 0 ):
                        return Action.Bomb
                    count += 1
'''''

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        # Creating and initializing a dictionary which stores the loss count of all players
        loss_count = {}
        for match in matches:
            for players in match:
                if players not in loss_count:
                    loss_count[players] = 0

        # Counting the losses 
        for match in matches:
            loss_count[match[1]] += 1

        # Creating lists for answers
        zero_loss = []
        single_loss = []
        
        for player in loss_count:
            if loss_count[player] == 0:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                single_loss.append(player)

        zero_loss.sort()
        single_loss.sort()
        answer = []
        answer.extend([zero_loss, single_loss])
        return answer
        
                
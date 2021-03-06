	#https://www.reddit.com/r/dailyprogrammer/comments/6ilyfi/20170621_challenge_320_intermediate_war_card_game/

class War():
		def __init__(self):
			# player decks
			self.p1 = []
			self.p2 = []

			# Challenge Inputs
			input1a = "5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 33 13 6 1 8 1"
			input1b = "9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5"
			self.input1a = [int(i) for i in input1a.split(' ')]
			self.input1b = [int(i) for i in input1b.split(' ')]

			input2a = "3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1"
			input2b = "9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5"
			self.input2a = [int(i) for i in input2a.split(' ')]
			self.input2b = [int(i) for i in input2b.split(' ')]

			input3 = "1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13"
			self.input3 = [int(i) for i in input3.split(' ')]

		def compare(self, card1, card2):
			#print("Compare: ", card1, ", ", card2)
			if card1 > card2: # player1 wins
				self.p1 = self.p1 + [card1, card2]
				return 1
			elif card2 > card1: #player2 wins
				self.p2 = self.p2 + [card2, card1]
				return 2
			else: # draw
				return(self.war(card1, card2))

		def play(self):
			while self.p1 and self.p2:
				card1 = self.p1.pop(0)
				card2 = self.p2.pop(0)
				self.compare(card1, card2)

			if not self.p1 and self.p2:
				return 2 # p2 wins
			elif not self.p2 and self.p1:
				return 1 # p1 wins
			else:
				return 0 # no one wins

		def war(self, wp1, wp2):
			# determine size of war
			warNum = 3
			if len(self.p1) > 0 and len(self.p2) > 0: # incase player out of cards (i.e. someone lost)
				if len(self.p1) < 4 or len(self.p2) < 4: # incase player has fewer cards than necessary for default
					warNum = min(len(self.p1), len(self.p2)) - 1
			else: # if somebody is out of cards at this stage they lose
				if len(self.p1) != 0:
					return 1
				elif len(self.p2) != 0:
					return 2
				else:
					return 0

			# format card1 and card2 into list, where
			# wp1 and wp2 are the war 'decks'
			if isinstance(wp1, int) and isinstance(wp2, int):
				wp1 = [wp1]
				wp2 = [wp2]

			# draw wager
			for i in range(warNum - 1):
				wp1.insert(0, self.p1.pop(0))
				wp2.insert(0, self.p2.pop(0))

			# determine who wins war
			card1 = self.p1.pop(0)
			card2 = self.p2.pop(0)
			result = self.compare(card1, card2)

			# winner take all
			if result == 1:
				self.p1 += [card1, card2]
				self.p1 += [card for tupl in zip(wp1, wp2) for card in tupl]
				return 1

			elif result == 2:
				self.p2 += [card2, card1]
				self.p2 += [card for tupl in zip(wp2, wp1) for card in tupl]
				return 2

			else: # draw state
				return 0

		def runChallenge(self):
			print("Challenge 1:")
			self.p1 = self.input1a
			self.p2 = self.input1b
			print(self.play())

			self.p1 = self.input2a
			self.p2 = self.input2b
			print(self.play())

			self.p1 = self.input3
			self.p2 = self.input3[:]
			print(self.play())

w = War()
w.runChallenge()

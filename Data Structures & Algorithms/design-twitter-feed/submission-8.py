class Twitter:

    def __init__(self):
        # Use hashmap monitor follows. User: Following. Need to see following to get the news feed
        # Need another data structure to store feeds of users? Individial user have individual tweet feed. max 10
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.order, tweetId))
        while len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]: 
        # Get top 10 recent tweets by following/own post. Most recent tweet IDs
            user_list = self.follows[userId]
            user_list.add(userId)
            max_heap = []
            for user in user_list:
                if self.tweets[user]:
                    last_order, last_tweetid = self.tweets[user][-1]
                    heapq.heappush_max(max_heap, (last_order, user, last_tweetid, len(self.tweets[user]) - 1)) #Store last pointer
            res = []
            while len(res) < 10 and max_heap:
                order, user, tweet, pointer = heapq.heappop_max(max_heap)
                res.append(tweet)
                if pointer > 0:
                    next_last_order, next_last_tweetid = self.tweets[user][pointer - 1] 
                    heapq.heappush_max(max_heap, (next_last_order, user, next_last_tweetid, pointer - 1)) #Store last pointer
            return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

class Twitter:

    def __init__(self):
        # Use hashmap monitor follows. User: Following. Need to see following to get the news feed
        # Need another data structure to store feeds of users? Individial user have individual tweet feed. max 10
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId],(self.order, userId, tweetId))
        while len(self.tweets[userId]) > 10:
            heapq.heappop(self.tweets[userId])
        self.order += 1

    def getNewsFeed(self, userId: int) -> List[int]: 
        # Get top 10 recent tweets by following/own post. Most recent tweet IDs
            feed = []
            for following in self.follows[userId]:
                feed += self.tweets[following]
            feed += self.tweets[userId]
            heapq.heapify_max(feed)
            res = []
            for i in range(10):
                if feed:
                    res.append(heapq.heappop_max(feed))
                else: 
                    break
            res = [tweetId for order, userId, tweetId in res]
            return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

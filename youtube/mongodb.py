from pymongo import MongoClient, DESCENDING
from django.conf import settings

class MongoDBConnection:
    def __init__(self):
        connection_string = f"mongodb://{settings.MONGODB['USER']}:" \
                            f"{settings.MONGODB['PASSWORD']}@" \
                            f"{settings.MONGODB['HOST']}:" \
                            f"{settings.MONGODB['PORT']}/"
        print(connection_string)
        self.client = MongoClient(connection_string, authSource=settings.MONGODB['DB_NAME'])
        self.db = self.client[settings.MONGODB['DB_NAME']]

class ChannelInfo(MongoDBConnection):
    def __init__(self):
        super().__init__()
        self.collection = self.db['channel_info']

    def get_documents(self, filter={}, page=1, limit=20, sort_order=DESCENDING):
        """
        Retrieve documents from the MongoDB collection, with pagination and sorting.

        Parameters:
        - filter: A dictionary specifying the conditions documents must meet to be included in the result.
        - page: The page number of the results to return.
        - limit: The maximum number of documents to return per page.
        - sort_order: The order in which to sort the results by subscriberCount. Use 1 for ascending, -1 for descending.

        Returns:
        - A list of documents from the collection that match the filter, sorted by subscriberCount and paginated.
        """
        # Calculate the number of documents to skip based on the current page number
        skip = (page - 1) * limit
        
        # Perform the query with sorting and pagination
        channels = list(self.collection.find(filter)
                                        .sort("statistics.subscriberCount", sort_order)
                                        .skip(skip)
                                        .limit(limit))
        return channels

class ChannelStats(MongoDBConnection):
    def __init__(self):
        super().__init__()
        self.collection = self.db['channel_stat']

    def get_documents(self, filter={}, limit=5, sort_order=DESCENDING):
        stats = list(self.collection.find(filter, {'_id': 0})
                                    .sort('timestamp', sort_order)
                                    .limit(limit))
        return stats
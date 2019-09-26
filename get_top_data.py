import pandas as pd
import warnings
warnings.filterwarnings('ignore')


class GetTopValues:

    def __init__(self):
        self.clicks_data = pd.read_csv('clicks.csv', names=['timestamp', 'user_id', 'hotel_id', 'hotel_region'])
        self.selection_data = pd.read_csv('selections.csv', names=['timestamp', 'user_id', 'amenity_id'])

    def get_top_hotels(self, user_id, n, cnt_flag):
        if user_id not in self.clicks_data['user_id'].tolist():
            return None
        clicks_data_user = self.clicks_data.loc[self.clicks_data['user_id'] == user_id]
        user_hotel = clicks_data_user.groupby(['hotel_id'])['hotel_id'].count().reset_index(name="count")

        all_count = list(user_hotel['count'].unique())
        sorted_count = sorted(all_count, reverse=True)

        if n>len(sorted_count):
            n = len(sorted_count)

        top_n = user_hotel[user_hotel['count'].isin(sorted_count[0:n])].sort_values(['count'], ascending=[False])
        top_n = top_n[['hotel_id', 'count']]
        if cnt_flag == 2:
            top_n_dict = top_n.to_dict('records1')
        else:
            top_n_dict = top_n.to_dict('records')
        return top_n_dict

    def get_top_amenities(self, user_id, n, cnt_flag=None):
        user_str = self.selection_data['user_id'].astype('str')
        if str(user_id) not in user_str.tolist():
            return None

        clicks_data_user = self.selection_data.loc[self.selection_data['user_id'] == user_id]
        user_amenity = clicks_data_user.groupby(['amenity_id'])['amenity_id'].count().reset_index(name="count")

        all_count = list(user_amenity['count'].unique())
        sorted_count = sorted(all_count, reverse=True)

        if n>len(sorted_count):
            n = len(sorted_count)

        top_k = user_amenity[user_amenity['count'].isin(sorted_count[0:n])].sort_values(['count'], ascending=[False])
        top_k = top_k[['amenity_id', 'count']]
        if cnt_flag == 2:
            top_k_dict = top_k.to_dict('records2')
        else:
            top_k_dict = top_k.to_dict('records')
        return top_k_dict

    def missing_users(self):
        user_hotel = list(self.clicks_data['user_id'].unique())
        user_amenity = list(self.selection_data['user_id'].unique())
        user_no_amenity = list(set(user_hotel) - set(user_amenity))
        user_no_hotel = list(set(user_amenity) - set(user_hotel))
        print(len(user_no_amenity))
        #print(user_no_amenity)
        print(len(user_no_hotel))
        #print(user_no_hotel)


if __name__ == "__main__":
    get_top_data = GetTopValues()
    #2996317656753913712
    #2835680135910998
    #9981336825190994

    #top_k = get_top_data.get_top_amenities(9981336825190994, 10)
    #get_top_data.missing_users()
    #print(top_k)


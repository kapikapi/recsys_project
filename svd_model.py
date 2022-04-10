import numpy as np
import json
import random
import os

class SvdRecommender:
    def __init__(self):
        # init vocab product <-> name
        # user id <-> user pos
        # product id <-> product pos
        # users representations
        # products representations
        with open("static/data/pos_product.json", "r") as read_file:
            self.pos_product = json.load(read_file)

        with open("static/data/user_pos.json", "r") as read_file:
            self.user_pos = json.load(read_file)

        with open("static/data/products_names.json", "r") as read_file:
            self.products_names = json.load(read_file)

        with open("static/data/products_names.json", "r") as read_file:
            self.products_names = json.load(read_file)

        self.products_repres = np.load("recsys_data/products_repres.npy")
        self.users_repres = np.load("recsys_data/users_repres.npy")

    def predict(self, user, n_recs):
        user_pos = self.user_pos[user]
        user_ratings = np.dot(self.users_repres[user_pos, :], self.products_repres)
        sorted_recs = user_ratings.argsort()[::-1][:n_recs]
        rec_product_ids = [str(self.pos_product[str(rec)]) for rec in sorted_recs]
        return [self.products_names[i] for i in rec_product_ids]

    def predict_save_batch(self, n_users, n_recs):
        users_list = list(self.user_pos.keys())
        users_sample = random.sample(users_list, n_users)
        recs = []
        for user in users_sample:
            rec_names = self.predict(user, n_recs)
            rec_str = f"{user}: {', '.join(rec_names)}"
            recs.append(rec_str)
        os.makedirs("res", exist_ok=True)
        with open("res/results.txt", 'w') as f:
            f.write('\n'.join(recs))



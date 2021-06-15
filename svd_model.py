import numpy as np
import json


class SvdRecommender():
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

    self.products_repres = np.load("static/data/products_repres.npy")
    self.users_repres = np.load("static/data/users_repres.npy")

  def predict(self, user, n_recs):
      user_pos = self.user_pos[user]
      user_ratings = np.dot(self.users_repres[user_pos, :], self.products_repres)
      sorted_recs = user_ratings.argsort()[::-1][:n_recs]
      rec_product_ids = [str(self.pos_product[str(rec)]) for rec in sorted_recs]
      return [self.products_names[i] for i in rec_product_ids]

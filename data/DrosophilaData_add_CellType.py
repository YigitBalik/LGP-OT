import pandas as pd
import matplotlib.pyplot as plt

subsample_df = pd.read_csv("../data/drosophila_embryonic/processed/subsample_meta_data.csv", header=0, index_col=0)
all_df = pd.read_csv("../data/drosophila_embryonic/raw/meta_data.csv", header=0, index_col=0)

subsample_df_annot = all_df.loc[subsample_df.index]

subsample_df['manual_annot'] = subsample_df_annot['manual_annot']
subsample_df['germ_layer'] = subsample_df_annot['germ_layer']

subsample_df.to_csv("../data/drosophila_embryonic/processed/subsample_meta_data_with_celltype.csv")

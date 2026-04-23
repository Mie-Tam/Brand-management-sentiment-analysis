import pandas as pd
import os

# 📌 đường dẫn thư mục của bạn
folder_path = r"E:\họcpython\đồ án"

# lấy tất cả file csv
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

df_list = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except:
        df = pd.read_csv(file_path, encoding='latin1')
    
    df_list.append(df)

# gộp file
merged_df = pd.concat(df_list, ignore_index=True)

# xoá trùng
merged_df.drop_duplicates(inplace=True)

# lưu file mới
output_path = os.path.join(folder_path, "merged_comments.csv")
merged_df.to_csv(output_path, index=False)

print("✅ Gộp file thành công:", output_path)
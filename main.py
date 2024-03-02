meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah" 
            }

for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital!): ")
    
    if word in meme_dict.keys():
        print(word + ": " + meme_dict[word])
        
    else:
        print("Maaf, kata yang anda cari tidak ditemukan.")

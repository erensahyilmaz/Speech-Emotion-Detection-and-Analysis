import os
from pydub import AudioSegment

# Ses dosyalarının bulunduğu klasör
dosya_yolu = "belirsiz/ayık"
dosya_cikis = "belirsiz"

# Çıktı klasörünü oluştur
os.makedirs(dosya_cikis, exist_ok=True)


# WebM dosyalarını işle
for dosya_adi in os.listdir(dosya_yolu):
    if dosya_adi.endswith(".wav"):  # Wav dosyalarını seç
        file_path = os.path.join(dosya_yolu, dosya_adi)

        
        ses = AudioSegment.from_file(file_path)

        # 30 saniyelik parçalara böl
        kirpma_uzunlugu = 5 * 1000  # 5 saniye
        parcalar = []

        for i in range(0, len(ses), kirpma_uzunlugu):
            parca = ses[i:i + kirpma_uzunlugu]
            parcalar.append(parca)

        # Parçaları kaydet
        for idx, segment in enumerate(parcalar):
            cikis_yolu = os.path.join(dosya_cikis, f"{dosya_adi[:-5]}_parca_{idx + 1}.wav")
            segment.export(cikis_yolu, format="wav")
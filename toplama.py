import os
import shutil

def vocal_bulma(dosya_yolu, kayit_yeri):
    # Hedef klasörü oluştur (eğer yoksa)
    os.makedirs(kayit_yeri, exist_ok=True)

    # Kaynak dizini tarayın
    for root, dirs, files in os.walk(dosya_yolu):
        # Eğer vocals.wav dosyasını bulursak
        if 'vocals.wav' in files:
            # vocals.wav dosyasının tam yolunu alın
            vocal_yolu = os.path.join(root, 'vocals.wav')
            
            # Dosya ismini çakışmaları önlemek için alt klasör isimleriyle birlikte alın
            rel_path = os.path.relpath(root, dosya_yolu).replace(os.sep, "_")
            hedef_yolu = os.path.join(kayit_yeri, f"{rel_path}_vocals.wav")
            
            # Dosyayı hedef klasöre kopyalayın
            shutil.copy2(vocal_yolu, hedef_yolu)
            print(f"Taşındı: {vocal_yolu} -> {hedef_yolu}")

# Kullanım
dosya_yolu = "belirsiz/islenmis"  # Tarama yapılacak ana klasörün yolu
kayıt_yeri = "belirsiz/ayık"  # vocals.wav dosyalarının toplanacağı hedef klasör

vocal_bulma(dosya_yolu, kayıt_yeri)

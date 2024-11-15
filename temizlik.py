import os
from spleeter.separator import Separator
import subprocess

def webm_to_wav(input_path, output_path):
    # ffmpeg ile webm dosyasını wav formatına dönüştürme
    commend = f'ffmpeg -i "{input_path}" -ac 2 -f wav "{output_path}"'
    subprocess.call(commend, shell=True)

if __name__ == '__main__':
    separator = Separator('spleeter:2stems')
    dosya_yolu  = "belirsiz"
    dosya_cikis  = "belirsiz/islenmis" 
    temp_directory  = "wav_dosyalar"

    # Geçici wav dosyalarını saklamak için klasör oluştur
    os.makedirs(temp_directory , exist_ok=True)
    os.makedirs(dosya_cikis, exist_ok=True)

    # Tüm webm dosyalarını al
    audio_files = [f for f in os.listdir(dosya_yolu) if f.endswith('.webm')]
    #Ses dosyaları üzerinde işlem
    for audio_file in audio_files:
        dosya_yolu = os.path.join(dosya_yolu, audio_file)
        temp_yol = os.path.join(temp_directory , audio_file.replace('.webm', '.wav'))
        output_path = os.path.join(dosya_cikis, audio_file.split('.')[0])

        try:
            # Webm dosyasını wav formatına dönüştür
            webm_to_wav(dosya_yolu, temp_yol)

            # Spleeter ile ayırma işlemi yap
            separator.separate_to_file(temp_yol, output_path)
            print(f"{audio_file} dosyası işlendi.")
        except Exception as e:
            print(f"Hata: {audio_file} dosyası işlenemedi. {e}")
            continue


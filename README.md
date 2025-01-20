# Speech-Emotion-Detection-and-Analysis

# Data Toplama
**Speech-Emotion-Detection-and-Analysis** duygu analizi için ses verisi toplama amacıyla geliştirilmiş bir Python programıdır. Bu program, özellikle YouTube'dan ses verilerini indirir ve verileri sesli duygu analizine uygun formatta işler. Topladığı ses dosyalarını belirli kategorilere ayırarak, daha sonra analiz edebilecek şekilde düzenler.

## Proje Özeti

Bu program, **YouTube** gibi platformlardan konuşma içerikli ses dosyalarını indirip, bu verileri duygusal içeriklerine göre ayırır. Amacı, veri seti oluşturmak ve farklı duygu kategorilerine göre sınıflandırma yapabilmek için doğru ve düzenli ses dosyaları sağlamaktır.

Program ile ayrıca:
- Ses dosyalarını indirir.
- Ses dosyalarında belirli düzenlemeler yaparak, duygu analizine uygun hale getirir.
- Boş (sessiz) ses dosyalarını ayıklayarak temizler.
- Ses dosyalarını kategorilere ayırarak düzenler.

### Şu anki Özellikler

- **Ses Dosyası İndirme**: YouTube'dan ses dosyalarını indirir ve ilgili formata dönüştürür.
- **Boş Ses Dosyaları Ayıklama**: Sessiz olan ses dosyalarını ayıklar ve gereksiz verilerden temizler.
- **Veri Organizasyonu**: Ses dosyalarını duygusal içeriklerine göre düzenler ve kategorize eder.
- **Ses Dosyası İşleme**: İndirilen ses dosyalarını işleyip veriye uygun formatta düzenler.

### Gelecek Planları

- **Duygusal İçerik Sınıflandırması**: Toplanan ses verileri için duygusal içerik sınıflandırması yapılabilir.
- **Daha Fazla Kaynak Ekleme**: YouTube dışında başka platformlardan veri toplamak için yeni kaynaklar eklenebilir.
- **Duygu Etiketleme ve Analiz**: Duygusal içeriklerin etiketlenmesi ve analiz edilmesi üzerinde çalışmalar yapılacaktır.

## Gereksinimler

Programı çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekir:

- `yt-dlp`: YouTube ve diğer platformlardan video ve ses dosyalarını indirmek için kullanılır.
- `pydub`: Ses dosyalarını işlemek için kullanılır.
- `spleeter`: Ses kaynağı ayırma aracı, müzikten ses ve konuşma gibi kaynakları ayırmak için kullanılır.
- `shutil`: Dosya ve dizin işlemleri için kullanılır.
- `os`: Dosya yolu işlemleri için kullanılır.
- `selenium` : Web tarayıcısını otomatikleştirmek için kullanılır.
- `beautifulsoup4` : HTML ve XML verilerini işlemek için kullanılır.

# Model Eğitimi 
## Yapay Zeka ile Ses Verisi Analizi: Transformer Modellerinin Karşılaştırılması

Bu proje, ses verisi üzerinde **Hubert**, **Wav2vec**, **WavLM** ve **Data2Vec** gibi dört farklı transformör modelinin performansını karşılaştırmayı amaçlamaktadır. Modeller, ses sinyallerinin özelliklerini analiz etmek ve farklı duygusal durumları tanımlamak için çeşitli metrikler ve görselleştirme yöntemleri kullanmıştır.

## Proje Özeti

Transformör modelleri, doğal dil işleme, görüntü işleme ve ses analizi gibi alanlarda başarılı sonuçlar vermektedir. Bu projede, ses verisinin frekans ve zaman domain'lerindeki özellikleri aşağıdaki teknikler kullanılarak analiz edilmiştir:

- **Spektrogram** ve **waveplot** grafikleri ile görselleştirme.
- **Accuracy**, **Recall**, **Precision**, **F-Score**, ve **AUC** gibi performans metrikleriyle model değerlendirmesi.

## Veri Hazırlama ve Ön İşleme

Proje kapsamında kullanılan ses verisi, aşağıdaki işlemlerden geçmiştir:

1. **Gürültü Azaltma**: Filtreleme teknikleri ile arka plan gürültüsü azaltıldı.
2. **Normalizasyon**: Ses sinyalleri sabit bir genlik aralığına getirildi.
3. **Özellik Çıkarımı**: MFCC gibi ses özellikleri çıkarıldı.

## Kullanılan Modeller

1. **Hubert**: Maskeli öğrenme yöntemiyle ses temsilleri çıkaran model.
2. **Wav2vec**: Ses verilerinden etkili özellikler çıkaran model.
3. **WavLM**: Büyük ölçekli ses verisi üzerinde eğitilmiş model.
4. **Data2Vec**: Çeşitli veri tipleri için genel bir öğrenme çerçevesi.

## Performans Sonuçları

Modellerin karşılaştırmalı sonuçları aşağıdaki tabloya yansıtılmıştır:

| Model    | Accuracy | Recall | Precision | F-Score | AUC  | Sensitivity |
|----------|----------|--------|-----------|---------|------|-------------|
| Hubert   | 0.27     | 0.27   | 0.07      | 0.12    | 0.56 | 0.25        |
| Wav2vec  | 0.25     | 0.25   | 0.12      | 0.16    | 0.53 | 0.25        |
| WavLM    | 0.36     | 0.36   | 0.20      | 0.24    | 0.64 | 0.64        |
| Data2Vec | 0.25     | 0.25   | 0.06      | 0.10    | 0.50 | 0.50        |

## Çalıştırma Talimatları

### Gereksinimler

Projenin çalıştırılabilmesi için aşağıdaki paketlerin yüklü olması gerekmektedir:

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- PyTorch

### Kod İçinden Bazı Grafikler
![indir (14)](https://github.com/user-attachments/assets/19874314-a2c1-4568-af28-29d60f4b076a)

- Burada Nötr ses duygusu için bir waveplot grafiği yer almaktadır.

![indir (20)](https://github.com/user-attachments/assets/662dcb49-b79a-4a78-b47f-d9b5d10f3276)

- Burada Wav2sec adlı modelin verileri arasında ROC eğrisi yer almaktadır.

![indir (11)](https://github.com/user-attachments/assets/5f43e50e-48cf-4556-9bfa-eb67370d52d1)

- Burada öfkeli duygusu için bir spectogram bulunmaktadır.

![indir (18)](https://github.com/user-attachments/assets/fd85499c-0b8b-417b-9f0b-a2d06a5352e1)

- Burada Wav2sec için epoch loss grafiği bulunmaktadır.

  



### Google Drive(Veriseti) Linki: https://drive.google.com/drive/folders/1ND_xq83rLYEkg_mtz7T2H_3nS4CB1Ny8
### Google Drive(Kod) Linki: https://drive.google.com/drive/folders/1waJZmucslhWvTvBu-Kz83W9CrEmlkJZ7?usp=sharing




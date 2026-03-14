# Titanic Survival Predictor API

Bu proje, Titanic yolcularının demografik verilerine dayanarak hayatta kalma ihtimalini tahmin eden basit  bir **Machine Learning API** servisidir.

## Teknolojiler
- **Model:** Random Forest (Scikit-learn)
- **API Framework:** FastAPI
- **Deployment:** Render.com
- **Serialization:** Joblib

1. `pip install -r requirements.txt`
2. `uvicorn main:app --reload`

## Canly API URL

https://titanic-fastapi-hc7s.onrender.com/docs
Harika örnekler seçmişsin! Özellikle 1. sınıf kadın yolcunun hayatta kalıp, 1. sınıf yaşlı erkek yolcunun hayatta kalamaması modelin mantıklı çalıştığını çok iyi kanıtlıyor.

İşte GitHub **README.md** dosyana direkt kopyalayıp yapıştırabileceğin, profesyonelce düzenlenmiş "Örnek Senaryolar" bölümü:

---

## Örnek Senaryolar ve Model Tahminleri (Demo)

API üzerinden yapılan testlerde modelin ürettiği gerçek sonuçlar aşağıdadır. Bu senaryolar, modelin değişkenlere (sınıf, cinsiyet, yaş vb.) verdiği tepkileri göstermektedir.

### Senaryo 1: Üst Sınıf Genç Kadın

* **Profil:** 1. Sınıf, Kadın, 20 Yaşında.
* **Model Tahmini:** ✅ **Survived (Hayatta Kaldı)**

```json
// Request
{ "Pclass": 1, "Sex": 1, "Age": 20, "SibSp": 0, "Parch": 0, "Fare": 0 }

// Response
{ "prediction": "Survived", "survived_binary": 1 }

```

---

### Senaryo 2: Üst Sınıf Yaşlı Erkek

* **Profil:** 1. Sınıf, Erkek, 56 Yaşında.
* **Model Tahmini:** ❌ **Not Survived (Hayatta Kalamadı)**

```json
// Request
{ "Pclass": 1, "Sex": 0, "Age": 56, "SibSp": 2, "Parch": 1, "Fare": 0 }

// Response
{ "prediction": "Not Survived", "survived_binary": 0 }

```

---

### Senaryo 3: Alt Sınıf Genç Erkek

* **Profil:** 3. Sınıf, Erkek, 20 Yaşında.
* **Model Tahmini:** ❌ **Not Survived (Hayatta Kalamadı)**

```json
// Request
{ "Pclass": 3, "Sex": 0, "Age": 20, "SibSp": 2, "Parch": 1, "Fare": 0 }

// Response
{ "prediction": "Not Survived", "survived_binary": 0 }

```

---

### Senaryo 4: Ailesiyle Seyahat Eden Üst Sınıf Kadın

* **Profil:** 1. Sınıf, Kadın, 20 Yaşında, 2 Aile Üyesi.
* **Model Tahmini:** ✅ **Survived (Hayatta Kaldı)**

```json
// Request
{ "Pclass": 1, "Sex": 1, "Age": 20, "SibSp": 1, "Parch": 1, "Fare": 0 }

// Response
{ "prediction": "Survived", "survived_binary": 1 }

```

---

### Teknik Notlar

* **Sex:** `0` Erkek, `1` Kadın olarak kodlanmıştır.
* **Pclass:** Yolcu sınıfını temsil eder (`1` en yüksek, `3` en düşük).
* **Model:** Scikit-learn Random Forest Classifier kullanılarak eğitilmiştir.


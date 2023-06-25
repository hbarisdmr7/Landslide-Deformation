import h5py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from osgeo import gdal
from osgeo import osr

# HDF5 dosyasını yükleme
filename = r'C:\Users\alkumru\Desktop\cumgeotif\cum.h5'
f = h5py.File(filename, 'r')

# Girdi verilerini al
imdates = f['imdates'][:]
data = f['cum'][:]

# Veri şeklini düzenleme
num_samples, height, width = data.shape
data = data.reshape(num_samples, height * width)
print("Veri şekli (num_samples, height, width):", data.shape)

# 'nan' değerleri 0 ile değiştirme
data = np.nan_to_num(data, nan=0.0)

# 'nan' değerleri komşu değerlerin ortalamasıyla doldurma
for i in range(num_samples):
    zero_indices = data[i] == 0
    non_zero_indices = np.logical_not(zero_indices)
    zero_count = np.sum(zero_indices)

    if zero_count > 0:
        # Komşu değerlerin ortalamasını hesaplama
        neighbor_values = np.zeros_like(data[i])
        for j in range(height * width):
            if zero_indices[j]:
                # Üst, alt, sol, sağ piksellerin değerlerini topla
                neighbors = []
                if j - width >= 0:
                    neighbors.append(data[i][j - width])  # üst piksel
                if j + width < height * width:
                    neighbors.append(data[i][j + width])  # alt piksel
                if j % width != 0:
                    neighbors.append(data[i][j - 1])  # sol piksel
                if (j + 1) % width != 0:
                    neighbors.append(data[i][j + 1])  # sağ piksel

                neighbor_values[j] = np.mean(neighbors)

        # 0 değerlerini komşu değerlerin ortalamasıyla doldurma
        data[i][zero_indices] = neighbor_values[zero_indices]


# Eğitim ve test veri setlerini oluşturma
train_size = 158  # İlk 158 veri örneği eğitim verisi olarak kullanılır
train_data = data[:train_size]
test_data = data[train_size:]
print("Eğitim veri seti şekli:", train_data.shape)
print("Test veri seti şekli:", test_data.shape)

# Girdi ve çıktı verilerini oluşturma
lookback = 8  # Tahmin için kullanılacak önceki gözlemler sayısı
X_train, y_train = [], []
for i in range(lookback, len(train_data)):
    X_train.append(train_data[i - lookback:i])
    y_train.append(train_data[i])
X_train, y_train = np.array(X_train), np.array(y_train)
print("Eğitim verisi X şekli:", X_train.shape)
print("Eğitim verisi y şekli:", y_train.shape)

X_test, y_test = [], []
for i in range(lookback, len(test_data)):
    X_test.append(test_data[i - lookback:i])
    y_test.append(test_data[i])
X_test, y_test = np.array(X_test), np.array(y_test)
print("Test verisi X şekli:", X_test.shape)
print("Test verisi y şekli:", y_test.shape)

# LSTM modelini oluşturma
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(lookback, height * width)))
model.add(LSTM(units=50))
model.add(Dense(units=height * width))
model.compile(optimizer='adam', loss='mean_squared_error')

# Modeli eğitme
print("Model eğitimi başlıyor...")
model.fit(X_train, y_train, epochs=2000, batch_size=32)
print("Model eğitimi tamamlandı.")

# Modelin tahmin yapması
print("Tahmin yapılıyor...")
predicted = model.predict(X_test)
print("Tahminler yapıldı. Tahmin şekli:", predicted.shape)

# Tahmin sonuçlarını kaydetme
output_folder = r'C:\Users\alkumru\Desktop\cumgeotif\predicted'
for i in range(len(predicted)):
    prediction = predicted[i].reshape((height, width))

    # Verileri GeoTIFF olarak kaydetme
    output_path = output_folder + f'/tahmin_{i+1}.tif'
    print("Kaydediliyor:", output_path)
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(output_path, width, height, 1, gdal.GDT_Float32)
    dataset.GetRasterBand(1).WriteArray(prediction)
    
    # Projeksiyon dönüşümü için ayarları yapma
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(3857)
    dataset.SetProjection(srs.ExportToWkt())

    # Veriye coğrafi dönüşüm bilgisini ekleme
    geotransform = (0, 1, 0, 0, 0, 1)  # Örnek bir coğrafi dönüşüm
    dataset.SetGeoTransform(geotransform)

    
    dataset.FlushCache()
    dataset = None

# HDF5 dosyasını kapatma
f.close()

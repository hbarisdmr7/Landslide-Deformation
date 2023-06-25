import os
import h5py
import numpy as np
from osgeo import gdal, osr
from datetime import datetime

filename = r'C:\Users\alkumru\Desktop\cumgeotif\cum.h5'
output_folder = r'C:\Users\alkumru\Desktop\cumgeotif\geotifs'  # Çıktı klasörü

# HDF5 dosyasını aç
f = h5py.File(filename, 'r')

# Girdi verilerini al
imdates = f['imdates'][:]
data = f['cum'][:]


# Verileri tarihe göre sırala
sorted_indices = np.argsort(imdates)
sorted_dates = imdates[sorted_indices]
sorted_dates = [datetime.strptime(str(date), "%Y%m%d").date() for date in sorted_dates]  # Tarihleri dönüştür
sorted_data = data[sorted_indices]

# Projeksiyon bilgisini ayarla
output_epsg = 3857
output_srs = osr.SpatialReference()
output_srs.ImportFromEPSG(output_epsg)
output_projection = output_srs.ExportToWkt()

# Her bir tarih için geotif dosyası oluştur
for i, date in enumerate(sorted_dates):
    # Tarih formatını düzenleme işlemini burada yapabilirsiniz
    # Örnek olarak 'YYYYMMDD' formatında bir tarih oluşturulabilir
    formatted_date = date.strftime("%Y%m%d")

    # Geotif dosya adı
    output_filename = os.path.join(output_folder, f'cum_{formatted_date}.tif')

    # Verileri geotif olarak kaydetme işlemi burada yapılabilir
    driver = gdal.GetDriverByName("GTiff")
    cols, rows = sorted_data[i].shape
    out_dataset = driver.Create(output_filename, rows, cols, 1, gdal.GDT_Float32)

    # Veriye projeksiyon bilgisini ekleme
    out_dataset.SetProjection(output_projection)

    # Veriye coğrafi dönüşüm bilgisini ekleme
    geotransform = (0, 1, 0, 0, 0, 1)  # Örnek bir coğrafi dönüşüm
    out_dataset.SetGeoTransform(geotransform)

    # Veriyi geotif dosyasına yazma
    out_band = out_dataset.GetRasterBand(1)
    out_band.WriteArray(sorted_data[i])

    out_band.FlushCache()
    out_dataset = None

# HDF5 dosyasını kapat
f.close()

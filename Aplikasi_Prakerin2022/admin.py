from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_siswa1, Model_dudi, Model_prakerin1, Model_perjalanan, Model_pengumuman, Model_walikelas, Model_catatan, Model_komentar, Model_kegiatan

admin.site.register(Model_siswa1)
admin.site.register(Model_dudi)
admin.site.register(Model_prakerin1)
admin.site.register(Model_perjalanan)
admin.site.register(Model_pengumuman)
admin.site.register(Model_walikelas)
admin.site.register(Model_catatan)
admin.site.register(Model_komentar)
admin.site.register(Model_kegiatan)
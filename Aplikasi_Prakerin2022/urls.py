from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_Prakerin2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views

from .views import index, HomeView, LogoutView, Data_siswa, Tambah_siswa, Hapus_siswa, Edit_siswa, Data_walikelas, Tambah_wali, Hapus_walikelas, Edit_walikelas, Data_pengumuman, Tambah_pengumuman, Hapus_pengumuman, Edit_pengumuman, Data_dudi, Hapus_dudi, Tambah_dudi, Edit_dudi, Data_prakerin, Hapus_prakerin, Tambah_prakerin, Edit_prakerin, Panggil_prakerin, Data_perjalanan, Edit_perjalanan, Hapus_perjalanan, Tambah_perjalanan, Proses_perjalanan, Menu, Lp_prakerin, Lp_prakerin_kl, Lp_perjalanan, Lp_perjalanan_kl, Lp_siswa, Lp_dudi, WEBSITE, Login_prakerin, Logout_prakerin, Chek_prakerin, Hapus_catatan, Data_catatan, PetugasV, T_PetugasV, HapuspetugasV, EditPetugasV, Data_pengumuman_pembina, Data_perjalanan_pembina, Data_prakerin_pembina,  Proses_komentar, Hapus_komentar, Tambah_kegiatan, Check_kegiatan,  Data_kegiatan, Hapus_kegiatan
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^login/$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),
    


    # data siswa
    url(r'^Siswa/$',Data_siswa, name="Siswa"),
    url(r'^Tambah_siswa/$',Tambah_siswa, name="Tambah_siswa"),
    url(r'^hapus_siswa/(?P<hapus_nis>[0-9]+)$',Hapus_siswa, name="hapus_siswa"),
    url(r'^edit_siswa/(?P<id_s>[0-9]+)$',Edit_siswa, name="edit_siswa"),

    # data walikelas
    url(r'^Wali_kelas/$',Data_walikelas, name="Wali_kelas"),
    url(r'^Tambah_wali/$',Tambah_wali, name="Tambah_wali"),
    url(r'^hapus_walikelas/(?P<hapus_id>[0-9]+)$',Hapus_walikelas, name="hapus_walikelas"),
    url(r'^edit_walikelas/(?P<id_w>[0-9]+)$',Edit_walikelas, name="edit_walikelas"),

    # data pengumuman
    url(r'^Pengumuman/$',Data_pengumuman, name="Pengumuman"),
    url(r'^Tambah_pengumuman/$',Tambah_pengumuman, name="Tambah_pengumuman"),
    url(r'^hapus_pengumuman/(?P<hapus_peng>[0-9]+)$',Hapus_pengumuman, name="hapus_pengumuman"),
    url(r'^edit_pengumuman/(?P<id_p>[0-9]+)$',Edit_pengumuman, name="edit_pengumuman"),

    # data dudi
    url(r'^Dudi/$',Data_dudi, name="Dudi"),
    url(r'^Tambah_dudi/$',Tambah_dudi, name="Tambah_dudi"),
    url(r'^hapus_dudi/(?P<hapus_dudi>[0-9]+)$',Hapus_dudi, name="hapus_dudi"),
    url(r'^edit_dudi/(?P<id_dudi>[0-9]+)$',Edit_dudi, name="edit_dudi"),

    # data prakerin
    url(r'^Prakerin/$',Data_prakerin, name="Prakerin"),
    url(r'^Tambah_prakerin/$',Tambah_prakerin, name="Tambah_prakerin"),
    url(r'^hapus_prakerin/(?P<hapus_pr>[0-9]+)$',Hapus_prakerin, name="hapus_prakerin"),
    url(r'^edit_prakerin/(?P<id_prakerin>[0-9]+)$',Edit_prakerin, name="edit_prakerin"),
    url(r'^panggil_prakerin/(?P<id_nis>[0-9]+)$',Panggil_prakerin, name="panggil_prakerin"),

    # data perjalanan
    url(r'^Perjalanan/$',Data_perjalanan, name="Perjalanan"),
    url(r'^Tambah_perjalanan/$',Tambah_perjalanan, name="Tambah_perjalanan"),
    url(r'^hapus_perjalanan/(?P<hapus_per>[0-9]+)$',Hapus_perjalanan, name="hapus_perjalanan"),
    url(r'^edit_perjalanan/(?P<id_per>[0-9]+)$',Edit_perjalanan, name="edit_perjalanan"),
    url(r'^proses/(?P<id>[0-9]+)$',Proses_perjalanan, name="proses"),

    # catatan 
    url(r'^Catatan/$',Data_catatan, name="Catatan"),
    url(r'^hapus_catatan/(?P<hapus_c>[0-9]+)$',Hapus_catatan, name="hapus_catatan"),
    # kegiatan
    url(r'^Data_kegiatan/$',Data_kegiatan, name="Data_kegiatan"),
    url(r'^Hapus_kegiatan/(?P<hapus_kegiatan>[0-9]+)$',Hapus_kegiatan, name="Hapus_kegiatan"),

    #petugas
    url(r'^petugas/$',PetugasV, name="petugas"),
    url(r'^T_petugas/$',T_PetugasV, name="T_petugas"),
    url(r'^hapus_petugas/(?P<hapuspt_id>[0-9]+)$',HapuspetugasV, name="hapus_petugas"),    
    url(r'^edit_petugas/(?P<id_pt>[0-9]+)$',EditPetugasV, name="edit_petugas"),    

    # menu laporan
    url(r'^menu/$',Menu, name="menu"),
    url(r'^lp_prakerin/$',Lp_prakerin, name="lp_prakerin"),
    url(r'^lp_prakerin_kl/$',Lp_prakerin_kl, name="lp_prakerin_kl"),
    # perjalanan
    url(r'^lp_perjalanan/$',Lp_perjalanan, name="lp_perjalanan"),
    url(r'^lp_perjalanan_kl/$',Lp_perjalanan_kl, name="lp_perjalanan_kl"),

    # lp siswa
    url(r'^lp_siswa/$',Lp_siswa, name="lp_siswa"),
    # lp dudi
    url(r'^lp_dudi/$',Lp_dudi, name="lp_dudi"),

    # halaman website
    url(r'^WEBSITE/$',WEBSITE, name="WEBSITE"),
    url(r'^login_pr/$',Login_prakerin, name="login_pr"),
    url(r'^logout_pr/$',Logout_prakerin, name="logout_pr"),
    url(r'^chek_praktek/$',Chek_prakerin, name="chek_praktek"),

    # pembina
    url(r'^Pengumuman_pembina/$',Data_pengumuman_pembina, name="Pengumuman_pembina"),
    url(r'^Perjalanan_pembina/$',Data_perjalanan_pembina, name="Perjalanan_pembina"),
    url(r'^Prakerin_pembina/$',Data_prakerin_pembina, name="Prakerin_pembina"),
    # komentar
    url(r'^Proses_komentar/$',Proses_komentar, name="Proses_komentar"),
    url(r'^Hapus_komentar/(?P<hapus_komen>[0-9]+)$',Hapus_komentar, name="Hapus_komentar"),    


    # kegiatan
    url(r'^Tambah_kegiatan/$',Tambah_kegiatan, name="Tambah_kegiatan"),
    url(r'^Check_kegiatan/$',Check_kegiatan, name="Check_kegiatan"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_siswa1(models.Model):
	nis	= models.CharField(max_length = 25)
	nama	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 25)
	alamat	=models.CharField(max_length = 1200)
	kelas	=models.CharField(max_length = 12)
	foto	=models.ImageField(upload_to ='Foto_siswa/', null=True)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama)

class Model_dudi(models.Model):
	id_dudi	= models.CharField(max_length = 25)
	nama_dudi	=models.CharField(max_length = 1200)
	tempat_dudi	=models.CharField(max_length = 1025)
	alamat	=models.CharField(max_length = 1200)
	telp	=models.CharField(max_length = 12)
	ketua_dudi	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_dudi)		

class Model_prakerin1(models.Model):
	id_prakerin	= models.CharField(max_length = 25)
	nis	=models.CharField(max_length = 1200)
	nama_dudi	=models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)
	nama_siswa	=models.CharField(max_length = 1200)
	pembina	=models.CharField(max_length = 1200)
	kelompok	=models.CharField(max_length = 12)
	jumlah_kelompok	=models.CharField(max_length = 12)
	tgl_prakerin	=models.CharField(max_length = 12)
	keterangan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_dudi)		

class Model_perjalanan(models.Model):
	id_perjalanan	= models.CharField(max_length = 25)
	id_prakerin	=models.CharField(max_length = 12)
	nis	=models.CharField(max_length = 12)
	nama_kelompok	=models.CharField(max_length = 1200)
	nama_siswa	=models.CharField(max_length = 1200)
	nama_dudi	=models.CharField(max_length = 1200)
	tgl_perjalanan	=models.CharField(max_length = 12)
	jam	=models.CharField(max_length = 12)
	tahun	=models.CharField(max_length = 12)
	keterangan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_dudi)				

class Model_pengumuman(models.Model):
	id_pengumuman	= models.CharField(max_length = 25)
	nama_pengumuman	=models.CharField(max_length = 1200)
	tgl_pelaksanaan	=models.CharField(max_length = 25)
	keterangan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pengumuman)		

class Model_walikelas(models.Model):
	id_wali	= models.CharField(max_length = 25)
	nama_lengkap	=models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 12)
	nohp	=models.CharField(max_length = 12)
	status	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_lengkap)


class Model_catatan(models.Model):
	id_catatan	= models.CharField(max_length = 25)
	nis	=models.CharField(max_length = 12)
	nama_siswa	=models.CharField(max_length = 1200)
	kelompok	=models.CharField(max_length = 1200)
	title_tugas	=models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_siswa)		

# komentar pembina
class Model_komentar(models.Model):
	nis	= models.CharField(max_length = 25)
	nama	=models.CharField(max_length = 1200)
	komentar	=models.CharField(max_length = 25)
	kelompok	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama)

# kegiatan
class Model_kegiatan(models.Model):
	kelompok	= models.CharField(max_length = 25)
	nama_kegiatan	=models.CharField(max_length = 1200)
	deskripsi	=models.CharField(max_length = 25)
	foto	=models.ImageField(upload_to ='Foto_siswa/', null=True)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.kelompok)
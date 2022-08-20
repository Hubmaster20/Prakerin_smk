from .forms import Form_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import ijinkan_pengguna, tolakhalaman_ini, pilihan_login
from .models import Model_siswa1, Model_dudi, Model_prakerin1, Model_perjalanan, Model_pengumuman, Model_walikelas, Model_catatan, User, Model_komentar, Model_kegiatan
import hashlib
from django.conf import settings


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'index.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def HomeView(request):	
	context = {
	'page_title':'Home'
	}
	test_group = Group.objects.get(name="pembina")
	admin_group = request.user.groups.all()

	template_name = None
	if test_group in admin_group:
		template_name = 'halaman_pembina.html'
	else:
		template_name = 'home.html'

	return render(request, template_name,  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	

	# data siswa
@login_required(login_url=settings.LOGIN_URL)
def Data_siswa(request):
	data_siswa = Model_siswa1.objects.all()
	context = {	
	'data_siswa': data_siswa,
	}
	return render(request, 'Master_data/data_siswa/tabel.html',  context)	

@login_required(login_url=settings.LOGIN_URL)
def Tambah_siswa(request):
	if request.method == 'POST':
		Model_siswa1.objects.create(
			nis = request.POST['nis'],
			nama = request.POST['nama'],
			jk = request.POST['jk'],			
			alamat = request.POST['alamat'],			
			kelas = request.POST['kelas'],			
			foto = request.FILES['foto'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Siswa/")	
	context = {	
	'Tambah siswa': 'Tambah siswa'
	}
	return render(request, 'Master_data/data_siswa/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def Hapus_siswa(request, hapus_nis):
	Model_siswa1.objects.filter(id=hapus_nis).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Siswa')			

@login_required(login_url=settings.LOGIN_URL)
def Edit_siswa(request, id_s):		
	edit_siswa = Model_siswa1.objects.get(id=id_s)
	if request.method == 'POST':		
			edit_siswa.nis = request.POST.get('nis')
			edit_siswa.nama = request.POST.get('nama')			
			edit_siswa.jk = request.POST.get('jk')						
			edit_siswa.alamat = request.POST.get('alamat')						
			edit_siswa.kelas = request.POST.get('kelas')						
			edit_siswa.foto = request.FILES.get('foto')						
			edit_siswa.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Siswa')

	context = {'edit_siswa': edit_siswa}
	return render(request, 'Master_data/data_siswa/edit.html',  context)	


	# data catatan
@login_required(login_url=settings.LOGIN_URL)
def Data_catatan(request):
	data_catatan = Model_catatan.objects.all()
	context = {	
	'data_catatan': data_catatan,
	}
	return render(request, 'Master_data/data_catatan/tabel.html',  context)		

@login_required(login_url=settings.LOGIN_URL)
def Hapus_catatan(request, hapus_c):
	Model_catatan.objects.filter(id=hapus_c).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Catatan')				
# kegiatan admin
@login_required(login_url=settings.LOGIN_URL)
def Data_kegiatan(request):
	data = Model_kegiatan.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_kegiatan/tabel.html',  context)		

@login_required(login_url=settings.LOGIN_URL)
def Hapus_kegiatan(request, hapus_kegiatan):
	Model_kegiatan.objects.filter(id=hapus_kegiatan).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Data_kegiatan')				

	# data wali kelas
@login_required(login_url=settings.LOGIN_URL)	
def Data_walikelas(request):
	data_walikelas = Model_walikelas.objects.all()
	context = {	
	'data_walikelas': data_walikelas,
	}
	return render(request, 'Master_data/data_wali_kelas/tabel.html',  context)		

@login_required(login_url=settings.LOGIN_URL)
def Tambah_wali(request):
	if request.method == 'POST':
		Model_walikelas.objects.create(
			id_wali = request.POST['id_wali'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],		
			jk = request.POST['jk'],							
			nohp = request.POST['nohp'],			
			status = request.POST['status'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Wali_kelas/")	
	context = {	
	'Tambah wali': 'Tambah wali'
	}
	return render(request, 'Master_data/data_wali_kelas/tambah.html', context)	

@login_required(login_url=settings.LOGIN_URL)
def Hapus_walikelas(request, hapus_id):
	Model_walikelas.objects.filter(id=hapus_id).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Wali_kelas')				

@login_required(login_url=settings.LOGIN_URL)
def Edit_walikelas(request, id_w):		
	edit_walikelas = Model_walikelas.objects.get(id=id_w)
	if request.method == 'POST':		
			edit_walikelas.id_wali = request.POST.get('id_wali')
			edit_walikelas.nama_lengkap = request.POST.get('nama_lengkap')			
			edit_walikelas.alamat = request.POST.get('alamat')			
			edit_walikelas.jk = request.POST.get('jk')											
			edit_walikelas.nohp = request.POST.get('nohp')						
			edit_walikelas.status = request.POST.get('status')						
			edit_walikelas.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Wali_kelas')

	context = {'edit_walikelas': edit_walikelas}
	return render(request, 'Master_data/data_wali_kelas/edit.html',  context)		

	# data pengumuman
@login_required(login_url=settings.LOGIN_URL)
def Data_pengumuman(request):
	data_pengumuman = Model_pengumuman.objects.all()
	context = {	
	'data_pengumuman': data_pengumuman,
	}
	return render(request, 'Master_data/data_pengumuman/tabel.html',  context)			

@login_required(login_url=settings.LOGIN_URL)
def Tambah_pengumuman(request):
	if request.method == 'POST':
		Model_pengumuman.objects.create(
			id_pengumuman = request.POST['id_pengumuman'],
			nama_pengumuman = request.POST['nama_pengumuman'],
			tgl_pelaksanaan = request.POST['tgl_pelaksanaan'],		
			keterangan = request.POST['keterangan'],							
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Pengumuman/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_pengumuman/tambah.html', context)		

@login_required(login_url=settings.LOGIN_URL)
def Hapus_pengumuman(request, hapus_peng):
	Model_pengumuman.objects.filter(id=hapus_peng).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Pengumuman')

@login_required(login_url=settings.LOGIN_URL)
def Edit_pengumuman(request, id_p):		
	edit_peng = Model_pengumuman.objects.get(id=id_p)
	if request.method == 'POST':		
			edit_peng.id_pengumuman = request.POST.get('id_pengumuman')
			edit_peng.nama_pengumuman = request.POST.get('nama_pengumuman')			
			edit_peng.tgl_pelaksanaan = request.POST.get('tgl_pelaksanaan')			
			edit_peng.keterangan = request.POST.get('keterangan')											
			edit_peng.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Pengumuman')

	context = {'edit_peng': edit_peng}
	return render(request, 'Master_data/data_pengumuman/edit.html',  context)			

	# data dudi
@login_required(login_url=settings.LOGIN_URL)
def Data_dudi(request):
	data_dudi = Model_dudi.objects.all()
	context = {	
	'data_dudi': data_dudi,
	}
	return render(request, 'Master_data/data_dudi/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_dudi(request):
	if request.method == 'POST':
		Model_dudi.objects.create(
			id_dudi = request.POST['id_dudi'],
			nama_dudi = request.POST['nama_dudi'],
			tempat_dudi = request.POST['tempat_dudi'],		
			alamat = request.POST['alamat'],
			telp = request.POST['telp'],
			ketua_dudi = request.POST['ketua_dudi'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Dudi/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_dudi/tambah.html', context)		

@login_required(login_url=settings.LOGIN_URL)
def Hapus_dudi(request, hapus_dudi):
	Model_dudi.objects.filter(id=hapus_dudi).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Dudi')	

@login_required(login_url=settings.LOGIN_URL)
def Edit_dudi(request, id_dudi):		
	edit_dudi = Model_dudi.objects.get(id=id_dudi)
	if request.method == 'POST':		
			edit_dudi.id_dudi = request.POST.get('id_dudi')
			edit_dudi.nama_dudi = request.POST.get('nama_dudi')			
			edit_dudi.tempat_dudi = request.POST.get('tempat_dudi')			
			edit_dudi.alamat = request.POST.get('alamat')
			edit_dudi.telp = request.POST.get('telp')
			edit_dudi.ketua_dudi = request.POST.get('ketua_dudi')
			edit_dudi.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Dudi')

	context = {'edit_dudi': edit_dudi}
	return render(request, 'Master_data/data_dudi/edit.html',  context)

	# data prakerin
@login_required(login_url=settings.LOGIN_URL)
def Data_prakerin(request):
	data_prakerin = Model_prakerin1.objects.all()
	context = {	
	'data_prakerin': data_prakerin,
	}
	return render(request, 'Master_data/data_prakerin/tabel.html',  context)	

@login_required(login_url=settings.LOGIN_URL)
def Tambah_prakerin(request):
	# cari data
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data_siswa = Model_siswa1.objects.filter(kelas=cari_data)
	else:
		data_siswa = Model_siswa1.objects.filter(kelas=None)				
		# end
	context = {	
	'Tambah': 'Tambah',
	'data_siswa': data_siswa,
	}
	return render(request, 'Master_data/data_prakerin/tambah.html', context)			

@login_required(login_url=settings.LOGIN_URL)
def Panggil_prakerin(request, id_nis):		
	data_dudi = Model_dudi.objects.all()
	select_wali = Model_walikelas.objects.all()
	panggil = Model_siswa1.objects.get(id=id_nis)
	if request.method == 'POST':
		Model_prakerin1.objects.create(
			id_prakerin = request.POST['id_prakerin'],
			nis = request.POST['nis'],
			nama_dudi = request.POST['nama_dudi'],
			alamat = request.POST['alamat'],
			nama_siswa = request.POST['nama_siswa'],
			pembina = request.POST['pembina'],
			kelompok = request.POST['kelompok'],
			jumlah_kelompok = request.POST['jumlah_kelompok'],
			tgl_prakerin = request.POST['tgl_prakerin'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Prakerin/")	
	context = {	
	'panggil': panggil,
	'data_dudi': data_dudi,
	'select_wali': select_wali,
	}
	return render(request, 'Master_data/data_prakerin/chek_data.html', context)			

@login_required(login_url=settings.LOGIN_URL)
def Hapus_prakerin(request, hapus_pr):
	Model_prakerin1.objects.filter(id=hapus_pr).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Prakerin')		

@login_required(login_url=settings.LOGIN_URL)
def Edit_prakerin(request, id_prakerin):		
	data_dudi = Model_dudi.objects.all()
	select_wali = Model_walikelas.objects.all()
	panggil_s = Model_prakerin1.objects.get(id=id_prakerin)
	panggil = Model_prakerin1.objects.get(id=id_prakerin)
	if request.method == 'POST':		
			panggil.id_prakerin = request.POST.get('id_prakerin')
			panggil.nis = request.POST.get('nis')			
			panggil.nama_dudi = request.POST.get('nama_dudi')
			panggil.alamat = request.POST.get('alamat')
			panggil.nama_siswa = request.POST.get('nama_siswa')
			panggil.pembina = request.POST.get('pembina')
			panggil.kelompok = request.POST.get('kelompok')
			panggil.jumlah_kelompok = request.POST.get('jumlah_kelompok')
			panggil.tgl_prakerin = request.POST.get('tgl_prakerin')
			panggil.keterangan = request.POST.get('keterangan')
			panggil.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Prakerin')

	context = {
	'panggil': panggil,
	'panggil_s': panggil_s,
	'data_dudi': data_dudi,
	'select_wali': select_wali,
	}
	return render(request, 'Master_data/data_prakerin/edit.html',  context)	

	# data perjalanan
@login_required(login_url=settings.LOGIN_URL)
def Data_perjalanan(request):
	data_perjalanan = Model_perjalanan.objects.all()
	context = {	
	'data_perjalanan': data_perjalanan,
	}
	return render(request, 'Master_data/data_perjalanan/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Proses_perjalanan(request, id):
	proses = Model_prakerin1.objects.get(id=id) 
	# proses_sis = Model_siswa1.objects.get(nis=nis)
	if request.method == 'POST':
		Model_perjalanan.objects.create(
			id_perjalanan = request.POST['id_perjalanan'],
			id_prakerin = request.POST['id_prakerin'],
			nis = request.POST['nis'],		
			nama_kelompok = request.POST['nama_kelompok'],
			nama_siswa = request.POST['nama_siswa'],
			nama_dudi = request.POST['nama_dudi'],
			tgl_perjalanan = request.POST['tgl_perjalanan'],
			jam = request.POST['jam'],
			tahun = request.POST['tahun'],
			keterangan = request.POST['keterangan'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Perjalanan/")		
	context = {	
	'Proses_perjalanan':'Proses_perjalanan',
	'proses': proses,
	# 'proses_sis': proses_sis,
	}
	return render(request, 'Master_data/data_perjalanan/proses.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_perjalanan(request):
	if 'cari_kelompok' in request.GET:
		cari_data=request.GET['cari_kelompok']
		data_prakerin = Model_prakerin1.objects.filter(kelompok=cari_data)
	else:
		data_prakerin = Model_prakerin1.objects.filter(kelompok=None)				
		# post
	context = {	
	'Tambah': 'Tambah',
	'data_prakerin': data_prakerin,
	# 'cari_data': cari_data,
	}
	return render(request, 'Master_data/data_perjalanan/tambah.html', context)		

@login_required(login_url=settings.LOGIN_URL)
def Hapus_perjalanan(request, hapus_per):
	Model_perjalanan.objects.filter(id=hapus_per).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Perjalanan')	

@login_required(login_url=settings.LOGIN_URL)
def Edit_perjalanan(request, id_per):		
	edit_per = Model_perjalanan.objects.get(id=id_per)
	# proses_sis = Model_siswa1.objects.get(id=id_per)
	if request.method == 'POST':		
			edit_per.id_perjalanan = request.POST.get('id_perjalanan')
			edit_per.id_prakerin = request.POST.get('id_prakerin')
			edit_per.nis = request.POST.get('nis')
			edit_per.nama_kelompok = request.POST.get('nama_kelompok')
			edit_per.nama_siswa = request.POST.get('nama_siswa')
			edit_per.nama_dudi = request.POST.get('nama_dudi')
			edit_per.tgl_perjalanan = request.POST.get('tgl_perjalanan')
			edit_per.jam = request.POST.get('jam')
			edit_per.tahun = request.POST.get('tahun')
			edit_per.keterangan = request.POST.get('keterangan')
			edit_per.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('Perjalanan')

	context = {
	'edit_per': edit_per,
	# 'proses_sis':proses_sis,
	}
	return render(request, 'Master_data/data_perjalanan/edit.html',  context)	

	# data petugas
@login_required(login_url=settings.LOGIN_URL)
def PetugasV(request):
	data_petugas = User.objects.all()
	context = {	
	'data_petugas': data_petugas,
	}
	return render(request, 'Master_data/data_petugas/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def T_PetugasV(request):
	form_user = Form_user()	
	if request.method == 'POST':
		form_user = Form_user(request.POST,  request.FILES)
		if form_user.is_valid():
			form_user.save()
			messages.info(request, 'Data Berhasil Di Simpan..')
			return HttpResponseRedirect("/petugas/")	
	context = {	
	'Tambah':'tambah',
	'form_user': form_user,
	}
	return render(request, 'Master_data/data_petugas/input.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def HapuspetugasV(request, hapuspt_id):
	User.objects.filter(id=hapuspt_id).delete()
	return redirect('petugas')		

@login_required(login_url=settings.LOGIN_URL)
def EditPetugasV(request, id_pt):		
	data = User.objects.get(id=id_pt)			
	if request.method == 'POST':		
			data.username = request.POST.get('username')
			data.password = request.POST.get('password')
			data.email = request.POST.get('email')			
			
			data.save()		
			return redirect('petugas')

	context = {'data': data}
	return render(request, 'Master_data/data_petugas/edit.html',  context)	

	# menu laporan
@login_required(login_url=settings.LOGIN_URL)
def Menu(request):	
	context = {	
	'menu': 'menu',
	}
	return render(request, 'Master_data/menu_laporan/menu.html',  context)	
	# lp prakerin
@login_required(login_url=settings.LOGIN_URL)
def Lp_prakerin(request):	
	lp = Model_prakerin1.objects.all()
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_prakerin.html',  context)		

@login_required(login_url=settings.LOGIN_URL)
def Lp_prakerin_kl(request):	
	if 'cetak' in request.GET:
		cari_data=request.GET['cetak']
		lp = Model_prakerin1.objects.filter(kelompok=cari_data)
	else:
		lp = Model_prakerin1.objects.filter(kelompok=None)				
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_prakerin_kl.html',  context)			

	# lp perjalanan
@login_required(login_url=settings.LOGIN_URL)
def Lp_perjalanan(request):	
	lp = Model_perjalanan.objects.all()
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_perjalanan.html',  context)			

@login_required(login_url=settings.LOGIN_URL)
def Lp_perjalanan_kl(request):	
	if 'cetak' in request.GET:
		cari_data=request.GET['cetak']
		lp = Model_perjalanan.objects.filter(nama_kelompok=cari_data)
	else:
		lp = Model_perjalanan.objects.filter(nama_kelompok=None)				
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_perjalanan_kl.html',  context)				

	# lp siswa
@login_required(login_url=settings.LOGIN_URL)
def Lp_siswa(request):	
	lp = Model_siswa1.objects.all()
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_siswa.html',  context)				

	# lp dudi
@login_required(login_url=settings.LOGIN_URL)
def Lp_dudi(request):	
	lp = Model_dudi.objects.all()
	context = {	
	'menu': 'menu',
	'lp':lp,
	}
	return render(request, 'Master_data/menu_laporan/lp_dudi.html',  context)					

	# halaman website
def WEBSITE(request):	
	data = Model_pengumuman.objects.all()
	context = {	
	'menu': 'menu',
	'data':data,
	}
	return render(request, 'Website/website.html',  context)						

	# login prakerin
def Login_prakerin(request):	
	if 'cari_nis' in request.GET:
		cari_data=request.GET['cari_nis']
		data = Model_perjalanan.objects.filter(nis=cari_data)
	else:
		data = Model_perjalanan.objects.filter(nis=None)

	if 'cari_nis' in request.GET:
		cari_data=request.GET['cari_nis']
		data1 = Model_siswa1.objects.filter(nis=cari_data)
	else:
		data1 = Model_siswa1.objects.filter(nis=None)

	for tampil in data1:
		nama_siswa = tampil.nama
		nis = tampil.nis
		foto=tampil.foto

	# cari prakerin
	if 'cari_nis' in request.GET:
		cari_data_pr=request.GET['cari_nis']
		data_pr = Model_prakerin1.objects.filter(nis=cari_data_pr)		
	else:
		data_pr = Model_prakerin1.objects.filter(nis=None)	

	# catatan
	if 'cari_nis' in request.GET:
		cari_data_pr=request.GET['cari_nis']
		data_catatan_s = Model_catatan.objects.filter(nis=cari_data_pr)		
	else:
		data_catatan_s = Model_catatan.objects.filter(nis=None)	

	for tampil_pr in data_pr:
		kelompok = tampil_pr.kelompok
		
	# cari berdasarkan kelompok
	data_kl = Model_prakerin1.objects.all()

	# simpan
	if request.method == 'POST':
		Model_catatan.objects.create(
			id_catatan = request.POST['id_catatan'],
			nis = request.POST['nis'],
			nama_siswa = request.POST['nama_siswa'],			
			kelompok = request.POST['kelompok'],			
			title_tugas = request.POST['title_tugas'],			
			keterangan = request.POST['keterangan'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan.., Selalu Semangat...?')	

	context = {	
	'menu': 'menu',
	'data':data,
	'nama_siswa': nama_siswa,
	'nis': nis,
	'kelompok': kelompok,
	'data_kl': data_kl,
	'foto': foto,
	'data_catatan_s': data_catatan_s
	}
	return render(request, 'Website/Master/data_prakerin/data.html',  context)					

def Logout_prakerin(request):	
	context = {	
	'Logout_prakerin': 'Logout_prakerin',
	}
	return render(request, 'Website/logout.html',  context)						

	# chek prakerin
def Chek_prakerin(request):	
	data = Model_prakerin1.objects.all()
	context = {	
	'menu': 'menu',
	'data':data,
	}
	return render(request, 'Website/Master/data_prakerin/chek_data.html',  context)					


# husus pembina
def Data_pengumuman_pembina(request):
	data_pengumuman = Model_pengumuman.objects.all()
	context = {	
	'data_pengumuman': data_pengumuman,
	}
	return render(request, 'Master_pembina/data_pengumuman/tabel.html',  context)			

def Data_perjalanan_pembina(request):
	data_perjalanan = Model_perjalanan.objects.all()
	context = {	
	'data_perjalanan': data_perjalanan,
	}
	return render(request, 'Master_pembina/data_perjalanan/tabel.html',  context)

def Data_prakerin_pembina(request):
	data_prakerin = Model_prakerin1.objects.all()
	context = {	
	'data_prakerin': data_prakerin,
	}
	return render(request, 'Master_pembina/data_prakerin/tabel.html',  context)	

#komentar pembina
@login_required(login_url=settings.LOGIN_URL)
def Proses_komentar(request):		
	data_komentar = Model_komentar.objects.all()
	if request.method == 'POST':
		Model_komentar.objects.create(
			nis = request.POST['nis'],
			nama = request.POST['nama'],
			komentar = request.POST['komentar'],		
			kelompok = request.POST['kelompok'],
			)
		messages.info(request, 'Data Berhasil..')
		return HttpResponseRedirect("/Proses_komentar/")

	context = {'data_komentar': data_komentar}
	return render(request, 'Master_pembina/data_komentar/proses_komentar.html',  context)	 

# hapus
def Hapus_komentar(request, hapus_komen):
	Model_komentar.objects.filter(id=hapus_komen).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('Proses_komentar')

# kegiatan
def Tambah_kegiatan(request):
	if request.method == 'POST':
		Model_kegiatan.objects.create(
			kelompok = request.POST['kelompok'],
			nama_kegiatan = request.POST['nama_kegiatan'],
			deskripsi = request.POST['deskripsi'],			
			foto = request.FILES['foto'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/Check_kegiatan/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Website/Master/data_prakerin/input_kegiatan.html',  context)					

# check kegiatan
def Check_kegiatan(request):
	data = Model_kegiatan.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Website/Master/data_prakerin/kegiatan.html',  context)					
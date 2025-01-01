
from metaflow import FlowSpec, step

class KuliahInformatikaFlow(FlowSpec):

    @step
    def start(self):
        print("Memulai proses kuliah informatika.")
        self.next(self.bayar_spp)
    
    @step
    def bayar_spp(self):
        print("Langkah 1: Bayar SPP.")
        # Proses pembayaran SPP
        self.status_pembayaran = "Lunas"
        print(f"Status Pembayaran: {self.status_pembayaran}")
        self.next(self.pilih_matakuliah)

    @step
    def pilih_matakuliah(self):
        print("Langkah 2: Pilih mata kuliah.")
        # Proses pemilihan mata kuliah
        self.matakuliah = ["Algoritma", "Struktur Data", "Basis Data", "Pemrograman Lanjut"]
        print(f"Mata Kuliah yang diambil: {', '.join(self.matakuliah)}")
        self.next(self.mengikuti_perkuliahan)
    
    @step
    def mengikuti_perkuliahan(self):
        print("Langkah 3: Mengikuti perkuliahan.")
        # Simulasi mengikuti perkuliahan
        self.kehadiran = {mk: "Hadir" for mk in self.matakuliah}
        print(f"Kehadiran perkuliahan: {self.kehadiran}")
        self.next(self.mengerjakan_tugas)

    @step
    def mengerjakan_tugas(self):
        print("Langkah 4: Mengerjakan tugas.")
        # Simulasi pengerjaan tugas
        self.nilai_tugas = {mk: 80 + (i * 5) for i, mk in enumerate(self.matakuliah)}  # Skor acak untuk setiap tugas
        print(f"Nilai tugas: {self.nilai_tugas}")
        self.next(self.ujian_akhir)

    @step
    def ujian_akhir(self):
        print("Langkah 5: Mengikuti ujian akhir.")
        # Simulasi mengikuti ujian akhir
        self.nilai_ujian = {mk: 70 + (i * 10) for i, mk in enumerate(self.matakuliah)}  # Skor acak untuk ujian
        print(f"Nilai ujian: {self.nilai_ujian}")
        self.next(self.hitung_nilai_akhir)

    @step
    def hitung_nilai_akhir(self):
        print("Langkah 6: Menghitung nilai akhir.")
        # Hitung nilai akhir berdasarkan nilai tugas dan ujian
        self.nilai_akhir = {
            mk: (self.nilai_tugas[mk] * 0.4) + (self.nilai_ujian[mk] * 0.6)
            for mk in self.matakuliah
        }
        print(f"Nilai akhir: {self.nilai_akhir}")
        self.next(self.selesai)

    @step
    def selesai(self):
        print("Proses kuliah informatika selesai.")
        print("Rekap nilai akhir:")
        for mk, nilai in self.nilai_akhir.items():
            print(f"{mk}: {nilai}")
        print("Selamat! Anda telah menyelesaikan semua tahapan kuliah.")

if _name_ == '_main_':
    KuliahInformatikaFlow()
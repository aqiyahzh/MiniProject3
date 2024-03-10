class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak kami temukan")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        if prev_node == self.tail:
            self.tail = new_node

    def delete_first(self):
        if self.head is None:
            print("Linked list masih kosong/tidak ada")
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def delete_last(self):
        if self.head is None:
            print("Linked list masih kosong/tidak ada")
            return

        prev_node = self.head
        while prev_node.next != self.tail:
            prev_node = prev_node.next

        prev_node.next = None
        self.tail = prev_node

        if self.tail is None:
            self.head = None

    def delete_after(self, prev_node):
        if not prev_node:
            print("Node sebelumnya tidak kami temukan")
            return

        if prev_node.next is None:
            print("Node setelah node sebelumnya tidak kami temukan")
            return

        next_node = prev_node.next
        prev_node.next = next_node.next

        if next_node == self.tail:
            self.tail = prev_node

    def print_list(self):
        if self.head is None:
            print("Linked list masih kosong nih :(")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()
    
    def to_list(self):
        # Mengubah linked list menjadi list
        data_list = []
        temp = self.head
        while temp is not None:
            data_list.append(temp.data)
            temp = temp.next
        return data_list

def merge(left, right, key, ascending):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if ascending:
            if left[i][key] < right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i][key] > right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(data, key, ascending):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid], key, ascending)
    right = merge_sort(data[mid:], key, ascending)

    return merge(left, right, key, ascending)

def tampil_sort():
    while True:
        print("\nFitur Sorting")
        print("[1] Sort berdasarkan ID (Ascending)")
        print("[2] Sort berdasarkan ID (Descending)")
        print("[3] Sort berdasarkan Nama Produk (Ascending)")
        print("[4] Sort berdasarkan Nama Produk (Descending)")
        print("[5] Kembali ke menu utama")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            toko.tampil(merge_sort(toko.barang.to_list(), 'ID', True))
        elif pilihan == 2:
            toko.tampil(merge_sort(toko.barang.to_list(), 'ID', False))
        elif pilihan == 3:
            toko.tampil(merge_sort(toko.barang.to_list(), 'Nama Produk', True))
        elif pilihan == 4:
            toko.tampil(merge_sort(toko.barang.to_list(), 'Nama Produk', False))
        elif pilihan == 5:
            break
        else:
            print("Pilihan anda tidak jelas bro!")

class TokoATK:
    def __init__(self):
        self.barang = LinkedList()

    def tambah(self, produk):
        self.barang.add_last(produk)
        print(f"Produk '{produk['Nama Produk']}' sudah ditambahkan nihh")

    def tampil(self, sorted_data=None):
        if sorted_data is None:
            if self.barang.head is None:
                print("Belum ada produk yang ditambahkan.")
            else:
                print("Daftar produk yang tersedia:")
                idx = 1
                temp = self.barang.head
                while temp is not None:
                    print(f"{idx}. {temp.data['Nama Produk']} | Harga: {temp.data['Harga']} | Stok: {temp.data['Stok']} | ID: {temp.data['ID']}")
                    idx += 1
                    temp = temp.next
        else:
            if not sorted_data:
                print("Tidak ada untuk ditampilkan")
                return
            print("Daftar Produk yang tersedia (Sudah diurutkan):")
            idx = 1
            for item in sorted_data:
                print(f"{idx}. {item['Nama Produk']} | Harga: {item['Harga']} | Stok: {item['Stok']} | ID: {item['ID']}")

    def perbaharui(self, index, updated):
        idx = 1
        temp = self.barang.head
        while temp is not None:
            if idx == index:
                temp.data = updated
                print(f"Produk '{updated['Nama Produk']}' sudah diperbaharui.")
                return
            idx += 1
            temp = temp.next

        print("Index produk yang anda masukkan salah.")

    def hapus(self, index):
        idx = 1
        prev = None
        temp = self.barang.head
        while temp is not None:
            if idx == index:
                if prev is None:
                    self.barang.delete_first()
            else:
                prev.next = temp.next
                if temp == self.tail:
                    self.tail = prev
            print(f"Produk dengan ID '{temp.data['ID']}' sudah dihapus.")
            return
        idx += 1
        prev = temp
        temp = temp.next

        print("Index produk yang anda masukkan salah :(")

    def tampil_sorted(self, sorted_data):
            if not sorted_data:
                print("Tidak ada data untuk ditampilkan.")
                return
            print("Daftar produk yang tersedia (sudah diurutkan):")
            idx = 1
            for item in sorted_data:
                print(f"ID: {item['ID']} | {item['Nama Produk']} | Harga: {item['Harga']} | Stok: {item['Stok']}")
                idx += 1

def menu():
    print('''
        Program Pendataan Barang Toko Alat Tulis 
        by: Aqiyah Zulqiyah (2309116075)
        ''')
    print('[1] Tampil Data')
    print('[2] Tambah Data')
    print('[3] Edit Data')
    print('[4] Hapus Data')
    print('[5] Keluar')
    print('')

toko = TokoATK()

# Menambahkan opsi sorting ke menu utama
while True:
    menu()
    kode = input('Masukkan Pilihan Anda: ')

    if kode == '1':
        toko.tampil()
        konfir = input("Apakah anda ingin melakukan pengurutan? y/n: ")
        if konfir == 'y':
            tampil_sort()
        else:
            print("Anda tidak ingin melakukan pengurutan")
            menu()

    elif kode == '2':
        id_barang = input("Masukkan ID produk: ")
        nama_barang = input("Masukkan nama produk: ")
        harga_barang = input("Masukkan harga produk: Rp. ")
        stok_barang = int(input("Masukkan stok produk: "))

        barang_baru = {'ID': id_barang, 'Nama Produk': nama_barang, 'Harga': harga_barang, 'Stok': stok_barang}
        toko.tambah(barang_baru)

    elif kode == '3':
        toko.tampil()
        index = int(input("Masukkan index produk yang ingin diedit: "))
        nama_baru = input("Masukkan nama produk yang baru: ")
        harga_baru = float(input("Masukkan harga produk yang baru: Rp. "))
        stok_baru = int(input("Masukkan stok produk yang terbaru: "))
        id_baru = input("Masukkan ID Produk yang baru: ")
        barang_baru = {'Nama Produk': nama_baru, 'Harga': harga_baru, 'Stok': stok_baru, 'ID': id_baru}
        toko.perbaharui(index, barang_baru)

    elif kode == '4':
        toko.tampil()
        try:
            index = int(input("Masukkan index produk yang ingin dihapus: "))
        except ValueError:
            print("Index yang Anda masukkan bukan angka.")

        toko.hapus(index)

    elif kode == '5':
        print("Terima kasih! Anda telah keluar dari program.")
        break

    elif kode == '6':
        tampil_sort()

    else:
        print('Kode yang anda masukkan tidak jelas. Tolong masukkan angka 1-6 saja jangan aneh-aneh :)')
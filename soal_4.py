berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = berat_badan / (tinggi_badan)
print(f"Indeks Massa Tubuh (BMI) Anda adalah: {bmi:.2f}")

if bmi < 18.5:
    print("Kategori: Berat badan kurang")
    
elif 18.5 <= bmi < 24.9:
    print("Kategori: Berat badan normal")
    
elif 25 <= bmi < 29.9:
    print("Kategori: Kelebihan berat badan")
    
else:
    print("Kategori: Obesitas")
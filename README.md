# Blog-loyihasi
Oddiy django loyihasi

Ushbu loyihani kompyuteringizda qanday ishga tushirish bo'yicha bosqichma-bosqich buyruqlar

1)- Muhit yuklab oling Virtualenv

```
pip install virtualenv
```

2)- Virtualenv yarating

```
virtualenv venv
```

3)- Virtual muhitni faollashtirish

```
venv/Scripts/activate
```

4)- O'rnatish talablari agar kutubxonalar to'liq bo'lsa shart emas!

```
pip install -r requirements.txt
```
Eslatma: Birinchi marta o'rnatish uchun yuqoridagi buyruq talab qilinadi!

5)- Quyidagi buyruqlarni bajaring bu shart database uchun

```
python manage.py makemigrations
```
```
python manage.py migrate
```
Eslatma: Agar database ni debug da ishga tushursangiz bu majburiy!

6)- Administratorga kirish uchun createsuperuser yarating va agar yaratilmagan bo'lsa, ko'rsatmalarga rioya qiling:

Username: Xusanbek
Parol: 0071

```
python manage.py createsuperuser
```

7)- Statik fayllarni bitta joyda to'plang. Bu shart aks holda sayt css fayllarni o'qimaydi
```
python manage.py collectstatic
```
<br>

## Ishga tushurish

```
python manage.py runserver
```
Loyiha ishga tayyor uni ishga tushurish mumkin!
Eslatma: Agar qadamlar to'g'ri bajarilsa loyiha ishga tushadi!

<br>


## Loyihadan lavhalar

# https://creators-blog.onrender.com
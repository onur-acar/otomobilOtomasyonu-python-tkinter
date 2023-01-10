import tkinter as tk
import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='',
    host="localhost",
    port ="3306"   
)

mycursor = cnx.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS h")

mycursor.execute("USE h")

root = tk.Tk()
root.geometry("500x500")

def musteri_bilgi_fonk():
    musteri_bilgi = tk.Toplevel()
    musteri_bilgi.geometry("500x500")

    cnx = mysql.connector.connect(
    user='root',
    password='',
    host="localhost", 
    database ="h",
    port ="3306"
)
    mycursor = cnx.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS musteri_bilgileri (ad VARCHAR(255), soyad VARCHAR(255), TC_No VARCHAR(255),dogum_tarihi VARCHAR(255),adres_bilgileri VARCHAR(255),telefon_numarasi VARCHAR(255),meslek VARCHAR(255),ehliyet VARCHAR(255),medeni_hali VARCHAR(255),egitim_durumu VARCHAR(255))")

    musteriadilabel = tk.Label(musteri_bilgi,text="Ad")
    musteriadilabel.grid(row=0,column=0,padx=20)
    musteriadentry = tk.Entry(musteri_bilgi)
    musteriadentry.grid(row=1,column=0,padx=20)

    musterisoyadlabel = tk.Label(musteri_bilgi,text="Soyad")
    musterisoyadlabel.grid(row=2,column=0,padx=20)
    musterisoyadentry = tk.Entry(musteri_bilgi)
    musterisoyadentry.grid(row=3,column=0,padx=20)

    musteritcnolabel = tk.Label(musteri_bilgi,text="TC No")
    musteritcnolabel.grid(row=4,column=0,padx=20)
    musteritcnoentry = tk.Entry(musteri_bilgi)
    musteritcnoentry.grid(row=5,column=0,padx=20)

    musteridogumtarihilabel = tk.Label(musteri_bilgi,text="Doğum Tarihi")
    musteridogumtarihilabel.grid(row=6,column=0,padx=20)
    musteridogumtarihientry = tk.Entry(musteri_bilgi)
    musteridogumtarihientry.grid(row=7,column=0,padx=20)

    musteriadresbilgilerilabel = tk.Label(musteri_bilgi,text="Adres Bilgileri")
    musteriadresbilgilerilabel.grid(row=8,column=0,padx=20)
    musteriadresbilgilerientry = tk.Entry(musteri_bilgi)
    musteriadresbilgilerientry.grid(row=9,column=0,padx=20)

    musteritelefonnolabel = tk.Label(musteri_bilgi,text="Telefon Numarası")
    musteritelefonnolabel.grid(row=10,column=0,padx=20)
    musteritelefonnoentry = tk.Entry(musteri_bilgi)
    musteritelefonnoentry.grid(row=11,column=0,padx=20)

    musterimesleklabel = tk.Label(musteri_bilgi,text="Meslek")
    musterimesleklabel.grid(row=12,column=0,padx=20)
    musterimeslekentry = tk.Entry(musteri_bilgi)
    musterimeslekentry.grid(row=13,column=0,padx=20)

    musteriehliyetlabel = tk.Label(musteri_bilgi,text="Ehliyet")
    musteriehliyetlabel.grid(row=14,column=0,padx=20)
    musteriehliyetentry = tk.Entry(musteri_bilgi)
    musteriehliyetentry.grid(row=15,column=0,padx=20)

    musterimedenihalilabel = tk.Label(musteri_bilgi,text="Medeni Hali")
    musterimedenihalilabel.grid(row=16,column=0,padx=20)
    musterimedenihalientry = tk.Entry(musteri_bilgi)
    musterimedenihalientry.grid(row=17,column=0,padx=20)

    musteriegitimdurumulabel = tk.Label(musteri_bilgi,text="Eğitim Durumu")
    musteriegitimdurumulabel.grid(row=18,column=0,padx=20)
    musteriegitimdurumuentry = tk.Entry(musteri_bilgi,)
    musteriegitimdurumuentry.grid(row=19,column=0,padx=20)

    def müşteriekle():
        cnx = mysql.connector.connect(
        user='root',
        password='',
        host="localhost",
        database = "h",
        port ="3306"    
        )
        musteriadi = musteriadentry.get()
        musterisoyadi = musterisoyadentry.get()
        musteritcno = musteritcnoentry.get()
        musteridogumtarihi = musteridogumtarihientry.get()
        musteriadresbilgileri = musteriadresbilgilerientry.get()
        musteritelefonno = musteritelefonnoentry.get()
        musterimeslek = musterimeslekentry.get()
        musteriehliyet = musteriehliyetentry.get()
        musterimedenihali = musterimedenihalientry.get()
        musteriegitimdurumu = musteriegitimdurumuentry.get()
        mycursor = cnx.cursor()

        mycursor.execute("INSERT INTO h.musteri_bilgileri (ad , soyad , TC_No ,dogum_tarihi ,adres_bilgileri ,telefon_numarasi ,meslek,ehliyet ,medeni_hali ,egitim_durumu ) values ('{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}','{j}','{k}')".format(a=musteriadi,b=musterisoyadi,c=musteritcno,d=musteridogumtarihi,e=musteriadresbilgileri,f=musteritelefonno,g=musterimeslek,h=musteriehliyet,j=musterimedenihali,k=musteriegitimdurumu))
        cnx.commit()

        



    musteri_kaydet = tk.Button(musteri_bilgi,text="Müşteri Kaydet",command=müşteriekle)
    musteri_kaydet.place(x=280,y=180)

    
btn1 = tk.Button(root,text="Müşteri Bilgileri",command=musteri_bilgi_fonk).place(x=100,y=100)

def arac_bilgi_fonk():
    arac_bilgi = tk.Toplevel()
    arac_bilgi.geometry("500x800")

    cnx = mysql.connector.connect(
        user='root',
        password='',
        host="localhost",
        database = "h",
        port ="3306"    
        )
    tablosorgu=cnx.cursor()



    tablosorgu.execute("CREATE TABLE IF NOT EXISTS arac_bilgileri (arac_turu VARCHAR(255), marka VARCHAR(255), model VARCHAR(255), uretim_yili VARCHAR(255), yakit_turu VARCHAR(255), vites VARCHAR(255), motor_gucu VARCHAR(255), kasa_tipi VARCHAR(255), motor_hacmi VARCHAR(255), cekis VARCHAR(255), kapi VARCHAR(255), renk VARCHAR(255), motor_no VARCHAR(255), sasi_no VARCHAR(255), gunluk_kiralama_bedeli VARCHAR(255), kirada_mi VARCHAR(255), kullanim_disi_mi VARCHAR(255))")

    aracturulabel = tk.Label(arac_bilgi,text="Araç Türü")
    aracturulabel.grid(row=0,column=0,padx=20)
    aracturuentry = tk.Entry(arac_bilgi)
    aracturuentry.grid(row=1,column=0,padx=20)

    aracmarkalabel = tk.Label(arac_bilgi,text="Marka")
    aracmarkalabel.grid(row=2,column=0,padx=20)
    aracmarkaentry = tk.Entry(arac_bilgi)
    aracmarkaentry.grid(row=3,column=0,padx=20)

    aracmodellabel = tk.Label(arac_bilgi,text="Model")
    aracmodellabel.grid(row=4,column=0,padx=20)
    aracmodelentry = tk.Entry(arac_bilgi)
    aracmodelentry.grid(row=5,column=0,padx=20)

    aracuretimyililabel = tk.Label(arac_bilgi,text="Üretim Yılı")
    aracuretimyililabel.grid(row=6,column=0,padx=20)
    aracuretimyilientry = tk.Entry(arac_bilgi)
    aracuretimyilientry.grid(row=7,column=0,padx=20)

    aracyakitturulabel = tk.Label(arac_bilgi,text="Yakıt Türü")
    aracyakitturulabel.grid(row=8,column=0,padx=20)
    aracyakitturuentry = tk.Entry(arac_bilgi)
    aracyakitturuentry.grid(row=9,column=0,padx=20)

    aracviteslabel = tk.Label(arac_bilgi,text="Vites")
    aracviteslabel.grid(row=10,column=0,padx=20)
    aracvitesentry = tk.Entry(arac_bilgi)
    aracvitesentry.grid(row=11,column=0,padx=20)

    aracmotorguculabel = tk.Label(arac_bilgi,text="Motor Gücü")
    aracmotorguculabel.grid(row=12,column=0,padx=20)
    aracmotorgucuentry = tk.Entry(arac_bilgi)
    aracmotorgucuentry.grid(row=13,column=0,padx=20)

    arackasatipilabel = tk.Label(arac_bilgi,text="Kasa Tipi")
    arackasatipilabel.grid(row=14,column=0,padx=20)
    arackasatipientry = tk.Entry(arac_bilgi)
    arackasatipientry.grid(row=15,column=0,padx=20)

    aracmotorhacmilabel = tk.Label(arac_bilgi,text="Motor Hacmi")
    aracmotorhacmilabel.grid(row=16,column=0,padx=20)
    aracmotorhacmientry = tk.Entry(arac_bilgi)
    aracmotorhacmientry.grid(row=17,column=0,padx=20)

    araccekislabel = tk.Label(arac_bilgi,text="Çekiş")
    araccekislabel.grid(row=18,column=0,padx=20)
    araccekisentry = tk.Entry(arac_bilgi)
    araccekisentry.grid(row=19,column=0,padx=20)

    arackapilabel = tk.Label(arac_bilgi,text="Kapı")
    arackapilabel.grid(row=20,column=0,padx=20)
    arackapientry = tk.Entry(arac_bilgi)
    arackapientry.grid(row=21,column=0,padx=20)

    aracrenklabel = tk.Label(arac_bilgi,text="Renk")
    aracrenklabel.grid(row=22,column=0,padx=20)
    aracrenkentry = tk.Entry(arac_bilgi)
    aracrenkentry.grid(row=23,column=0,padx=20)

    aracmotornolabel = tk.Label(arac_bilgi,text="Motor No")
    aracmotornolabel.grid(row=24,column=0,padx=20)
    aracmotornoentry = tk.Entry(arac_bilgi)
    aracmotornoentry.grid(row=25,column=0,padx=20)

    aracsasinolabel = tk.Label(arac_bilgi,text="Şaşi No")
    aracsasinolabel.grid(row=26,column=0,padx=20)
    aracsasinoentry = tk.Entry(arac_bilgi)
    aracsasinoentry.grid(row=27,column=0,padx=20)

    aracgunlukkiralamabedelilabel = tk.Label(arac_bilgi,text="Günlük Kiaralama Bedeli")
    aracgunlukkiralamabedelilabel.grid(row=28,column=0,padx=20)
    aracgunlukkiralamabedelientry = tk.Entry(arac_bilgi)
    aracgunlukkiralamabedelientry.grid(row=29,column=0,padx=20)

    arackiradamilabel = tk.Label(arac_bilgi,text="Kirada mı?")
    arackiradamilabel.grid(row=30,column=0,padx=20)
    arackiradamientry = tk.Entry(arac_bilgi)
    arackiradamientry.grid(row=31,column=0,padx=20)

    arackullanimdisimilabel = tk.Label(arac_bilgi,text="Kullanım Dışı mı?")
    arackullanimdisimilabel.grid(row=32,column=0,padx=20)
    arackullanimdisimientry = tk.Entry(arac_bilgi)
    arackullanimdisimientry.grid(row=33,column=0,padx=20)

    def aracekle():
        cnx = mysql.connector.connect(
        user='root',
        password='',
        host="localhost",
        database = "h",
        port ="3306"    
        )
        aracturu = aracturuentry.get()
        aracmarka = aracmarkaentry.get()
        aracmodel = aracmodelentry.get()
        aracuretimyili = aracuretimyilientry.get()
        aracyakitturu = aracyakitturuentry.get()
        aracvites = aracvitesentry.get()
        aracmotorgucu = aracmotorgucuentry.get()
        arackasatipi = arackasatipientry.get()
        aracmotorhacmi = aracmotorhacmientry.get()
        araccekis = araccekisentry.get()
        arackapi = arackapientry.get()
        aracrenk = aracrenkentry.get()
        aracmotorno = aracmotornoentry.get()
        aracsasino = aracsasinoentry.get()
        aracgunlukkiralamabedeli = aracgunlukkiralamabedelientry.get()
        arackiradami = arackiradamientry.get()
        arackullanimdisimi = arackullanimdisimientry.get()

        aracsorgu = cnx.cursor()
        aracsorgu.execute("INSERT INTO h.arac_bilgileri (arac_turu , marka , model , uretim_yili , yakit_turu , vites , motor_gucu , kasa_tipi , motor_hacmi , cekis , kapi , renk , motor_no , sasi_no , gunluk_kiralama_bedeli , kirada_mi , kullanim_disi_mi ) values ('{aracturu}','{aracmarka}','{aracmodel}','{aracuretimyili}','{aracyakitturu}','{aracvites}','{aracmotorgucu}','{arackasatipi}','{aracmotorhacmi}','{araccekis}','{arackapi}','{aracrenk}','{aracmotorno}','{aracsasino}','{aracgunlukkiralamabedeli}','{arackiradami}','{arackullanimdisimi}')".format(aracturu=aracturu,aracmarka=aracmarka,aracmodel=aracmodel,aracuretimyili=aracuretimyili,aracyakitturu=aracyakitturu,aracvites=aracvites,aracmotorgucu=aracmotorgucu,arackasatipi=arackasatipi,aracmotorhacmi=aracmotorhacmi,araccekis=araccekis,arackapi=arackapi,aracrenk=aracrenk,aracmotorno=aracmotorno,aracsasino=aracsasino,aracgunlukkiralamabedeli=aracgunlukkiralamabedeli,arackiradami=arackiradami,arackullanimdisimi=arackullanimdisimi))
        cnx.commit()


    musteri_kaydet = tk.Button(arac_bilgi,text="Araç Kaydet",command=aracekle)
    musteri_kaydet.grid(row=35,column=0,padx=20)


btn2 = tk.Button(root,text="Araç Bilgileri",command=arac_bilgi_fonk).place(x=200,y=100)

def kiralama_bilgi_fonk():
    cnx = mysql.connector.connect(
        user='root',
        password='',
        host="localhost",
        database = "h",
        port ="3306"    
        )
    cursor = cnx.cursor()

    cursor.execute("CREATE TABLE kiralanmisaraclar (ad VARCHAR(255),marka VARCHAR(255),yolculuk varchar(255),kacgun varchar(255));")

    kiralama_bilgi = tk.Toplevel()
    kiralama_bilgi.geometry("500x500")

    kacgunkiralanacaklabel = tk.Label(kiralama_bilgi,text="Kaç gün kiralanacak?")
    kacgunkiralanacaklabel.grid(row=1,column=0,padx=20)
    kacgunkiralanacakentry = tk.Entry(kiralama_bilgi)
    kacgunkiralanacakentry.grid(row=2,column=0,padx=20)

    yolculuknereyeolacaklabel = tk.Label(kiralama_bilgi,text="Yolculuk nereye olacak?")
    yolculuknereyeolacaklabel.grid(row=3,column=0,padx=20)
    yolculuknereyeolacakentry = tk.Entry(kiralama_bilgi)
    yolculuknereyeolacakentry.grid(row=4,column=0,padx=20)


    def kiraolustur():

        cnx = mysql.connector.connect(
        user='root',
        password='',
        host="localhost",
        database = "h",
        port ="3306"    
        )
    
        yolculuk = yolculuknereyeolacakentry.get()
        kacgun = kacgunkiralanacakentry.get()

        sorgu = cnx.cursor(dictionary=True)
        sorgu.execute("Select ad from h.musteri_bilgileri")
        musteriliste = sorgu.fetchall()
        def musterikaydet(musteriisim):
            cnx = mysql.connector.connect(
            user='root',
            password='',
            host="localhost",
            database = "h",
            port ="3306"    
            )
            global sonisim
            sonisim = musteriisim
        def arackirala(aracisim):
            cnx = mysql.connector.connect(
            user='root',
            password='',
            host="localhost",
            database = "h",
            port ="3306"    
            )
            sonsorgu = cnx.cursor()
            sonsorgu.execute("INSERT INTO h.kiralanmisaraclar (ad,marka,yolculuk,kacgun) Values ('{aa}','{ba}','{ca}','{da}')".format(aa=sonisim,ba=aracisim,ca=yolculuk,da=kacgun))
            sonsorgu.execute("UPDATE h.arac_bilgileri SET kirada_mi = 'kirada' where marka = '{ea}'".format(ea=aracisim))
            cnx.commit()    
        satir = 1
        for i in musteriliste:
            musteributton = tk.Button(kiralama_bilgi,text=i['ad'],command=lambda musteriisim = i['ad']:musterikaydet(musteriisim))
            musteributton.grid(row=satir,column=1,padx=5,pady=5)
            satir+=1
        aracsorgu = cnx.cursor(dictionary=True)
        aracsorgu.execute("Select marka from h.arac_bilgileri where kirada_mi != 'kirada'")
        aracliste = aracsorgu.fetchall()
        satirr = 1
        for j in aracliste:
            aracbutton = tk.Button(kiralama_bilgi,text=j['marka'],command=lambda aracisim = j['marka']:arackirala(aracisim))
            aracbutton.grid(row=satirr,column=2,padx=5,pady=5)
            satirr+=1    


    kiralanacak_arackaydet = tk.Button(kiralama_bilgi,text="Kiralanacak Araç Kaydet",command=kiraolustur)
    kiralanacak_arackaydet.grid(row=5,column=0,padx=20)


btn3 = tk.Button(root,text="Kiralama Bilgileri",command=kiralama_bilgi_fonk).place(x=100,y=150)

def kiralanan_araclar_fonk():
    kiralanan_araclar = tk.Toplevel()
    kiralanan_araclar.geometry("500x500")

    cnx = mysql.connector.connect(
    user='root',
    password='',
    host="localhost",
    database = "h",
    port ="3306"    
    )

    kiralananaraclarframe = tk.Frame(kiralanan_araclar,width=250,height=470,background="white")
    kiralananaraclarframe.grid(row=1,column=1,padx=220,pady=10)

    cek = cnx.cursor(dictionary=True)
    cek.execute("Select * from h.kiralanmisaraclar")
    sonliste = cek.fetchall()
    sonss = 0
    for m in sonliste:
        cardlabel = tk.Label(kiralananaraclarframe,text=m['ad'],font="Arial 10 bold")
        cardlabel.grid(row=sonss,column=0,padx=5,pady=5)
        cardlabel = tk.Label(kiralananaraclarframe,text=m['marka'],font="Arial 10 bold")
        cardlabel.grid(row=sonss,column=1,padx=5,pady=5)
        cardlabel = tk.Label(kiralananaraclarframe,text=m['yolculuk'],font="Arial 10 bold")
        cardlabel.grid(row=sonss,column=2,padx=5,pady=5)
        cardlabel = tk.Label(kiralananaraclarframe,text=m['kacgun'],font="Arial 10 bold")
        cardlabel.grid(row=sonss,column=3,padx=5,pady=5)
        sonss+=1
 
btn4 = tk.Button(root,text="kiralanan Araçlar",command=kiralanan_araclar_fonk).place(x=200,y=150)


root.mainloop()
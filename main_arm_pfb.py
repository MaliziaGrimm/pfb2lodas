#Example (Hello, World):
from tkinter import * #in python 3.x: tkinter wird kleingeschrieben
from tkinter import messagebox
import os, sys, time
from shutil import copyfile


def speichern_neu_AN():

### Block Pflichtfelder lesen
   v_pnr = E_pnr.get()
   v_name = E_name.get()
   v_vname = E_vname.get()
   v_geburtsdatum = E_geburtsdatum.get()
   v_eintrittsdatum = E_eintrittsdatum.get()
   v_strasse = E_strasse.get()
   v_hnummer = E_hnummer.get()
   v_plz = E_plz.get()
   v_wohnort = E_wohnort.get() 
   v_geschlecht = str(R_geschlecht.get())
### Ende der Pflichtfelder 

### länge Pflichtdatum lesen
   v_eintrittsdatumfehler = len(v_eintrittsdatum)
   v_geburtsdatumfehler = len(v_geburtsdatum)

### Pflichtfelder prüfen - wenn ok - dann weitere v_*** zuordnen und Datei schreiben
   if v_pnr == "" or v_name == "" or v_vname == "" or v_geburtsdatum == "" or v_eintrittsdatum =="" or v_strasse == "" or v_hnummer =="" or v_plz =="" or v_wohnort == "":
      messagebox.showerror("Fehler", "Es sind nicht alle Pflichtfelder gefüllt")
### Personalnummer im gültigen Bereich?
   elif v_pnr < "1" or v_pnr > "99999":
      messagebox.showerror("Personalnummer", "Die Personalnummer ist nicht im Bereich von 1 bis 99999")
# Geburtsdatum (v_geburtsdatum) und Eintrittsdatum (v_eintrittsdatum) auf Eingabe und korrekte Länge prüfen - Fehler erzeugen, 
# wenn nicht 10 stellig    
   elif v_geburtsdatum == "TT.MM.JJJJ":
      messagebox.showwarning("Geburtsdatum", "Kein korrektes Datum")
   elif v_geburtsdatumfehler != 10:
      messagebox.showwarning("Geburtsdatum", "Kein korrektes Geburtsdatum\nBitte TT.MM.JJJJ angeben")
      E_geburtsdatum.delete(0, END)
      E_geburtsdatum.insert(10, "TT.MM.JJJJ")
   elif v_eintrittsdatum == "TT.MM.JJJJ":
      messagebox.showwarning("Eintrittsdatum", "Kein korrektes Datum")
   elif v_eintrittsdatumfehler != 10:
      messagebox.showwarning("Eintrittsdatum", "Kein korrektes Eintrittsdatum\nBitte TT.MM.JJJJ angeben")
      E_eintrittsdatum.delete(0, END)
      E_eintrittsdatum.insert(10, "TT.MM.JJJJ")
### es scheint alles zu stimmen - restliche Felder lesen und Variablen zuordnen
   else:
      v_versicherungsnummer = E_versicherungsnummer.get()
      v_krankenkasse = E_krankenkasse.get()
      v_uvgefahrtarif = E_uvgefahrtarif.get()
      v_austritt = E_austritt.get()
      if v_austritt == "TT.MM.JJJJ":
         v_austritt = ""
      else:
         pass
         
      v_elterneigenschaft = str(R_elterneigenschaft.get())

      zv_kv = var_KV.get()
      if zv_kv == ("0 kein Beitrag"):
         v_kv = "0"
      elif zv_kv == ("1 allgemeiner Beitrag"):
         v_kv = "1"
      elif zv_kv == ("3 ermäßigter Beitrag"):
         v_kv = "3"
      elif zv_kv == ("6 Pauschal geringfügig Beschäftigte"):
         v_kv ="6"
      elif zv_kv == ("9 freiwillig KV"):
         v_kv = "9"
      else:
         messagebox.showwarning("SV Schlüssel", "Dieser KV Fehler ist nicht möglich!")
         pass
      zv_kv = ""

      zv_rv = var_RV.get()
      if zv_rv == ("0 kein Beitrag"):
         v_rv = "0"
      elif zv_rv == ("1 allgemeiner Beitrag"):
         v_rv = "1"
      elif zv_rv == ("3 halber Beitrag"):
         v_rv = "3"
      elif zv_rv == ("5 geringfügig entlohnt"):
         v_rv ="5"
      else:
         messagebox.showwarning("SV Schlüssel", "Dieser RV Fehler ist nicht möglich!")
         pass
      zv_rv = ""
     
      zv_av = var_AV.get()
      if zv_av == ("0 kein Beitrag"):
         v_av = "0"
      elif zv_av == ("1 voller Beitrag"):
         v_av = "1"
      elif zv_av == ("2 halber Beitrag"):
         v_av = "2"
      else:
         messagebox.showwarning("SV Schlüssel", "Dieser AV Fehler ist nicht möglich!")
         pass
      zv_av = ""

      zv_pv = var_PV.get()
      if zv_pv == ("0 kein Beitrag"):
         v_pv = "0"
      elif zv_pv == ("1 voller Beitrag"):
         v_pv = "1"
      elif zv_pv == ("2 halber Beitrag"):
         v_pv = "2"
      else:
         messagebox.showwarning("SV Schlüssel", "Dieser PV Fehler ist nicht möglich!")
         pass
      zv_pv = ""

      v_steuerid = E_steuerid.get()
      v_artbeschaeftigung = str(R_artbeschaeftigung.get())
      v_staatsang = E_staatsang.get()
      v_berufsbez = E_berufsbez.get()
      v_weiterebesch = str(R_artbeschaeftigung.get())
      v_weitereauchgering = str(R_weitereauchgering.get())

      zv_pgr = var_PGR.get()
      if zv_pgr == ("101 SV pflichtige Beschäftigte"):
         v_pgr = "101"
      elif zv_pgr == ("102 Auszubildende ohne bes. Merkmale"):
         v_pgr = "102"
      elif zv_pgr == ("104 Hausgewerbetreibende"):
         v_pgr = "104"
      elif zv_pgr == ("105 Praktikanten"):
         v_pgr = "105"
      elif zv_pgr == ("106 Werkstudenten"):
         v_pgr = "106"
      elif zv_pgr == ("108 Bezieher von Vorruhestandsgeld"):
         v_pgr = "108"
      elif zv_pgr == ("109 geringfügig entlohnte Beschäftigte"):
         v_pgr = "109"
      elif zv_pgr == ("110 kurzfristig Beschäftigte"):
         v_pgr = "110"
      elif zv_pgr == ("111 Beschäftigte in berufsfördernden Maßnahmen"):
         v_pgr = "111"
      elif zv_pgr == ("118 Unständig Beschäftigte"):
         v_pgr = "118"
      elif zv_pgr == ("119 versicherungsfreie Altersvollrenter"):
         v_pgr = "119"
      elif zv_pgr == ("190 Beschäftigte, die nur in der gesetzlichen UV"):
         v_pgr = "190"
      elif zv_pgr == ("900 nicht meldepflichtige Beschäftigte"):
         v_pgr = "900"
      else:
         v_pgr ="0"
         messagebox.showwarning("Personengruppenschlüssel", "Dieser PV Fehler ist nicht möglich!")
      zv_pgr = ""

      zv_schulab = var_SCHUL.get()
      if zv_schulab == ("1 ohne Schulabschluss"):
         v_schulab = "1"
      elif zv_schulab == ("2 Haupt-/Volksschulabschluss"):
         v_schulab = "2"
      elif zv_schulab == ("3 mittlere Reife oder gleichwertig"):
         v_schulab = "3"
      elif zv_schulab == ("4 Abitur/Fachabitur"):
         v_schulab = "4"
      elif zv_schulab == ("9 Abschluss unbekannt"):
         v_schulab = "9"
      else:
         v_schulab = "9"
         messagebox.showwarning("Schulabschluss", "Dieser Fehler ist nicht möglich!")
      zv_schulab = ""

      zv_berufab = var_BERUF.get()
      if zv_berufab == ("1 ohne beruflichen Ausbildungsabschluss"):
         v_berufab = "1"
      elif zv_berufab == ("2 Abschluss einer anerkannten Berufsausbildung"):
         v_berufab = "2"
      elif zv_berufab == ("3 Meister-/Techniker- oder gleichwertig"):
         v_berufab = "3"
      elif zv_berufab == ("4 Bachelor"):
         v_berufab = "4"
      elif zv_berufab == ("5 Diplom/Magister/Master/Staatsexamen"):
         v_berufab = "5"
      elif zv_berufab == ("6 Promotion"):
         v_berufab = "6"
      elif zv_berufab == ("9 Abschluss unbekannt"):
         v_berufab = "9"
      else:
         v_berufab = "9"
         messagebox.showwarning("Berufsabschluss", "Dieser Fehler ist nicht möglich!")
      zv_berufab = ""

      v_iban = E_iban.get()

      
      v_gehalt = E_gehalt.get()
      if v_gehalt < ("1") or v_gehalt > ("99999"):
         v_fbid = ""
         v_fbeigenelohnart = ""
      else:
         v_fbid = "1"
         v_fbeigenelohnart = "1"
 
      v_stdlohn = E_stdlohn.get()
      v_waz = E_waz.get()
      v_kostenstelle = E_kostenstelle.get()
      v_geburtsort = E_geburtsort.get()
      v_geburtsland = E_geburtsland.get()
      v_steuerklasse = E_steuerklasse.get()
      v_kinderfreibetrag = E_kinderfreibetrag.get()
      v_faktor = E_faktor.get()
      v_konfession = E_konfession.get()
      v_textfeld = E_textfeld.get()
      
      #######
      # alle Felder wieder leeren und neu belegen 
      # Radiobuton fehlt noch

      E_pnr.delete(0,END)
      E_pnr.insert(5,"99999")
      E_name.delete(0,END)
      E_vname.delete(0,END)
      E_geburtsdatum.delete(0, END)
      E_eintrittsdatum.delete(0, END)
      E_geburtsdatum.insert(15, "TT.MM.JJJJ")
      E_eintrittsdatum.insert(15, "TT.MM.JJJJ")
      E_strasse.delete(0,END)
      E_hnummer.delete(0,END)
      E_plz.delete(0,END)
      E_wohnort.delete(0,END) 
      E_versicherungsnummer.delete(0,END)
      E_krankenkasse.delete(0,END)
      E_uvgefahrtarif.delete(0,END)
      E_austritt.delete(0,END)
      E_austritt.insert(15, "TT.MM.JJJJ")
      var_KV.set(KV_list[1])
      var_RV.set(RV_list[1])
      var_AV.set(AV_list[1])
      var_PV.set(PV_list[1])
      E_steuerid.delete(0,END)
      E_staatsang.delete(0,END)
      E_berufsbez.delete(0,END)
      var_PGR.set(PGR_list[6])
      var_SCHUL.set(SCHUL_list[4])
      var_BERUF.set(BERUF_list[6])
      E_iban.delete(0, END)
      E_gehalt.delete(0,END)
      E_stdlohn.delete(0,END)
      E_waz.delete(0,END)
      E_kostenstelle.delete(0,END)
      E_geburtsort.delete(0,END)
      E_geburtsland.delete(0,END)
      E_steuerklasse.delete(0,END)
      E_kinderfreibetrag.delete(0,END)
      E_faktor.delete(0,END)
      E_konfession.delete(0,END)
      E_textfeld.delete(0,END)

##############################################
### ist schon eine Erfassungsdatei da? 

      if os.path.exists("daten\\pfb_lodas.txt"):
         ## Datei öffnen und Daten werden angehangen
         fileziel=open("daten\\pfb_lodas.txt","a")
      else:
         ## Datei neu öffnen und Kopfdaten schreiben
         fileziel=open("daten\\pfb_lodas.txt","w")
         ## Beraternummer, Mandantennummer ** anpassen an die eigene BNR, Mdt
         fileziel.write("[Allgemein]\nZiel=LODAS\nVersion_SST=1.0\nBeraterNr=999999\nMandantenNr=99999\n")
         fileziel.write("Stringbegrenzer='\n\n* LEGENDE:\n* Datei erzeugt mit Tool main_arm_pfb\n* AP: Andreé Rosenkranz; andree@rosenkranz.one")
         fileziel.write("\n\n* Satzbeschreibungen zur Anlage von Stammdaten für Mitarbeiter\n\n")
         ## schreiben der Satzarten
         fileziel.write("[Satzbeschreibung]")
         fileziel.write("\n10;u_lod_psd_beschaeftigung;pnr#psd;eintrittdatum#psd;austrittdatum#psd;arbeitsverhaeltnis#psd;schriftl_befristung#psd;datum_urspr_befr#psd;abschl_befr_arbvertr#psd;verl_befr_arbvertr#psd;befr_gr_2_monate#psd;")
         fileziel.write("\n11;u_lod_psd_mitarbeiter;pnr#psd;duevo_familienname#psd;duevo_vorname#psd;adresse_strassenname#psd;adresse_strasse_nr#psd;adresse_ort#psd;adresse_plz#psd;staatsangehoerigkeit#psd;geburtsdatum_ttmmjj#psd;geschlecht#psd;familienstand#psd;sozialversicherung_nr#psd;adresse_anschriftenzusatz#psd;gebort#psd;")
         fileziel.write("\n12;u_lod_psd_taetigkeit;pnr#psd;berufsbezeichnung#psd;persgrs#psd;schulabschluss#psd;ausbildungsabschluss#psd;stammkostenstelle#psd;")
         fileziel.write("\n13;u_lod_psd_arbeitszeit_regelm;pnr#psd;az_wtl_indiv#psd;")
         fileziel.write("\n14;u_lod_psd_steuer;pnr#psd;identifikationsnummer#psd;els_2_haupt_ag_kz#psd;st_klasse#psd;kfb_anzahl#psd;faktor#psd;")
         fileziel.write("\n15;u_lod_psd_sozialversicherung;pnr#psd;kz_zuschl_pv_kinderlose#psd;kv_bgrs#psd;rv_bgrs#psd;av_bgrs#psd;pv_bgrs#psd;")
         fileziel.write("\n16;u_lod_psd_ma_bank;pnr#psd;ma_bank_zahlungsart#psd;ma_iban#psd;")
         fileziel.write("\n17;u_lod_psd_festbezuege;pnr#psd;festbez_id#psd;lohnart_nr#psd;betrag#psd;")
         fileziel.write("\n18;u_lod_psd_lohn_gehalt_bezuege;pnr#psd;std_lohn_1#psd;")
         fileziel.write("\n\n* Stammdaten zur Anlage von Mitarbeitern\n")
      
      ####### Daten schreiben
      fileziel.write("\n[Stammdaten]\n10;"+v_pnr+";"+v_eintrittsdatum+";"+v_austritt+";;;;;;")
      fileziel.write("\n11;"+v_pnr+";'"+v_name+"';'"+v_vname+"';'"+v_strasse+"';'"+v_hnummer+"';'"+v_wohnort+"';"+v_plz+";000;"+v_geburtsdatum+";"+v_geschlecht+";;"+v_versicherungsnummer+";;'"+v_geburtsort+"';")
      fileziel.write("\n12;"+v_pnr+";'"+v_berufsbez+"';"+v_pgr+";"+v_schulab+";"+v_berufab+";"+v_kostenstelle+";")
      fileziel.write("\n13;"+v_pnr+";"+v_waz+";")
      fileziel.write("\n14;"+v_pnr+";'"+v_steuerid+"';"+v_artbeschaeftigung+";"+v_steuerklasse+";"+v_kinderfreibetrag+";;")
      fileziel.write("\n15;"+v_pnr+";"+v_elterneigenschaft+";"+v_kv+";"+v_rv+";"+v_av+";"+v_pv+";")
      fileziel.write("\n16;"+v_pnr+";5;"+v_iban+";")
      fileziel.write("\n17;"+v_pnr+";"+v_fbid+";"+v_fbeigenelohnart+";"+v_gehalt+";")
      fileziel.write("\n18;"+v_pnr+";"+v_stdlohn+";")
      fileziel.write("\n[Hinweisdaten]\n'**"+v_pnr+"** Krankenkasse: "+v_krankenkasse+" ** Gefahrtarif: "+v_uvgefahrtarif+" ** Staatsangehörigkeit: "+v_staatsang+" ** weitere Beschäftigung: "+v_weiterebesch+" (1=ja)** weitere Besch. auch geringfüging: "+v_weitereauchgering+" (1=ja)")
      fileziel.write("** Geburtsland: "+v_geburtsland+" ** Konfession: "+v_konfession+" ** Faktor zur Steuer: "+v_faktor+" ** Informationen aus dem Textfeld: "+v_textfeld+"'")   

      fileziel.close()

#################################################################################################

def konvertieren():
   # kopieren der Erfassunsgdatei in einen Lodas import mit Protokoll
   if os.path.exists("daten\\pfb_lodas.txt"):
      ZielDatei = os.path.join(time.strftime('%Y%m%d_%H%M'))
      copyfile("daten\\pfb_lodas.txt","sicherung\\"+(ZielDatei)+"_pfb.sic")
      os.rename("daten\\pfb_lodas.txt","daten\\"+(ZielDatei)+"_pfb_lodas.txt")
      messagebox.showinfo("Konvertierung", "Die Datei "+str(ZielDatei)+"_lodas.txt in dem Verzeichnis \\daten\\ steht für LODAS bereit!")
   else:
      messagebox.showwarning("Quelldatei", "Es ist keine Datei zur Konvertierung vorhanden")
   
### Ende 

def kurzhilfe():
   messagebox.showwarning("Hinweise zur Verwendung", "Personalnummer zwischen 1 und 99999.\nDie Personalnummer darf NICHT in Lodas vergeben sein!\nDatumsangaben Tage und Monate immer 2 stellig,\ndas Jahr 4 stellig. Datum Trennzeichen Punkt.")

def exit():
    root.destroy()
    return

#GUI definieren
root = Tk()
#######################################################################################################################################

#################
# # Bildschirm aufbauen
#################
root.iconbitmap("format/datevreport.ico")
root.configure(bg='#FAFAFA')
root.title("Personalfragebogen V0.1a")

screen_breite = root.winfo_screenwidth()
screen_hoehe = root.winfo_screenheight()
width  = 1200 #später auf BSGröße anpassen
height = 800
x_coord = (screen_breite/2) - (width/2)
y_coord = (screen_hoehe/2) - (height/2)
root.wm_geometry("%dx%d+%d+%d"  % (width,height, x_coord, y_coord))

#Rahmen definieren

#Bildschirm füllen

#Steuerrung über Button
button_neuanlage = Button(root, width=22, text = "Speichern und Neuanlage", font="Verdana 10", command=speichern_neu_AN, bg="#E6E6E6")
button_neuanlage.place(x = 10, y = 10)
button_konv = Button(root, width=10, text = "Konvertieren", font="Verdana 10", command=konvertieren, bg="#E6E6E6")
button_konv.place(x = 208, y = 10)
L_hinweis_dsgvo = Label(root, text= "Beachten Sie die Hinweise zur DSGVO in der Hilfe!", font="Verdana 13", bg="#E6E6E6")
L_hinweis_dsgvo.place(x= 504, y= 11)
button_kurzhilfe = Button(root, text="Kurzhilfe", width=10, height=1, font="Verdana 10", command=kurzhilfe, bg="#E6E6E6")
button_kurzhilfe.place(x=950, y=10)
button_hilfe = Button(root, text="Hilfe", width=5, height=1, font="Verdana 10", command= lambda:os.system('Handbuch_PFB2LODAS.pdf'), bg="#E6E6E6")
button_hilfe.place(x=1040, y=10)
button_exit = Button(root, text="Exit", width=5, height=1, font="Verdana 10", command=exit, bg="#E6E6E6")
button_exit.place(x=1100, y=10)

#################
#Erfassungsfelder
#################

L_hinweis_01 = Label(root, text= "Pflichtfelder:", font="Verdana 15")
L_hinweis_01.place(x= 10, y= 60)

#Rahmen in rot für Pflichtfelder

L_redline = Label(root, bg='#FF0000')
L_redline1 = Label(root, bg='#FF0000')
L_redline2 = Label(root, bg='#FF0000')
L_redline3 = Label(root, bg='#FF0000')
L_redline.place(x=150, y=85,height=1, width=800)
L_redline1.place(x=950, y=85,height=101, width=1)
L_redline2.place(x=10, y=185,height=1, width=740)
L_redline3.place(x=900, y=185,height=1, width=50)
L_redlined = Label(root, bg='#FF0000')
L_redlined1 = Label(root, bg='#FF0000')
L_redlined2 = Label(root, bg='#FF0000')
L_redlined3 = Label(root, bg='#FF0000')
L_redlined.place(x=150, y=82,height=2, width=804)
L_redlined1.place(x=952, y=82,height=106, width=2)
L_redlined2.place(x=10, y=187,height=2, width=740)
L_redlined3.place(x=900, y=187,height=2, width=54)

#Zeile 1: Personalnummer, Name, Vorname, Geburtsdatum, Eintrittdatum  
L_pnr = Label(root,text = "PNR(5)", bg='#FAFAFA', font="Verdana 10")
L_pnr.place(x = 10,y = 100)
E_pnr = Entry(root,bd = 1)
E_pnr.place(x = 70,y = 100, height=25, width=60)
# ggf. nächste freie PNR
E_pnr.insert(10,"99999")

L_name = Label(root,text = "Name", bg='#FAFAFA', font="Verdana 10")
L_name.place(x = 140,y = 100)
E_name = Entry(root,bd = 1)
E_name.place(x = 190,y = 100, height=25, width=120)

L_vname = Label(root, text = "Vorname", bg='#FAFAFA', font="Verdana 10" )
L_vname.place(x = 320,y = 100)
E_vname = Entry(root, bd = 1)
E_vname.place(x = 390,y = 100, height=25, width=120)

L_geburtsdatum = Label(root, text= "Geburtsdatum", bg='#FAFAFA', font="Verdana 10" )
L_geburtsdatum.place(x= 520,y = 100)
E_geburtsdatum = Entry(root, bd = 1)
E_geburtsdatum.place(x = 630, y = 100, height=25, width=80)
E_geburtsdatum.insert(15,"TT.MM.JJJJ")

L_eintrittsdatum = Label(root, text= "Eintrittsdatum", bg='#FAFAFA', font="Verdana 10" )
L_eintrittsdatum.place(x= 720,y = 100)
E_eintrittsdatum = Entry(root, bd = 1)
E_eintrittsdatum.place(x = 830, y = 100, height=25, width=80)
E_eintrittsdatum.insert(15,"TT.MM.JJJJ")

#Zeile 2: Strasse, Hausnummer, PLZ, Wohnort, Geschlecht
L_strasse = Label(root, text= "Strasse", bg='#FAFAFA', font="Verdana 10" )
L_strasse.place(x= 10,y = 150)
E_strasse = Entry(root, bd = 1)
E_strasse.place(x = 70, y = 150, height=25, width=240)

L_hnummer = Label(root, text= "Haus-Nr.", bg='#FAFAFA', font="Verdana 10" )
L_hnummer.place(x= 320,y = 150)
E_hnummer = Entry(root, bd = 1)
E_hnummer.place(x = 390, y = 150, height=25, width=40)

L_plz = Label(root, text= "PLZ", bg='#FAFAFA', font="Verdana 10" )
L_plz.place(x= 440,y = 150)
E_plz = Entry(root, bd = 1)
E_plz.place(x = 480, y = 150, height=25, width=40)

L_wohnort = Label(root, text= "Ort", bg='#FAFAFA', font="Verdana 10" )
L_wohnort.place(x= 550,y = 150)
E_wohnort = Entry(root, bd = 1)
E_wohnort.place(x = 580, y = 150, height=25, width=240)

L_geschlecht = Label(root, text="Geschlecht", bg='#FAFAFA', font="Verdana 10")
L_geschlecht.place(x = 750, y = 175)
# radiobutton weiblich männlich divers
def sel():
   pass
R_geschlecht = IntVar()
R1 = Radiobutton(root, text="weiblich", bg='#FAFAFA', variable=R_geschlecht, value=1,
                  command=sel)
R1.place(x = 830, y = 155)
R2 = Radiobutton(root, text="männlich", bg='#FAFAFA', variable=R_geschlecht, value=0,
                  command=sel)
R2.place(x = 830, y = 175)
R3 = Radiobutton(root, text="divers", bg='#FAFAFA', variable=R_geschlecht, value=2,
                  command=sel)
R3.place(x = 830, y = 195)

###############
### Block 2 ###
###############

# notwendige Felder 
L_hinweis_02 = Label(root, text= "notwendige Angaben:", font="Verdana 15")
L_hinweis_02.place(x= 10, y= 200)

L_greenline = Label(root, bg='#00FF7F')
L_greenline1 = Label(root, bg='#00FF7F')
L_greenline11 = Label(root, bg='#00FF7F')
L_greenline2 = Label(root, bg='#00FF7F')
L_greenline.place(x=240, y=225,height=1, width=860)
L_greenline1.place(x=600, y=225,height=256, width=1)
L_greenline11.place(x=1100, y=225,height=256, width=1)
L_greenline2.place(x=10, y=480,height=1, width=1090)
L_greenlined = Label(root, bg='#00FF7F')
L_greenlined1 = Label(root, bg='#00FF7F')
L_greenlined11 = Label(root, bg='#00FF7F')
L_greenlined2 = Label(root, bg='#00FF7F')
L_greenlined.place(x=240, y=222,height=2, width=862)
L_greenlined1.place(x=602, y=222,height=262, width=2)
L_greenlined11.place(x=1102, y=222,height=262, width=2)
L_greenlined2.place(x=10, y=482,height=2, width=1092)

###########
## links ##
###########

# SV Nummer, Krankenkasse, UV Gefahrtarif, Austritt, Elterneigenschaft 
L_versicherungsnummer = Label(root, text= "SV Nummer", bg='#FAFAFA', font="Verdana 10" )
L_versicherungsnummer.place(x= 10,y = 245)
E_versicherungsnummer = Entry(root, bd = 1)
E_versicherungsnummer.place(x = 120, y = 245, height=25, width=190)

L_krankenkasse = Label(root, text= "Krankenkasse", bg='#FAFAFA', font="Verdana 10" )
L_krankenkasse.place(x= 10,y = 295)
E_krankenkasse = Entry(root, bd = 1)
E_krankenkasse.place(x = 120, y = 295, height=25, width=190)

L_uvgefahrtarif = Label(root, text= "UV-Gefahrtarif", bg='#FAFAFA', font="Verdana 10" )
L_uvgefahrtarif.place(x= 10, y = 345)
E_uvgefahrtarif = Entry(root, bd = 1)
E_uvgefahrtarif.place(x = 120, y = 345, height=25, width=105)

L_austritt =  Label(root, text= "Austrittsdatum", bg='#FAFAFA', font="Verdana 10" )
L_austritt.place(x= 10, y = 415)
E_austritt = Entry(root, bd = 1)
E_austritt.place(x = 120, y = 415, height=25, width=105)
E_austritt.insert(15,"TT.MM.JJJJ")

L_elterne = Label(root, text="Elterneigenschaft", bg='#FAFAFA', font="Verdana 10")
L_elterne.place(x = 350, y = 245)
def sel2():
   pass
R_elterneigenschaft = IntVar()
R_eltern1 = Radiobutton(root, text="ja", bg='#FAFAFA', variable=R_elterneigenschaft, value=1,
                  command=sel2)
R_eltern1.place(x = 480, y = 235)
R_eltern2 = Radiobutton(root, text="nein", bg='#FAFAFA', variable=R_elterneigenschaft, value=0,
                  command=sel2)
R_eltern2.place(x = 480, y = 255)

#KV,RV,AV,PV
L_kv = Label(root, text= "KV", bg='#FAFAFA', font="Verdana 10" )
L_kv.place(x= 330,y = 295)
KV_list = ["0 kein Beitrag","1 allgemeiner Beitrag","3 ermäßigter Beitrag","6 Pauschal geringfügig Beschäftigte", "9 freiwillig KV"]
var_KV = StringVar(root)
var_KV.set(KV_list[1])
D_kv = OptionMenu(root, var_KV, *KV_list)
D_kv.place(x = 355, y = 295, height=25, width=230)

L_rv = Label(root, text= "RV", bg='#FAFAFA', font="Verdana 10" )
L_rv.place(x= 330,y = 335)
RV_list = ["0 kein Beitrag","1 allgemeiner Beitrag","3 halber Beitrag","5 geringfügig entlohnt"]
var_RV = StringVar(root)
var_RV.set(RV_list[1])
D_rv = OptionMenu(root, var_RV, *RV_list)
D_rv.place(x = 355, y = 335, height=25, width=170)

L_av = Label(root, text= "AV", bg='#FAFAFA', font="Verdana 10" )
L_av.place(x= 330,y = 375)
AV_list = ["0 kein Beitrag","1 voller Beitrag","2 halber Beitrag"]
var_AV = StringVar(root)
var_AV.set(AV_list[1])
D_av = OptionMenu(root, var_AV, *AV_list)
D_av.place(x = 355, y = 375, height=25, width=170)

L_pv = Label(root, text= "PV", bg='#FAFAFA', font="Verdana 10" )
L_pv.place(x= 330,y = 415)
PV_list = ["0 kein Beitrag","1 voller Beitrag","2 halber Beitrag"]
var_PV = StringVar(root)
var_PV.set(PV_list[1])
D_pv = OptionMenu(root, var_PV, *PV_list)
D_pv.place(x = 355, y = 415, height=25, width=170)

### rechts

#Steuer ID, PGR, Staatsangehörigkeit 
L_steuerid = Label(root, text="Steuer Id", bg='#FAFAFA', font="Verdana 10")
L_steuerid.place(x=610 , y = 245)
E_steuerid = Entry(root, bd = 1)
E_steuerid.place(x = 750, y = 245, height=25, width=130) 

L_artbesch = Label(root, text="Art der Beschäftigung", bg='#FAFAFA', font="Verdana 10")
L_artbesch.place(x= 900 , y = 245)
def sel3():
   pass
R_artbeschaeftigung = IntVar()
R_artbesch1 = Radiobutton(root, text="Hauptbeschäftigung", bg='#FAFAFA', variable=R_artbeschaeftigung, value=0,
                  command=sel3)
R_artbesch1.place(x = 1050, y = 236)
R_artbesch2 = Radiobutton(root, text="Nebenbeschäftigung", bg='#FAFAFA', variable=R_artbeschaeftigung, value=1,
                  command=sel3)
R_artbesch2.place(x = 1050, y = 260)

L_staatsang = Label(root, text="Staatsangehörigkeit", bg='#FAFAFA', font="Verdana 10")
L_staatsang.place(x=610 , y = 295)
E_staatsang = Entry(root, bd = 1)
E_staatsang.place(x = 750, y = 295, height=25, width=130) 

#Berufbezeichnung, Art der Beschäftigung, weitere Beschäftigung, weitere geringfügige Beschäftigung
L_berufsbez = Label(root, text="Berufsbezeichnung", bg='#FAFAFA', font="Verdana 10")
L_berufsbez.place(x= 610 , y = 345)
E_berufsbez = Entry(root, bd = 1)
E_berufsbez.place(x = 750, y = 345, height=25, width=130) 

L_weiterebesch = Label(root, text="weitere Beschäftigung", bg='#FAFAFA', font="Verdana 10")
L_weiterebesch.place(x= 900 , y = 295)
def sel4():
   pass
R_weiterebesch = IntVar()
R_weiterebesch1 = Radiobutton(root, text="nein", bg='#FAFAFA', variable=R_weiterebesch, value=0,
                  command=sel4)
R_weiterebesch1.place(x = 1050, y = 284)
R_weiterebesch2 = Radiobutton(root, text="ja", bg='#FAFAFA', variable=R_weiterebesch, value=1,
                  command=sel4)
R_weiterebesch2.place(x = 1050, y = 308)

L_auchgering = Label(root, text="wei. auch Geringfügig", bg='#FAFAFA', font="Verdana 10")
L_auchgering.place(x= 900, y = 345)
def sel5():
   pass
R_weitereauchgering = IntVar()
R_auchgering1 = Radiobutton(root, text="nein", bg='#FAFAFA', variable=R_weitereauchgering, value=0,
                  command=sel5)
R_auchgering1.place(x = 1050, y = 336)
R_auchgering2 = Radiobutton(root, text="ja", bg='#FAFAFA', variable=R_weitereauchgering, value=1,
                  command=sel5)
R_auchgering2.place(x = 1050, y = 360)

L_personengruppe = Label(root, text="Personengruppe", bg='#FAFAFA', font="Verdana 10")
L_personengruppe.place(x=610 , y = 390)
PGR_list = [
   "101 SV pflichtige Beschäftigte",
   "102 Auszubildende ohne bes. Merkmale",
   "104 Hausgewerbetreibende",
   "105 Praktikanten",
   "106 Werkstudenten",
   "108 Bezieher von Vorruhestandsgeld",
   "109 geringfügig entlohnte Beschäftigte",
   "110 kurzfristig Beschäftigte",
   "111 Beschäftigte in berufsfördernden Maßnahmen",
   "118 Unständig Beschäftigte",
   "119 versicherungsfreie Altersvollrenter",
   "190 Beschäftigte, die nur in der gesetzlichen UV",
   "900 nicht meldepflichtige Beschäftigte"
   ]
var_PGR = StringVar(root)
var_PGR.set(PGR_list[6])
D_pgr = OptionMenu(root, var_PGR, *PGR_list)
D_pgr.place(x = 750, y = 390, height=25, width=330)

#Schulabschluss, Berufsausbildung
L_schulab = Label(root, text="höchster Schulabschluss", bg='#FAFAFA', font="Verdana 10")
L_schulab.place(x=610 , y = 420)
SCHUL_list = [
   "1 ohne Schulabschluss",
   "2 Haupt-/Volksschulabschluss",
   "3 mittlere Reife oder gleichwertig",
   "4 Abitur/Fachabitur",
   "9 Abschluss unbekannt"
   ]
var_SCHUL = StringVar(root)
var_SCHUL.set(SCHUL_list[4])
D_schulab = OptionMenu(root, var_SCHUL, *SCHUL_list)
D_schulab.place(x = 800, y = 420, height=25, width=280)

L_berufab = Label(root, text="höchste Berufsausbildung", bg='#FAFAFA', font="Verdana 10")
L_berufab.place(x=610 , y = 450)
BERUF_list = [
   "1 ohne beruflichen Ausbildungsabschluss",
   "2 Abschluss einer anerkannten Berufsausbildung",
   "3 Meister-/Techniker- oder gleichwertig",
   "4 Bachelor",
   "5 Diplom/Magister/Master/Staatsexamen",
   "6 Promotion",
   "9 Abschluss unbekannt"
   ]
var_BERUF = StringVar(root)
var_BERUF.set(BERUF_list[6])
D_berufab = OptionMenu(root, var_BERUF, *BERUF_list)
D_berufab.place(x = 800, y = 450, height=25, width=280)

###############
### Block 3 ###
###############

L_greenline = Label(root, bg='#00FF7F')
L_greenline1 = Label(root, bg='#00FF7F')
L_greenline2 = Label(root, bg='#00FF7F')
L_greenline.place(x=175, y=525,height=1, width=925)
L_greenline1.place(x=1100, y=525,height=111, width=1)
L_greenline2.place(x=10, y=635,height=1, width=1090)
L_greenlined = Label(root, bg='#00FF7F')
L_greenlined1 = Label(root, bg='#00FF7F')
L_greenlined2 = Label(root, bg='#00FF7F')
L_greenlined.place(x=175, y=522,height=2, width=927)
L_greenlined1.place(x=1102, y=522,height=117, width=2)
L_greenlined2.place(x=10, y=637,height=2, width=1092)

#Verdienst und Vertragsdaten

L_hinweis_03 = Label(root, text= "Vertragsdaten:", font="Verdana 15")
L_hinweis_03.place(x= 10, y= 500)

L_iban = Label(root, text = "IBAN", bg='#FAFAFA', font="Verdana 10" )
L_iban.place(x = 10, y = 550)
E_iban = Entry(root, bd = 1)
E_iban.place(x = 60,y = 550, height=25, width=150)

L_gehalt = Label(root, text="Gehalt", bg='#FAFAFA', font="Verdana 10")
L_gehalt.place(x = 220 , y = 550)
E_gehalt = Entry(root, bd = 1)
E_gehalt.place(x = 280, y = 550, height=25, width=60) 

L_stdlohn = Label(root, text="oder Stundenlohn", bg='#FAFAFA', font="Verdana 10")
L_stdlohn.place(x=350 , y = 550)
E_stdlohn = Entry(root, bd = 1)
E_stdlohn.place(x = 480, y = 550, height=25, width=60) 

L_stdlab = Label(root, text= "gültig ab Eintritt (Gehalt mit anteiliger Berechnung bei Teilmonat)", bg='#FAFAFA', font="Verdana 10" )
L_stdlab.place(x= 550,y = 550)

#wöchentliche Arbeitszeit, Vertragsform 
L_waz = Label(root, text = "wöchentliche Arbeitszeit", bg='#FAFAFA', font="Verdana 10" )
L_waz.place(x = 100, y = 600)
E_waz = Entry(root, bd = 1)
E_waz.place(x = 280,y = 600, height=25, width=60) 

L_kostenstelle = Label(root, text = "Kostenstelle", bg='#FAFAFA', font="Verdana 10" )
L_kostenstelle.place(x = 385, y = 600)
E_kostenstelle = Entry(root, bd = 1)
E_kostenstelle.place(x = 480, y = 600, height=25, width=100) 


###############
### Block 4 ###
###############

L_blackline = Label(root, bg='#000000')
L_blackline1 = Label(root, bg='#000000')
L_blackline2 = Label(root, bg='#000000')
L_blackline.place(x=425, y=675,height=1, width=675)
L_blackline1.place(x=1100, y=675,height=116, width=1)
L_blackline2.place(x=10, y=790,height=1, width=1090)
L_blacklined = Label(root, bg='#000000')
L_blacklined1 = Label(root, bg='#000000')
L_blacklined2 = Label(root, bg='#000000')
L_blacklined.place(x=425, y=672,height=2, width=677)
L_blacklined1.place(x=1102, y=672,height=122, width=2)
L_blacklined2.place(x=10, y=792,height=2, width=1092)

#wenn Daten fehlen = 

L_hinweis_04 = Label(root, text= "SV und Steuer - wenn Angaben fehlen!", font="Verdana 15")
L_hinweis_04.place(x= 10, y= 650)

#SV
L_geburtsort = Label(root, text = "Geburtsort", bg='#FAFAFA', font="Verdana 10" )
L_geburtsort.place(x = 10, y = 700)
E_geburtsort = Entry(root, bd = 1)
E_geburtsort.place(x = 110, y = 700, height=25, width=120) 

L_geburtsland = Label(root, text = "Geburtsland", bg='#FAFAFA', font="Verdana 10" )
L_geburtsland.place(x = 260, y = 700)
E_geburtsland = Entry(root, bd = 1)
E_geburtsland.place(x = 360, y = 700, height=25, width=120) 

#Steuer
L_steuerklasse = Label(root, text = "Steuerklasse", bg='#FAFAFA', font="Verdana 10" )
L_steuerklasse.place(x = 10, y = 750)
E_steuerklasse = Entry(root, bd = 1)
E_steuerklasse.place(x = 110, y = 750, height=25, width=20) 

L_kinderfreibetrag = Label(root, text = "Kinderfreibetrag", bg='#FAFAFA', font="Verdana 10" )
L_kinderfreibetrag.place(x = 140, y = 750)
E_kinderfreibetrag = Entry(root, bd = 1)
E_kinderfreibetrag.place(x = 260, y = 750, height=25, width=30) 

L_faktor = Label(root, text = "Faktor", bg='#FAFAFA', font="Verdana 10" )
L_faktor.place(x = 300, y = 750)
E_faktor = Entry(root, bd = 1)
E_faktor.place(x = 360, y = 750, height=25, width=30)

L_konfession = Label(root, text="Konfession", bg='#FAFAFA', font="Verdana 10")
L_konfession.place(x = 415 , y = 750)
E_konfession = Entry(root, bd = 1)
E_konfession.place(x = 500, y = 750, height=25, width=50)

L_textfeld = Label(root, text="Nachricht:", bg='#FAFAFA', font="Verdana 10")
L_textfeld.place(x = 530 , y = 700)
E_textfeld = Entry(root, bd = 1)
E_textfeld.place(x = 620, y = 700, height=80, width=440)


#######
## Start
#######

root.mainloop()
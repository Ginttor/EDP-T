import xml.etree.ElementTree as ET
import webbrowser as wb
import os

re=open("elpdf.txt", "r",encoding='utf-8')
pdfee=re.readlines()
re.close()
eg=open("exp.txt", "r")
ex=eg.readlines()
eg.close()
re=open("listt/L-sospe.txt", "r",encoding='utf-8')
sos=re.readlines()
re.close()
re=open("listt/L-trans.txt", "r",encoding='utf-8')
tra=re.readlines()
re.close()
re=open("listt/L-alime.txt", "r",encoding='utf-8')
ali=re.readlines()
re.close()
re=open("listt/L-comui.txt", "r",encoding='utf-8')
com=re.readlines()
re.close()
re=open("listt/L-vesti.txt", "r",encoding='utf-8')
ves=re.readlines()
re.close()
re=open("listt/L-varia.txt", "r",encoding='utf-8')
bar=re.readlines()
re.close()
re=open("listt/L-vivie.txt", "r",encoding='utf-8')
viv=re.readlines()
re.close()
re=open("listt/L-depor.txt", "r",encoding='utf-8')
dep=re.readlines()
re.close()
re=open("listt/L-educa.txt", "r",encoding='utf-8')
edu=re.readlines()
re.close()
re=open("listt/L-salud.txt", "r",encoding='utf-8')
sal=re.readlines()
re.close()

def estka(ile):
    z=0
    while z<len(ex):
        xe=ex[z].replace("\n", "")
        #print("ele:",xe)
        if len(xe)<=8:
            q=9-len(xe);qi=0
            while qi<=q:
                #print(len(ex[z]),"/",q)
                xe="0"+xe
                qi+=1
        #print("ele:",xe)
        if 0<ile[1].count(xe):
            ile[1]+="<YA ESTA OCUPADO>"
            print("<YA ESTA OCUPADO>")
        z+=1
    ile[1]=ile[1].replace(" ", "")
    print("estka: completado")
    return ile
def ojo(feria,feed,ile):
            #print("op")
            ss=0
            while ss<len(sos):
                if 0<feed.count(sos[ss].replace("\n", "")):
                    ile[6]="sospechoso"
                    ile[7]+=feed+"|"
                ss+=1
            tr=0
            while tr<len(tra):
                if 0<feed.count(tra[tr].replace("\n", "")):
                    if ile[6]=="":ile[6]="TRANSPORTE"
                    ile[7]+=feed+"|"
                tr+=1
            al=0
            while al<len(ali):
                if 0<feed.count(ali[al].replace("\n", "")):
                    if ile[6]=="":ile[6]="ALIMENTACION"
                    ile[7]+=feed+"|"
                al+=1
            cp=0
            while cp<len(com):
                if 0<feed.count(com[cp].replace("\n", "")):
                    if ile[6]=="":ile[6]="COMUNICACION"
                    ile[7]+=feed+"|"
                cp+=1
            ve=0
            while ve<len(ves):
                if 0<feed.count(ves[ve].replace("\n", "")):
                    if ile[6]=="":ile[6]="VESTIMENTA"
                    ile[7]+=feed+"|"
                ve+=1
            va=0
            while va<len(bar):
                #print("op", feed)
                if 0<feed.count(bar[va].replace("\n", "")) and ile[6]!="sospechoso":
                    #print("op1")
                    ile[6]="<o>"
                    ile[7]+=feed+"|"
                va+=1
            vi=0
            while vi<len(viv):
                if 0<feed.count(viv[vi].replace("\n", "")):
                    if ile[6]=="":ile[6]="VIVIENDA"
                    ile[7]+=feed+"|"
                vi+=1
            di=0
            while di<len(dep):
                if 0<feed.count(dep[di].replace("\n", "")):
                    if ile[6]=="":ile[6]="DEPORTE"
                    ile[7]+=feed+"|"
                di+=1
            el=0
            while el<len(edu):
                if 0<feed.count(edu[el].replace("\n", "")):
                    if ile[6]=="":ile[6]="EDUCACION"
                    ile[7]+=feed+"|"
                el+=1
            da=0
            while da<len(sal):
                if 0<feed.count(sal[da].replace("\n", "")):
                    if ile[6]=="":ile[6]="SALUD"
                    ile[7]+=feed+"|"
                da+=1
            if 0<feed.count("MEDINA GUEVARA WALTER BERNABE"):
                feria=True
            if 0<feed.count("SUPERMERCADO LA FERIA") and feria==True:
                ile[6]="sospechoso"
                ile[7]+=feed+"|"
                feria=False
            ile[7]=ile[7].replace("\n", "|")
            ile[7]=ile[7].replace("descripcion", "")
            ile[7]=ile[7].replace("razonSocial", "")
            ile[7]=ile[7].replace("nombreComercial", "")
            ile[7]=ile[7].replace("/", "")
            ile[7]=ile[7].replace("  ", "")
            ile[7]=ile[7].replace("<", "")
            ile[7]=ile[7].replace(">", "")
            return ile
def analy(tpa3, ile):
        print(">>Analisis de archimo XML en marcaha...")
        x=0;i=0;f=0      
        while x<len(tpa3):
            if 0<tpa3[x].count("infoTributaria"):
                print(tpa3[x])
                if 0<tpa3[x+20].count("identificacionComprador>"):
                    ile[9]=tpa3[x+20]
                    ile[9]=ile[9].replace("identificacionComprador", "")
                    ile[9]=ile[9].replace("/", "")
                    ile[9]=ile[9].replace(">", "")
                    ile[9]=ile[9].replace("<", "")
                    ile[9]=ile[9].replace(" ", "")
                if 0<tpa3[x+3].count("razonSocial>"):
                    ile=ojo(False,tpa3[x+3],ile)
                if 0<tpa3[x+4].count("nombreComercial>"):
                    ile=ojo(False,tpa3[x+4],ile)
                    ile[7]=ile[7].replace("nombreComercial>", "")
                    ile[7]=ile[7].replace("</nombreComercial", "")
                if 0<tpa3[x+5].count("ruc>"):#RUC
                    #print("<ruc>")
                    agd2=tpa3[x+5].replace("ruc", "")
                    ile[0]=agd2
                    ile[0]=ile[0].replace("/", "")
                    ile[0]=ile[0].replace(">", "")
                    ile[0]=ile[0].replace("<", "")
                    ile[0]=ile[0].replace(" ", "")
                    ile[0]=ile[0].replace("\t", "")
                z=0
                while z<20:#NO. factura
                    if 0<tpa3[x+z].count("estab>"):
                        y=0;ile[1]=""
                        while y<3:
                            agd6=tpa3[x+z+y]
                            if y<2:ile[1]+=str(agd6)+"-"
                            else:ile[1]+=str(agd6)
                            y+=1
                        ile[1]=ile[1].replace("estab", "")
                        ile[1]=ile[1].replace("/", "")
                        ile[1]=ile[1].replace(">", "")
                        ile[1]=ile[1].replace("<", "")
                        ile[1]=ile[1].replace("ptoEmi", "")
                        ile[1]=ile[1].replace("secuencial", "")
                        ile[1]=ile[1].replace(" ", "")
                        ile[1]=ile[1].replace("\t", "")
                    z+=1
            if 0<tpa3[x].count("infoFactura"):
                #print("infoFactura")
                if 0<tpa3[x+7].count("identificacionComprador>"):
                    ile[8]=ile[8].replace("identificacionComprador>", "")
                    ile[8]=ile[8].replace("</identificacionComprador", "")
                if 0<tpa3[x+1].count("fechaEmision>"):#fecha
                    #print(tpa3[x+1])
                    agd1=tpa3[x+1].replace("fechaEmision>", "")
                    agd2=agd1.replace("</fechaEmision", "")
                    agd3=agd2.split("/")
                    ile[2]=agd3[0];ile[2]=ile[2].replace("<", "");ile[2]=ile[2].replace(" ", "")
                    ile[3]=agd3[1];ile[3]=ile[3].replace("<", "")
                    ile[4]=agd3[2];ile[4]=ile[4].replace("<", "")
                z=0
                while 20>z:#IVA 12%
                    #print("totalConImpuestos")
                    if 0<tpa3[x+z].count("totalConImpuestos"):
                        z1=0
                        while 20>z1:
                            if 0<tpa3[x+z+z1].count("baseImponible>"):
                                ile[8]="T:"+"["+tpa3[x+z+z1]+"]"
                                ile[8]=ile[8].replace("baseImponible", "")
                                ile[8]=ile[8].replace("/", "")
                                ile[8]=ile[8].replace("<", "")
                                ile[8]=ile[8].replace(">", "")
                                ile[8]=ile[8].replace(" ", "")
                            z1+=1
                        z1=0
                        while 20>z1:
                            if 0<tpa3[x+z+z1].count("valor>"):
                                print("valor")
                                ile[5]=tpa3[x+z+z1]
                                ile[5]=ile[5].replace("valor", "")
                                ile[5]=ile[5].replace("/", "")
                                ile[5]=ile[5].replace("<", "")
                                ile[5]=ile[5].replace(">", "")
                                ile[5]=ile[5].replace(" ", "")
                            z1+=1
                    z+=1
            if 0<tpa3[x].count("detalles") and 0<tpa3[x+1].count("detalle"):i=x+1
            if 0<tpa3[x].count("/detalles"):f=x+1
            x+=1
        producto=""
        while i<f:
            print(tpa3[0])
            if 0<tpa3[i].count("detalle") and 0==tpa3[i].count("/"):
                #print(tpa3[i])
                z1=0
                while z1<11:
                    if 0<tpa3[i+z1].count("descripcion>"):
                        #print("abanse en descripcion")
                        ile=ojo(False,tpa3[i+z1],ile)
                        producto=tpa3[i+z1]
                        producto=producto.replace("descripcion", "")
                        #producto=producto.replace("<", "")
                        #producto=producto.replace(">", "")
                        break
                    z1+=1
                z1=0
                while z1<11:
                    if 0<tpa3[i+z1-1].count("impuestos") and 0<tpa3[i+z1].count("impuesto"):
                        if 0<tpa3[i+z1+3].count("tarifa>") and 0<tpa3[i+z1+3].count("12") and 0<tpa3[i+z1+4].count("baseImponible>"):
                            ile[8]+=producto+" ="+tpa3[i+z1+4]+"|"
                            ile[8]=ile[8].replace("baseImponible", "")
                            ile[8]=ile[8].replace("<", "")
                            ile[8]=ile[8].replace(">", "")
                            ile[8]=ile[8].replace("/", "")
                            ile[8]=ile[8].replace("\t", "")
                            ile[8]=ile[8].replace(" ", "")
                    z1+=1  
            i+=1
        return ile

TaT = list(range(2));TaT[0]="[Tabla]";TaT[1]="\n"

x=0;li=1;timi=0;pu=False
ARK=input("FORMATO_DE_ARCHIVO:>");ile=list(range(14))
ile[0]="RUC";ile[1]="F-No.";ile[2]="";ile[3]="";ile[4]="";ile[5]="";ile[6]="";ile[7]="";ile[8]="";ile[9]="";ile[10]="";ile[11]="";ile[12]="";ile[13]=""
if ARK=="p" or ARK=="P" or ARK=="pdf" or ARK=="PDF":
    PI=input("FORMATO_Tabla:>")
    P=input("FORMATO_PDF.TXT:>")
    while x<len(pdfee):
        pdfee[x]=pdfee[x].replace("  ", "")
        if 0<pdfee[x].count("R.U.C.:"):
            pu=False
            print("FACTURA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            if PI!="r":ile[5]="IVA_12%"
            if P!="l":
                mip=pdfee[x].split(":")
                print(mip[1])
                ile[0]=str(mip[1].replace("\n", ""))
            else:
                print(pdfee[x+2])
                ile[0]=str(pdfee[x+2].replace("\n", ""))
            li+=1;ile[6]=""
        #if 2==pdfee[x].count("-"):ile[1]=str(pdfee[x].replace("\n", ""))
        if 0<pdfee[x].count("No."):
            print("Proseso No.", PI)
            if PI!="r":
                if P!="l" and ile[1]=="F-No.":
                    mip=pdfee[x].split(".")
                    print(mip[1])
                    ile[1]=str(mip[1].replace("\n", ""))
                else:
                    if 2==pdfee[x+2].count("-"):
                        print(pdfee[x+2])
                        ile[1]=str(pdfee[x+2].replace("\n", ""))          
                ile=estka(ile)
            if PI=="r" and ile[1]=="F-No.":
                print("Proseso No. R")
                mip=pdfee[x+2].split("-")
                print("Formato R", str(mip[0])+"-"+str(mip[1]), "...",str(mip[2]))
                ile[3]=str(mip[0])+"-"+str(mip[1])
                ile[4]=str(mip[2].replace("\n", ""))
        if 0<pdfee[x].count("NÚMERO DE AUTORIZACIÓN") and PI=="r":
            ile[1]="<"+pdfee[x+1].replace("\n", "")+">"
        if PI!="r":
            ile=ojo(False,pdfee[x],ile)
        if 0<pdfee[x].count("SUBTOTAL 12%") and PI=="r":
            print("modulo de 12%", pdfee[x+2])
            ile[6]=pdfee[x+2].replace("\n", "")
        if 0<pdfee[x].count("Identificaci") and PI!="r":
            if P!="l":
                ile[9]=pdfee[x]
                ile[9]=ile[9].replace(" ", "")
                ile[9]=ile[9].replace("Identificaci", "")
                ile[9]=ile[9].replace("\n", "")
        if 0<pdfee[x].count("SUBTOTAL 0%"):
            if PI=="r":
                print("modulo de 0%", pdfee[x+2])
                ile[7]=pdfee[x+2].replace("\n", "")
            else:
                if P=="l" and 0<pdfee[x+2].count("."):
                    if float(pdfee[x+2])>0 and ile[6]!="sospechoso":
                        ile[6]="<o>"
                if P!="l":
                    mip=pdfee[x].split("%")
                    print(mip)
                    if float(mip[len(mip)-1])>0 and ile[6]!="sospechoso":
                        ile[6]="<o>"
        if 0<pdfee[x].count("VALOR TOTAL") and pu==False:
            if PI=="r":
                print("Enmarcha---T", pdfee[x+2])
                ile[9]=pdfee[x+2].replace("\n", "")
                print("VALORES T:>",ile[7], ile[9])
            pu=True
            print(ile)
            TaT.append("\t".join(ile))
            ile[0]="RUC";ile[1]="F-No.";ile[2]="D";ile[3]="M";ile[4]="A";ile[5]="IVA_12%";ile[6]="CLAK";ile[7]="";ile[8]="";ile[9]="";ile[10]="";ile[11]="";ile[12]="";ile[13]=""
        if 0<pdfee[x].count("FECHA Y HORA DE"):timi+=1
        if 0<pdfee[x].count("Fecha"):timi+=1
        if 1<pdfee[x].count("/") and timi>1:
            mip=pdfee[x].split("/")
            map=mip[2].split(" ")
            print(str(mip[0]+"\t"+mip[1]+"\t"+mip[2]+"\t"))
            if PI!="r":
                ile[2] = str(mip[0])
                ile[3] = str(mip[1])
                ile[4] = str(map[0].replace("\n", ""))
            if PI=="r":
                ile[0]=str(mip[0])+"/"+str(mip[1])+"/"+str(map[0].replace("\n", ""))
            timi=0
        if 0<pdfee[x].count("IVA 12%"):
            if P!="l":
                mip=pdfee[x].split("%")
                print(mip[1])
                ile[5]=str(mip[1].replace("\n", ""))
            else:
                if PI!="r":
                    print(pdfee[x+2])
                    ile[5]=str(pdfee[x+2].replace("\n", ""))
                else:
                    ile[8]=str(pdfee[x+2].replace("\n", ""))
        x+=1
if ARK=="x":
    lu=input("Ingresar archibos_>")
    arXml=os.listdir(lu)
    print(arXml);xlf=0
    while xlf<len(arXml):
        ile[0]="RUC";ile[1]="F-No.";ile[2]="D";ile[3]="M";ile[4]="A";ile[5]="IVA_12%";ile[6]="";ile[7]="";ile[8]="";ile[9]="";ile[10]="";ile[11]="";ile[12]="";ile[13]=""
        harlik=ET.parse(lu+"\\"+arXml[xlf])
        raiz=harlik.getroot()
        for h in raiz:
            x+=1
            #print(x,h)
        #print(raiz[4].text)
        alf=(raiz[len(raiz)-2].text).split("\n")
        #print(alf[0])   C:\Users\User\Downloads\Factura.xml
        x=0
        while x<len(alf):
            if 0<alf[x].count("<ds"):
                break
            x+=1
        #print(x,alf[x])
        tpa3=""
        if x<3:
            tpa3=alf[0].split("><")
        else:tpa3=alf
        ile=analy(tpa3, ile)
        ile=estka(ile)
        ile[10]=arXml[xlf]
        print(arXml[xlf],">>>>>",ile)
        TaT.append("\t".join(ile))
        xlf+=1
sa="";x=0
while x < len(TaT):
    sa+=str(TaT[x])+"\n"
    #print(TaT[x])
    x+=1
#print(sa);sa=tpa2
reg=open("latabla.txt", "w")
reg.write(sa)
reg.close()
"""
Pmake (Python make)
"""
import importlib.util
import sys
import os
import locale

_config={
  "version": "1.0",
  "author": "Zoda",
  "license": "mit"
}

if "pmake.py" in os.listdir(os.getcwd()):
  spec = importlib.util.spec_from_file_location("module.name", "pmake.py")
  pmake = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(pmake)
else:
  print("Pmake Dosyası dizinde bulunamadı.")
  sys.exit()

try:
  pfunc=pmake.Pfunc
  if callable(pfunc):
    pass
  else:
    print(f"Pmake dosyasındaki Pmake objesinin bir sınıf olması gerekiyor. {type(pfunc)} değil")
    sys.exit()
except AttributeError:
  print("Pfunc sınıfı pmake dosyasında bulunamadı.")


pfunc.pmake_vars={"args":sys.argv,"lang":locale.getdefaultlocale()[0],"pmake_ver":_config["version"],"python_ver":sys.version.split()[0]}

try:
  if sys.argv[1] == "-d" or sys.argv[1] == "--description":
    try:
      print(pmake.description)
    except:
      print("Pmake dosyasında bir açıklama bulunamadı")

  elif sys.argv[1] == "-h":
    print(f"""Pmake
pmake <argüman yok>: standart fonksiyonu çalıştırır 
pmake -h: bu mesaj
pmake -v: Versiyonu gösterir
pmake <fonksiyon adı>:Pmake dosyasındaki Pfunc sınıfıdaki fonksiyonu çağırır""")

  elif sys.argv[1] == "-v":
    print(_config["version"])

  elif sys.argv[1] in pfunc.__dict__:
    if callable(pfunc.__dict__[sys.argv[1]]):  
      pfunc.__dict__[sys.argv[1]]()
    else:
      print(f"Pmake dosyasındaki Pfunc sınıfındaki {sys.argv[1]} bir fonksiyon değil")
  else:
    print(f"Argüman bulunamadı: {sys.argv[1]}")



except IndexError:
  if "all" in pfunc.__dict__:
    if callable(pfunc.__dict__["all"]):
      pfunc.all()
  else:
    print("Pmake Hiçbir İşlem Gerçekliştirmeden kapatıldı.")
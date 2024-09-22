# Robot Framework Installation Guide (เวอร์ชันภาษาไทย)


## ขั้นตอนที่ 1: ติดตั้ง Python
1. ดาวน์โหลด Python จาก [python.org](https://www.python.org/downloads/)
2. ติดตั้ง Python โดยเลือกตัวเลือก "Add Python to PATH" ในระหว่างการติดตั้ง
3. หลังจากติดตั้งเสร็จ คุณสามารถเปิด Command Prompt แล้วพิมพ์ python --version หรือ pip --version เพื่อตรวจสอบว่าทำงานได้หรือไม่ ถ้าทำงานได้แสดงว่า Python ถูกเพิ่มเข้า PATH เรียบร้อยแล้ว

## ขั้นตอนที่ 2: ติดตั้ง pip (ถ้ายังไม่ได้ติดตั้ง)
1. เปิด Terminal (macOS) หรือ Command Prompt (Windows)
2. รันคำสั่งต่อไปนี้เพื่อตรวจสอบว่ามี pip ติดตั้งอยู่แล้วหรือไม่:
  ```bash
   pip3 --version
  ```

หากไม่พบ ให้ดาวน์โหลด get-pip.py จาก get-pip.py และรันคำสั่ง:
  ```bash
  python get-pip.py
  ```
## ขั้นตอนที่ 3: ติดตั้งไฟล์
1. ดาวน์โหลดไฟล์ setup.py (จาก repository นี้) ลงเครื่อง
2. เข้าไปที่ directory ของไฟล์ที่ดาวน์โหลด
รันคำสั่งต่อไปนี้เพื่อติดตั้ง:
  ```bash
  pip3 install .
  ```
## ขั้นตอนที่ 4: ตั้งค่า PATH
### สำหรับ macOS
1. เปิด Terminal
2. แก้ไขไฟล์ .bash_profile (หรือ .zshrc สำหรับ zsh)
    ```bash
    vim ~/.bash_profile
    ```
   หรือถ้าใช้ zsh:
    ```bash
    vim ~/.zshrc
    ```
  เพิ่มบรรทัดต่อไปนี้ที่ส่วนท้ายของไฟล์
    ```bash
    export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
    ```
3. บันทึกและออกจาก Vim โดย กด Esc แล้วพิมพ์ :wq เพื่อบันทึกและออก
4. โหลดการตั้งค่าใหม่
  ```bash
  source ~/.bash_profile
  ```
หรือถ้าใช้ zsh:
  ```bash
  source ~/.zshrc
  ```

### สำหรับ Windows
1. คลิกขวาที่ "This PC" หรือ "My Computer" และเลือก "Properties"
2. คลิกที่ "Advanced system settings"
3. ในแท็บ "Advanced" คลิก "Environment Variables"
4. ใน "System variables" หาชื่อ "Path" แล้วคลิก "Edit"
5. คลิก "New" แล้วเพิ่มพาธที่ติดตั้ง Python เช่น:
  ```makefile
  C:\Python312\Scripts\
  C:\Python312\
```
6. คลิก "OK" เพื่อบันทึกการเปลี่ยนแปลง

## เสร็จสิ้น
ตอนนี้คุณสามารถใช้งาน Robot Framework ได้โดยรันคำสั่ง:
  ```bash
  robot --version
  ```

import qrcode

qr = qrcode.make("https://1drv.ms/p/s!AudQXTHqt_uz0w0EmUO4tphjfTFg?e=xGjcho")
qr.save("abstract,qr.png", scale = 8)

import cv2
a = {"name":"liushuai","age":30,"sex":"male"}
fs = cv2.FileStorage('config.yml',cv2.FILE_STORAGE_WRITE)
fs.write(name="info",val="message")
fs.write(name="name",val="python")
fs.release()
import cv2, time
# Crear Objeto
video=cv2.VideoCapture(1)

# Crear un objeto frame
check, frame = video.read() # Definicion de check
print(check)
print(frame) # Representar la imagen

# Mostrar el frame
cv2.imshow("capturing", frame)

# Apagar la Cámara
video.release()
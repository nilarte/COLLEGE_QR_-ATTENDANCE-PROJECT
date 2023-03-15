import time
import qrcode
import cv2

# Define a list of students as required for every class
students = ['Hritik', 'Rajnish', 'Shubham Parsad', 'Shuham Parshar', 'Vishal','Priyam']

# Generate QR code for each student
for student in students:
    # Create a unique code for each student
    qr_code = qrcode.make(student)
    
    # Save the QR code as an image file
    qr_code.save(f"{student}.png")

# Initialize camera
cap = cv2.VideoCapture(0)

# Load attendance list
attendance = {student: False for student in students}

# Capture video until 'q' key is pressed
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Display the frame
    cv2.imshow('frame', frame)
    
    # Decode QR code
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(frame)
    
    # Mark student as present
    if data in students:
        attendance[data] = True
    
    # Quit program when 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()

# Print attendance report
print("====================================")
print("      Attendance Report:")
print("====================================")
for student, present in attendance.items():
    status = "Present" if present else "Absent"
    print(f"{student}: {status}")

print("====================================")

import qrcode
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView


def generate_qr_code(request):
    # Replace 'http://example.com' with the URL of your open website project
    data = 'http://127.0.0.1:8000/verified/'
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file (optional)
    # img.save('path/to/save/qr_code.png')

    # Return the QR code as a response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response




import cv2
from django.shortcuts import render
from django.http import JsonResponse

def qr_code_scanner(request):
    # Use the computer's default camera (0) for scanning
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Initialize the QR code scanner
        qr_code_detector = cv2.QRCodeDetector()
        val, pts, qr_info = qr_code_detector.detectAndDecodeMulti(frame)

        # If QR code is detected, stop the camera and return the result
        if qr_info is not None:
            cap.release()
            cv2.destroyAllWindows()
            return JsonResponse({'qr_info': qr_info})

        cv2.imshow('QR Code Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return render(request, 'qr_scanner.html')





class qr_code_verified(TemplateView):
    template_name = "verify template.html"    
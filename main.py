import cv2
import mediapipe as mp
# import time
import numpy as np
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialisation de Mediapipe pour la détection des mains
detect_main = mp.solutions.hands
hands = detect_main.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Configuration de la webcam du caméra
cap = cv2.VideoCapture(0)

# Configuration de l'audio par le volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Obtention des valeurs minimales et maximales pour le volume
volume_min, volume_max = volume.GetVolumeRange()[:2]

# Redimensionner la fenêtre (optionnel)
cv2.namedWindow('Interaction Software', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Interaction Software', 1280, 720)

# Plein écran
# cv2.setWindowProperty('Interaction Software', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


def calculeDistanceMain(landmark1, landmark2):
    return hypot(landmark2.x - landmark1.x, landmark2.y - landmark1.y)


while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Conversion de l'image en RGB pour Mediapipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Revenir à BGR pour afficher avec OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, detect_main.HAND_CONNECTIONS)

            # Détection du pouce et de l'index
            thumb_tip = hand_landmarks.landmark[detect_main.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[detect_main.HandLandmark.INDEX_FINGER_TIP]

            # Calcul de la distance entre le pouce et l'index
            distance = calculeDistanceMain(thumb_tip, index_finger_tip)

            # Mise à l'échelle de la distance pour correspondre au volume
            volume_level = np.interp(distance, [0.02, 0.2], [volume_min, volume_max])

            # Ajustement du volume
            volume.SetMasterVolumeLevel(volume_level, None)

            # Affichage de la distance et du niveau de volume
            cv2.putText(image, f'Distance: {distance:.2f}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(image, f'Volume: {int(volume_level)}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Affichage de l'image
    cv2.imshow('Interaction Software', image)

    # Quitter la boucle si la touche "Esc" est appuyée
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()

# Commentaire du code précedent (efa mandeha)
"""import cv2
import mediapipe as mp
import time
import numpy as np
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialisation de Mediapipe pour la détection des mains
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Configuration de la webcam
cap = cv2.VideoCapture(0)

# Configuration de l'audio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Obtention des valeurs minimales et maximales pour le volume
vol_min, vol_max = volume.GetVolumeRange()[:2]

# Redimensionner la fenêtre (optionnel)
cv2.namedWindow('Hand Tracking', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Hand Tracking', 1280, 720)


# Plein écran (optionnel)
# cv2.setWindowProperty('Hand Tracking', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def calculate_distance(landmark1, landmark2):
    return hypot(landmark2.x - landmark1.x, landmark2.y - landmark1.y)


while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Conversion de l'image en RGB pour Mediapipe
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Revenir à BGR pour afficher avec OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Détection du pouce et de l'index
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calcul de la distance entre le pouce et l'index
            distance = calculate_distance(thumb_tip, index_finger_tip)

            # Mise à l'échelle de la distance pour correspondre au volume
            volume_level = np.interp(distance, [0.02, 0.2], [vol_min, vol_max])

            # Ajustement du volume
            volume.SetMasterVolumeLevel(volume_level, None)

            # Affichage de la distance et du niveau de volume
            cv2.putText(image, f'Distance: {distance:.2f}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(image, f'Volume: {int(volume_level)}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Affichage de l'image
    cv2.imshow('Hand Tracking', image)

    # Quitter la boucle si la touche "Esc" est appuyée
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()"""

import cv2
import numpy as np

def detect_dangerous_flame(frame):
    # 1. 將影像從 RGB 轉換為 HSV，HSV 更容易篩選特定顏色
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 2. 定義橘色火焰的範圍 (HSV 閥值)
    # 這些數值可以根據實際店內燈光進行微調
    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([25, 255, 255])
    
    # 3. 建立掩碼，過濾出橘色部分
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # 4. 去除噪音 (消除微小雜點)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # 5. 計算橘色像素的密度
    orange_pixel_count = cv2.countNonZero(mask)
    
    # 6. 安全判定與警報
    if orange_pixel_count > 500:  # 閥值可依攝影機距離調整
        status = "CRITICAL: INCOMPLETE COMBUSTION"
        color = (0, 0, 255) # 紅色警告
    else:
        status = "NORMAL: BLUE FLAME"
        color = (255, 0, 0) # 藍色正常
        
    return status, mask, color

# 這裡可以使用攝影機讀取：cap = cv2.VideoCapture(0)

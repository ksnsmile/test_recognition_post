# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 09:51:20 2025

@author: USER
"""

import easyocr
import os
from PIL import Image

# EasyOCR 리더 초기화
reader = easyocr.Reader(['ko', 'en'], model_storage_directory=r'C:\Users\USER\EasyOCR\workspace\user_network_dir', 
                            user_network_directory=r'C:\Users\USER\EasyOCR\workspace\user_network_dir', 
                            recog_network='custom')

# 이미지와 파일 경로 저장을 위한 딕셔너리
preprocessed_data = {}

# 이미지 폴더 경로 설정
folder_path = r'C:/Users/USER/Desktop//DB processing/data'
overall_results = []

# 이미지 파일을 폴더에서 불러오기
for file_name in os.listdir(folder_path):
    print(f"Loading {file_name}...")
    file_path = os.path.join(folder_path, file_name)
    
    try:
        # 이미지 열기 (RGB로 변환)
        image = Image.open(file_path).convert("RGB")
        
        # 이미지와 파일 경로를 딕셔너리에 저장
        preprocessed_data[file_name] = {
            'image': image,
            'file_path': file_path,
        }
        print(f"Successfully loaded {file_name}")
    except Exception as e:
        # 이미지 로딩 오류 처리
        print(f"Error loading {file_name}: {str(e)}")
        continue

# 각 이미지에 대해 OCR 처리
for file_name, data in preprocessed_data.items():
    print(f"\nProcessing image: {file_name}")
    print("-" * 50)
    
    try:
        # 이미지 입력
        print("이미지 처리 중...")
        image = data['image']
        
        # OCR 처리
        print("OCR 처리 중...")
        easyocr_results = reader.readtext(data['file_path'])
        print(f"OCR 결과: {len(easyocr_results)} items found")
        
        # 결과를 overall_results에 추가 (선택적)
        overall_results.append({
            'file_name': file_name,
            'ocr_results': easyocr_results
        })

    except Exception as e:
        # OCR 처리 중 오류 처리
        print(f"Error processing {file_name}: {str(e)}")


#첫번 째 택배 송장 데이터 results 리스트에 다 저장  

results=[]

ocr_results=overall_results[5]

a=ocr_results['ocr_results']


for result in ocr_results['ocr_results']:
    text = result[1]  # OCR 결과에서 텍스트만 가져오기
      
    results.append(text)





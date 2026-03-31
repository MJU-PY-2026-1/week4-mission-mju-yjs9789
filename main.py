# 파일이름 :main.py
# 작 성 자 :mju.3.31
bucket_list=[]
restaurant=input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant=input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

restaurant=input('맛집 리스트 입력: ')
bucket_list.append(restaurant)

print(f"리스트: {bucket_list}")

vip_restaurant=input('맛집 리스트 추가: ')
bucket_list.insert(0, restaurant)
print(f'리스트: {bucket_list}')

visited=input('도장 깨기: ')
bucket_list.remove(visited)
print(f'리스트: {bucket_list}')

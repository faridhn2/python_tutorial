import requests
src = 'https://dkstatics-public.digikala.com/digikala-products/bcdd98b2da5d830dc8aa7181f15e2ebf3e4598fa_1701084436.jpg'
response = requests.get(src)
with open('my_img.jpg','wb') as f:
    f.write(response.content)

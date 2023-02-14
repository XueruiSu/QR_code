
import segno
from segno import helpers
import datetime
vcard = helpers.make_vcard(
    name='Su;Xuerui',
    displayname='1',
    email=('bj2030592079@163.com'),
    url=[
        'https://github.com/XueruiSu'
    ],
    phone="18610633766",
    birthday=datetime.datetime.strptime('20001217', '%Y%m%d'),
    title='Wechat: su2030592079'
)
# vcard.to_artistic(background='src/albums.gif', target='albums.gif', scale=8)
img = vcard.to_pil(scale=6, dark="#FF7D92") 
img.save('Etsy.png')
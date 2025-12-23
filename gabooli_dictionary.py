def gabooli(rate):
    gabooli_dict={
               500:('کامپیوتر', ' تهران'),
              1500:('کامپیوتر', 'قم'),
              2500:('برق', 'قم'),
              3500:('فیزیک', 'تهران'),
              4500:('معماری', 'شیراز'),
              5500:('معماری', 'قم'),
              6500:('برق', 'قم'),
              7500:('شیمی', 'تهران'),
              8500:('شیمی', 'شیراز'),
              9500:('فیزیک', 'قم'),
              10500:('شیمی', 'قم')
              }
    if int(rate)<1:
         return f'not possible'
    if 1<=int(rate)<1000:
        return f'code 500,{gabooli_dict[500]}'
    elif 1000<=int(rate)<2000:
        return f'code 1500,{gabooli_dict[1500]}'
    elif 2000<=int(rate)<3000:
          return f'code 2500,{gabooli_dict[2500]}'
    elif 3000<=int(rate)<4000:
         return f'code 3500, {gabooli_dict[3500]}'
    elif 4000<=int(rate)<5000:
         return f'code 4500, {gabooli_dict[4500]}'
    elif 5000<=int(rate)<6000:
         return f'code 5500, {gabooli_dict[5500]}'
    elif 6000<=int(rate)<7000:
         return f'code 6500, {gabooli_dict[6500]}'
    elif 7000<=int(rate)<8000:
         return f'code 7500, {gabooli_dict[7500]}'
    elif 8000<=int(rate)<9000:
         return f'code 8500, {gabooli_dict[8500]}'
    elif 9000<=int(rate)<10000:
         return f'code 9500, {gabooli_dict[9500]}'
    elif 10000<=int(rate)<11000:
         return f'code 10500, {gabooli_dict[10500]}'
    else:
         return f'مردود'
    
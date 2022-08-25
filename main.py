male_female = input('Are you measuring a male or female? ')

male_list = ['male', 'Male', 'm', 'M']
female_list = ['female', 'Female', 'f', 'F']
if male_female in male_list:
  male_age = int(input('Enter age (in years (obviously)): '))
  skinfold_1 = float(input('Enter skinfold measurement #1: '))
  skinfold_2 = float(input('Enter skinfold measurement #2: '))
  skinfold_3 = float(input('Enter skinfold measurement #3: '))

  skinfold_sum = skinfold_1 + skinfold_2 + skinfold_3
  body_density_male = 1.10938 - (0.0008267 * skinfold_sum) + (0.0000016 * (skinfold_sum * skinfold_sum)) - (0.0002574 * male_age)
  #brozek body fat equation for males
  brozek_male = ((4.570/body_density_male) - 4.142) * 100
  print(f"Body Fat % is: {brozek_male}")
  
elif male_female in female_list:
  female_age = int(input('Enter age (in years (obviously)): '))
  skinfold_1 = float(input('Enter skinfold measurement #1: '))
  skinfold_2 = float(input('Enter skinfold measurement #2: '))
  skinfold_3 = float(input('Enter skinfold measurement #3: '))
  
  skinfold_sum = skinfold_1 + skinfold_2 + skinfold_3
  body_density_female = 1.0994921 - (0.0009929 * skinfold_sum) + (0.0000023 * (skinfold_sum * skinfold_sum)) - (0.0001392 * female_age)
  #brozek body fat equation for males
  brozek_female = ((4.570/body_density_female) - 4.142) * 100
  print(f"Body Fat % is: {brozek_female}")

else:
  print('no go')
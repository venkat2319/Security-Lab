alphabets = "abcdefghijklmnopqrstuvwxyz"
alpha_order = dict()
inv_alpha = dict()
for i,ch in enumerate(alphabets):
    alpha_order[ch] = i
    inv_alpha[i] = ch
  
#input for key(a,b) and Plain text
print("NOTE:- Keys should be Relative prime i.e. gcd(a,b) = 1.")   #gcd stands for greatest common divisor.
key = list(map(int, input("Enter key values a and b for key(a,b) :").split()))
plain_text = input("Enter plain text (only letters): ").lower().replace(" ", "")

encrypted = dict()
for char in set(plain_text):
  encrypted[char] = ''

a,b = key[0], key[1]
for ch in encrypted.keys():
  val = ( a * alpha_order[ch] + b )  % 26    # Ci = ( a * Pi + b ) mod 26
  encrypted[ch] = inv_alpha[val]

cipher_text=''
for ch in plain_text:
  if ch not in encrypted:
    cipher_text += ch
  else:
    cipher_text += encrypted[ch]

print("Plain text is  :", plain_text)
print("Cipher text is :", cipher_text)

def gcd(a, b): 
    if a == 0 : 
        return b  
    return gcd(b%a, a) 

# To find a inverse (a^-1) in m(m=26).
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

print("Cipher text is:",cipher_text)
my_keys = []
print("Hacked Keys might be:(See at the end,found key)")
for a in range(1,26,1):
  for b in range(26):
    if gcd(a,b)==1:   #as we know only 12*26 = 312 cases are there for Relative Prime.
      temp = ''

      a_inv = modInverse(a,26)
      for ch in cipher_text:
        if ch in alphabets:
          num = (alphabets.find(ch) - b ) *  a_inv     # Pi = [(Ci – b) * a^(-1) ] mod 26
          num = num % 26
          if num < 0:
            num = num + 26
          temp = temp + alphabets[num]
        else:
          temp = temp + ch
      if temp == plain_text:  #when predicted text is same as Plain text, keys has found.
        my_keys = [a,b]
      print("key(%d,%d) ::  %s " %(a,b,temp))

print("\n Key has found:- keys(%d,%d)"% (my_keys[0],my_keys[1]))

'''
NOTE:- Keys should be Relative prime i.e. gcd(a,b) = 1.
Enter key values a and b for key(a,b) : 5 11
5 11
Enter plain text (only letters): abcdefghijklmnoop
Plain text is  : abcdefghijklmnoop
Cipher text is : lqvafkpuzejotyddi
Cipher text is: lqvafkpuzejotyddi
Hacked Keys might be:(See at the end,found key)
key(1,0) ::  lqvafkpuzejotyddi 
key(1,1) ::  kpuzejotydinsxcch 
key(1,2) ::  jotydinsxchmrwbbg 
key(1,3) ::  insxchmrwbglqvaaf 
key(1,4) ::  hmrwbglqvafkpuzze 
key(1,5) ::  glqvafkpuzejotyyd 
key(1,6) ::  fkpuzejotydinsxxc 
key(1,7) ::  ejotydinsxchmrwwb 
key(1,8) ::  dinsxchmrwbglqvva 
key(1,9) ::  chmrwbglqvafkpuuz 
key(1,10) ::  bglqvafkpuzejotty 
key(1,11) ::  afkpuzejotydinssx 
key(1,12) ::  zejotydinsxchmrrw 
key(1,13) ::  ydinsxchmrwbglqqv 
key(1,14) ::  xchmrwbglqvafkppu 
key(1,15) ::  wbglqvafkpuzejoot 
key(1,16) ::  vafkpuzejotydinns 
key(1,17) ::  uzejotydinsxchmmr 
key(1,18) ::  tydinsxchmrwbgllq 
key(1,19) ::  sxchmrwbglqvafkkp 
key(1,20) ::  rwbglqvafkpuzejjo 
key(1,21) ::  qvafkpuzejotydiin 
key(1,22) ::  puzejotydinsxchhm 
key(1,23) ::  otydinsxchmrwbggl 
key(1,24) ::  nsxchmrwbglqvaffk 
key(1,25) ::  mrwbglqvafkpuzeej 
key(2,1) ::  kpuzejotydinsxcch 
key(2,3) ::  insxchmrwbglqvaaf 
key(2,5) ::  glqvafkpuzejotyyd 
key(2,7) ::  ejotydinsxchmrwwb 
key(2,9) ::  chmrwbglqvafkpuuz 
key(2,11) ::  afkpuzejotydinssx 
key(2,13) ::  ydinsxchmrwbglqqv 
key(2,15) ::  wbglqvafkpuzejoot 
key(2,17) ::  uzejotydinsxchmmr 
key(2,19) ::  sxchmrwbglqvafkkp 
key(2,21) ::  qvafkpuzejotydiin 
key(2,23) ::  otydinsxchmrwbggl 
key(2,25) ::  mrwbglqvafkpuzeej 
key(3,1) ::  mfyrkdwpibungzssl 
key(3,2) ::  dwpibungzslexqjjc 
key(3,4) ::  lexqjcvohatmfyrrk 
key(3,5) ::  cvohatmfyrkdwpiib 
key(3,7) ::  kdwpibungzslexqqj 
key(3,8) ::  bungzslexqjcvohha 
key(3,10) ::  jcvohatmfyrkdwppi 
key(3,11) ::  atmfyrkdwpibunggz 
key(3,13) ::  ibungzslexqjcvooh 
key(3,14) ::  zslexqjcvohatmffy 
key(3,16) ::  hatmfyrkdwpibunng 
key(3,17) ::  yrkdwpibungzsleex 
key(3,19) ::  gzslexqjcvohatmmf 
key(3,20) ::  xqjcvohatmfyrkddw 
key(3,22) ::  fyrkdwpibungzslle 
key(3,23) ::  wpibungzslexqjccv 
key(3,25) ::  exqjcvohatmfyrkkd 
key(4,1) ::  kpuzejotydinsxcch 
key(4,3) ::  insxchmrwbglqvaaf 
key(4,5) ::  glqvafkpuzejotyyd 
key(4,7) ::  ejotydinsxchmrwwb 
key(4,9) ::  chmrwbglqvafkpuuz 
key(4,11) ::  afkpuzejotydinssx 
key(4,13) ::  ydinsxchmrwbglqqv 
key(4,15) ::  wbglqvafkpuzejoot 
key(4,17) ::  uzejotydinsxchmmr 
key(4,19) ::  sxchmrwbglqvafkkp 
key(4,21) ::  qvafkpuzejotydiin 
key(4,23) ::  otydinsxchmrwbggl 
key(4,25) ::  mrwbglqvafkpuzeej 
key(5,1) ::  cdefghijklmnopqqr 
key(5,2) ::  hijklmnopqrstuvvw 
key(5,3) ::  mnopqrstuvwxyzaab 
key(5,4) ::  rstuvwxyzabcdeffg 
key(5,6) ::  bcdefghijklmnoppq 
key(5,7) ::  ghijklmnopqrstuuv 
key(5,8) ::  lmnopqrstuvwxyzza 
key(5,9) ::  qrstuvwxyzabcdeef 
key(5,11) ::  abcdefghijklmnoop 
key(5,12) ::  fghijklmnopqrsttu 
key(5,13) ::  klmnopqrstuvwxyyz 
key(5,14) ::  pqrstuvwxyzabcdde 
key(5,16) ::  zabcdefghijklmnno 
key(5,17) ::  efghijklmnopqrsst 
key(5,18) ::  jklmnopqrstuvwxxy 
key(5,19) ::  opqrstuvwxyzabccd 
key(5,21) ::  yzabcdefghijklmmn 
key(5,22) ::  defghijklmnopqrrs 
key(5,23) ::  ijklmnopqrstuvwwx 
key(5,24) ::  nopqrstuvwxyzabbc 
key(6,1) ::  kpuzejotydinsxcch 
key(6,5) ::  glqvafkpuzejotyyd 
key(6,7) ::  ejotydinsxchmrwwb 
key(6,11) ::  afkpuzejotydinssx 
key(6,13) ::  ydinsxchmrwbglqqv 
key(6,17) ::  uzejotydinsxchmmr 
key(6,19) ::  sxchmrwbglqvafkkp 
key(6,23) ::  otydinsxchmrwbggl 
key(6,25) ::  mrwbglqvafkpuzeej 
key(7,1) ::  urolifczwtqnkheeb 
key(7,2) ::  fczwtqnkhebyvsppm 
key(7,3) ::  qnkhebyvspmjgdaax 
key(7,4) ::  byvspmjgdaxurolli 
key(7,5) ::  mjgdaxurolifczwwt 
key(7,6) ::  xurolifczwtqnkhhe 
key(7,8) ::  tqnkhebyvspmjgdda 
key(7,9) ::  ebyvspmjgdaxurool 
key(7,10) ::  pmjgdaxurolifczzw 
key(7,11) ::  axurolifczwtqnkkh 
key(7,12) ::  lifczwtqnkhebyvvs 
key(7,13) ::  wtqnkhebyvspmjggd 
key(7,15) ::  spmjgdaxurolifccz 
key(7,16) ::  daxurolifczwtqnnk 
key(7,17) ::  olifczwtqnkhebyyv 
key(7,18) ::  zwtqnkhebyvspmjjg 
key(7,19) ::  khebyvspmjgdaxuur 
key(7,20) ::  vspmjgdaxuroliffc 
key(7,22) ::  rolifczwtqnkhebby 
key(7,23) ::  czwtqnkhebyvspmmj 
key(7,24) ::  nkhebyvspmjgdaxxu 
key(7,25) ::  yvspmjgdaxuroliif 
key(8,1) ::  kpuzejotydinsxcch 
key(8,3) ::  insxchmrwbglqvaaf 
key(8,5) ::  glqvafkpuzejotyyd 
key(8,7) ::  ejotydinsxchmrwwb 
key(8,9) ::  chmrwbglqvafkpuuz 
key(8,11) ::  afkpuzejotydinssx 
key(8,13) ::  ydinsxchmrwbglqqv 
key(8,15) ::  wbglqvafkpuzejoot 
key(8,17) ::  uzejotydinsxchmmr 
key(8,19) ::  sxchmrwbglqvafkkp 
key(8,21) ::  qvafkpuzejotydiin 
key(8,23) ::  otydinsxchmrwbggl 
key(8,25) ::  mrwbglqvafkpuzeej 
key(9,1) ::  etixmbqfujyncrggv 
key(9,2) ::  bqfujyncrgvkzodds 
key(9,4) ::  vkzodshwlapetixxm 
key(9,5) ::  shwlapetixmbqfuuj 
key(9,7) ::  mbqfujyncrgvkzood 
key(9,8) ::  jyncrgvkzodshwlla 
key(9,10) ::  dshwlapetixmbqffu 
key(9,11) ::  apetixmbqfujynccr 
key(9,13) ::  ujyncrgvkzodshwwl 
key(9,14) ::  rgvkzodshwlapetti 
key(9,16) ::  lapetixmbqfujynnc 
key(9,17) ::  ixmbqfujyncrgvkkz 
key(9,19) ::  crgvkzodshwlapeet 
key(9,20) ::  zodshwlapetixmbbq 
key(9,22) ::  tixmbqfujyncrgvvk 
key(9,23) ::  qfujyncrgvkzodssh 
key(9,25) ::  kzodshwlapetixmmb 
key(10,1) ::  kpuzejotydinsxcch 
key(10,3) ::  insxchmrwbglqvaaf 
key(10,7) ::  ejotydinsxchmrwwb 
key(10,9) ::  chmrwbglqvafkpuuz 
key(10,11) ::  afkpuzejotydinssx 
key(10,13) ::  ydinsxchmrwbglqqv 
key(10,17) ::  uzejotydinsxchmmr 
key(10,19) ::  sxchmrwbglqvafkkp 
key(10,21) ::  qvafkpuzejotydiin 
key(10,23) ::  otydinsxchmrwbggl 
key(11,1) ::  izqhypgxofwnevmmd 
key(11,2) ::  pgxofwnevmdulcttk 
key(11,3) ::  wnevmdulctkbsjaar 
key(11,4) ::  dulctkbsjarizqhhy 
key(11,5) ::  kbsjarizqhypgxoof 
key(11,6) ::  rizqhypgxofwnevvm 
key(11,7) ::  ypgxofwnevmdulcct 
key(11,8) ::  fwnevmdulctkbsjja 
key(11,9) ::  mdulctkbsjarizqqh 
key(11,10) ::  tkbsjarizqhypgxxo 
key(11,12) ::  hypgxofwnevmdullc 
key(11,13) ::  ofwnevmdulctkbssj 
key(11,14) ::  vmdulctkbsjarizzq 
key(11,15) ::  ctkbsjarizqhypggx 
key(11,16) ::  jarizqhypgxofwnne 
key(11,17) ::  qhypgxofwnevmduul 
key(11,18) ::  xofwnevmdulctkbbs 
key(11,19) ::  evmdulctkbsjariiz 
key(11,20) ::  lctkbsjarizqhyppg 
key(11,21) ::  sjarizqhypgxofwwn 
key(11,23) ::  gxofwnevmdulctkkb 
key(11,24) ::  nevmdulctkbsjarri 
key(11,25) ::  ulctkbsjarizqhyyp 
key(12,1) ::  kpuzejotydinsxcch 
key(12,5) ::  glqvafkpuzejotyyd 
key(12,7) ::  ejotydinsxchmrwwb 
key(12,11) ::  afkpuzejotydinssx 
key(12,13) ::  ydinsxchmrwbglqqv 
key(12,17) ::  uzejotydinsxchmmr 
key(12,19) ::  sxchmrwbglqvafkkp 
key(12,23) ::  otydinsxchmrwbggl 
key(12,25) ::  mrwbglqvafkpuzeej 
key(13,1) ::  kpuzejotydinsxcch 
key(13,2) ::  jotydinsxchmrwbbg 
key(13,3) ::  insxchmrwbglqvaaf 
key(13,4) ::  hmrwbglqvafkpuzze 
key(13,5) ::  glqvafkpuzejotyyd 
key(13,6) ::  fkpuzejotydinsxxc 
key(13,7) ::  ejotydinsxchmrwwb 
key(13,8) ::  dinsxchmrwbglqvva 
key(13,9) ::  chmrwbglqvafkpuuz 
key(13,10) ::  bglqvafkpuzejotty 
key(13,11) ::  afkpuzejotydinssx 
key(13,12) ::  zejotydinsxchmrrw 
key(13,14) ::  xchmrwbglqvafkppu 
key(13,15) ::  wbglqvafkpuzejoot 
key(13,16) ::  vafkpuzejotydinns 
key(13,17) ::  uzejotydinsxchmmr 
key(13,18) ::  tydinsxchmrwbgllq 
key(13,19) ::  sxchmrwbglqvafkkp 
key(13,20) ::  rwbglqvafkpuzejjo 
key(13,21) ::  qvafkpuzejotydiin 
key(13,22) ::  puzejotydinsxchhm 
key(13,23) ::  otydinsxchmrwbggl 
key(13,24) ::  nsxchmrwbglqvaffk 
key(13,25) ::  mrwbglqvafkpuzeej 
key(14,1) ::  kpuzejotydinsxcch 
key(14,3) ::  insxchmrwbglqvaaf 
key(14,5) ::  glqvafkpuzejotyyd 
key(14,9) ::  chmrwbglqvafkpuuz 
key(14,11) ::  afkpuzejotydinssx 
key(14,13) ::  ydinsxchmrwbglqqv 
key(14,15) ::  wbglqvafkpuzejoot 
key(14,17) ::  uzejotydinsxchmmr 
key(14,19) ::  sxchmrwbglqvafkkp 
key(14,23) ::  otydinsxchmrwbggl 
key(14,25) ::  mrwbglqvafkpuzeej 
key(15,1) ::  sbktcludmvenwfoox 
key(15,2) ::  ludmvenwfoxgpyhhq 
key(15,4) ::  xgpyhqzirajsbkttc 
key(15,7) ::  cludmvenwfoxgpyyh 
key(15,8) ::  venwfoxgpyhqzirra 
key(15,11) ::  ajsbktcludmvenwwf 
key(15,13) ::  mvenwfoxgpyhqziir 
key(15,14) ::  foxgpyhqzirajsbbk 
key(15,16) ::  rajsbktcludmvennw 
key(15,17) ::  ktcludmvenwfoxggp 
key(15,19) ::  wfoxgpyhqzirajssb 
key(15,22) ::  bktcludmvenwfoxxg 
key(15,23) ::  udmvenwfoxgpyhqqz 
key(16,1) ::  kpuzejotydinsxcch 
key(16,3) ::  insxchmrwbglqvaaf 
key(16,5) ::  glqvafkpuzejotyyd 
key(16,7) ::  ejotydinsxchmrwwb 
key(16,9) ::  chmrwbglqvafkpuuz 
key(16,11) ::  afkpuzejotydinssx 
key(16,13) ::  ydinsxchmrwbglqqv 
key(16,15) ::  wbglqvafkpuzejoot 
key(16,17) ::  uzejotydinsxchmmr 
key(16,19) ::  sxchmrwbglqvafkkp 
key(16,21) ::  qvafkpuzejotydiin 
key(16,23) ::  otydinsxchmrwbggl 
key(16,25) ::  mrwbglqvafkpuzeej 
key(17,1) ::  whsdozkvgrcnyjuuf 
key(17,2) ::  zkvgrcnyjufqbmxxi 
key(17,3) ::  cnyjufqbmxitepaal 
key(17,4) ::  fqbmxitepalwhsddo 
key(17,5) ::  itepalwhsdozkvggr 
key(17,6) ::  lwhsdozkvgrcnyjju 
key(17,7) ::  ozkvgrcnyjufqbmmx 
key(17,8) ::  rcnyjufqbmxiteppa 
key(17,9) ::  ufqbmxitepalwhssd 
key(17,10) ::  xitepalwhsdozkvvg 
key(17,11) ::  alwhsdozkvgrcnyyj 
key(17,12) ::  dozkvgrcnyjufqbbm 
key(17,13) ::  grcnyjufqbmxiteep 
key(17,14) ::  jufqbmxitepalwhhs 
key(17,15) ::  mxitepalwhsdozkkv 
key(17,16) ::  palwhsdozkvgrcnny 
key(17,18) ::  vgrcnyjufqbmxitte 
key(17,19) ::  yjufqbmxitepalwwh 
key(17,20) ::  bmxitepalwhsdozzk 
key(17,21) ::  epalwhsdozkvgrccn 
key(17,22) ::  hsdozkvgrcnyjuffq 
key(17,23) ::  kvgrcnyjufqbmxiit 
key(17,24) ::  nyjufqbmxitepallw 
key(17,25) ::  qbmxitepalwhsdooz 
key(18,1) ::  kpuzejotydinsxcch 
key(18,5) ::  glqvafkpuzejotyyd 
key(18,7) ::  ejotydinsxchmrwwb 
key(18,11) ::  afkpuzejotydinssx 
key(18,13) ::  ydinsxchmrwbglqqv 
key(18,17) ::  uzejotydinsxchmmr 
key(18,19) ::  sxchmrwbglqvafkkp 
key(18,23) ::  otydinsxchmrwbggl 
key(18,25) ::  mrwbglqvafkpuzeej 
key(19,1) ::  gjmpsvybehknqtwwz 
key(19,2) ::  vybehknqtwzcfillo 
key(19,3) ::  knqtwzcfiloruxaad 
key(19,4) ::  zcfiloruxadgjmpps 
key(19,5) ::  oruxadgjmpsvybeeh 
key(19,6) ::  dgjmpsvybehknqttw 
key(19,7) ::  svybehknqtwzcfiil 
key(19,8) ::  hknqtwzcfiloruxxa 
key(19,9) ::  wzcfiloruxadgjmmp 
key(19,10) ::  loruxadgjmpsvybbe 
key(19,11) ::  adgjmpsvybehknqqt 
key(19,12) ::  psvybehknqtwzcffi 
key(19,13) ::  ehknqtwzcfiloruux 
key(19,14) ::  twzcfiloruxadgjjm 
key(19,15) ::  iloruxadgjmpsvyyb 
key(19,16) ::  xadgjmpsvybehknnq 
key(19,17) ::  mpsvybehknqtwzccf 
key(19,18) ::  behknqtwzcfilorru 
key(19,20) ::  filoruxadgjmpsvvy 
key(19,21) ::  uxadgjmpsvybehkkn 
key(19,22) ::  jmpsvybehknqtwzzc 
key(19,23) ::  ybehknqtwzcfiloor 
key(19,24) ::  nqtwzcfiloruxaddg 
key(19,25) ::  cfiloruxadgjmpssv 
key(20,1) ::  kpuzejotydinsxcch 
key(20,3) ::  insxchmrwbglqvaaf 
key(20,7) ::  ejotydinsxchmrwwb 
key(20,9) ::  chmrwbglqvafkpuuz 
key(20,11) ::  afkpuzejotydinssx 
key(20,13) ::  ydinsxchmrwbglqqv 
key(20,17) ::  uzejotydinsxchmmr 
key(20,19) ::  sxchmrwbglqvafkkp 
key(20,21) ::  qvafkpuzejotydiin 
key(20,23) ::  otydinsxchmrwbggl 
key(21,1) ::  yxwvutsrqponmlkkj 
key(21,2) ::  tsrqponmlkjihgffe 
key(21,4) ::  jihgfedcbazyxwvvu 
key(21,5) ::  edcbazyxwvutsrqqp 
key(21,8) ::  ponmlkjihgfedcbba 
key(21,10) ::  fedcbazyxwvutsrrq 
key(21,11) ::  azyxwvutsrqponmml 
key(21,13) ::  qponmlkjihgfedccb 
key(21,16) ::  bazyxwvutsrqponnm 
key(21,17) ::  wvutsrqponmlkjiih 
key(21,19) ::  mlkjihgfedcbazyyx 
key(21,20) ::  hgfedcbazyxwvutts 
key(21,22) ::  xwvutsrqponmlkjji 
key(21,23) ::  srqponmlkjihgfeed 
key(21,25) ::  ihgfedcbazyxwvuut 
key(22,1) ::  kpuzejotydinsxcch 
key(22,3) ::  insxchmrwbglqvaaf 
key(22,5) ::  glqvafkpuzejotyyd 
key(22,7) ::  ejotydinsxchmrwwb 
key(22,9) ::  chmrwbglqvafkpuuz 
key(22,13) ::  ydinsxchmrwbglqqv 
key(22,15) ::  wbglqvafkpuzejoot 
key(22,17) ::  uzejotydinsxchmmr 
key(22,19) ::  sxchmrwbglqvafkkp 
key(22,21) ::  qvafkpuzejotydiin 
key(22,23) ::  otydinsxchmrwbggl 
key(22,25) ::  mrwbglqvafkpuzeej 
key(23,1) ::  ovcjqxelszgnubiip 
key(23,2) ::  xelszgnubipwdkrry 
key(23,3) ::  gnubipwdkryfmtaah 
key(23,4) ::  pwdkryfmtahovcjjq 
key(23,5) ::  yfmtahovcjqxelssz 
key(23,6) ::  hovcjqxelszgnubbi 
key(23,7) ::  qxelszgnubipwdkkr 
key(23,8) ::  zgnubipwdkryfmtta 
key(23,9) ::  ipwdkryfmtahovccj 
key(23,10) ::  ryfmtahovcjqxells 
key(23,11) ::  ahovcjqxelszgnuub 
key(23,12) ::  jqxelszgnubipwddk 
key(23,13) ::  szgnubipwdkryfmmt 
key(23,14) ::  bipwdkryfmtahovvc 
key(23,15) ::  kryfmtahovcjqxeel 
key(23,16) ::  tahovcjqxelszgnnu 
key(23,17) ::  cjqxelszgnubipwwd 
key(23,18) ::  lszgnubipwdkryffm 
key(23,19) ::  ubipwdkryfmtahoov 
key(23,20) ::  dkryfmtahovcjqxxe 
key(23,21) ::  mtahovcjqxelszggn 
key(23,22) ::  vcjqxelszgnubippw 
key(23,24) ::  nubipwdkryfmtahho 
key(23,25) ::  wdkryfmtahovcjqqx 
key(24,1) ::  kpuzejotydinsxcch 
key(24,5) ::  glqvafkpuzejotyyd 
key(24,7) ::  ejotydinsxchmrwwb 
key(24,11) ::  afkpuzejotydinssx 
key(24,13) ::  ydinsxchmrwbglqqv 
key(24,17) ::  uzejotydinsxchmmr 
key(24,19) ::  sxchmrwbglqvafkkp 
key(24,23) ::  otydinsxchmrwbggl 
key(24,25) ::  mrwbglqvafkpuzeej 
key(25,1) ::  qlgbwrmhcxsnidyyt 
key(25,2) ::  rmhcxsnidytojezzu 
key(25,3) ::  snidytojezupkfaav 
key(25,4) ::  tojezupkfavqlgbbw 
key(25,6) ::  vqlgbwrmhcxsniddy 
key(25,7) ::  wrmhcxsnidytojeez 
key(25,8) ::  xsnidytojezupkffa 
key(25,9) ::  ytojezupkfavqlggb 
key(25,11) ::  avqlgbwrmhcxsniid 
key(25,12) ::  bwrmhcxsnidytojje 
key(25,13) ::  cxsnidytojezupkkf 
key(25,14) ::  dytojezupkfavqllg 
key(25,16) ::  favqlgbwrmhcxsnni 
key(25,17) ::  gbwrmhcxsnidytooj 
key(25,18) ::  hcxsnidytojezuppk 
key(25,19) ::  idytojezupkfavqql 
key(25,21) ::  kfavqlgbwrmhcxssn 
key(25,22) ::  lgbwrmhcxsnidytto 
key(25,23) ::  mhcxsnidytojezuup 
key(25,24) ::  nidytojezupkfavvq 

 Key has found:- keys(5,11)
'''
